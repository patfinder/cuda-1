import numpy as np
from numba import cuda, jit
import time

# Define array size
N = 10**7 # 10 million elements

# CPU function
def cpu_multiply(a, b, out):
    for i in range(N):
        out[i] = a[i] * b[i]

# CUDA GPU kernel
@cuda.jit
def gpu_multiply_kernel(a, b, out):
    idx = cuda.grid(1)
    if idx < N:
        out[idx] = a[idx] * b[idx]

# Main execution
if __name__ == "__main__":
    # Initialize arrays
    a_cpu = np.random.rand(N)
    b_cpu = np.random.rand(N)
    out_cpu = np.empty_like(a_cpu)

    # CPU execution
    start_time = time.perf_counter()
    cpu_multiply(a_cpu, b_cpu, out_cpu)
    cpu_time = time.perf_counter() - start_time
    print(f"CPU time: {cpu_time:.6f} seconds")

    # GPU execution (requires a CUDA-enabled GPU)
    try:
        # Allocate memory on the device
        a_gpu = cuda.to_device(a_cpu)
        b_gpu = cuda.to_device(b_cpu)
        out_gpu = cuda.device_array_like(out_cpu)

        # Configure the blocks and threads per block
        threads_per_block = 256
        blocks_per_grid = (N + threads_per_block - 1) // threads_per_block

        start_time = time.perf_counter()
        gpu_multiply_kernel[blocks_per_grid, threads_per_block](a_gpu, b_gpu, out_gpu)
        cuda.synchronize() # Wait for GPU to finish
        gpu_time = time.perf_counter() - start_time
        print(f"GPU time: {gpu_time:.6f} seconds")

        # Verify results (optional)
        # out_host = out_gpu.copy_to_host()
        # assert np.allclose(out_cpu, out_host)

    except Exception as e:
        print(f"GPU execution failed: {e}. Ensure you have a CUDA-enabled GPU and Numba with CUDA support installed.")

