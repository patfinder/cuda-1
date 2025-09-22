
<!-- ======================================================= -->

nvidia-smi

21:53 $ nvidia-smi 
Sun Sep 21 21:56:02 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.82.09              Driver Version: 580.82.09      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce GTX 960         Off |   00000000:03:00.0 Off |                  N/A |
|  0%   45C    P8             14W /  160W |       0MiB /   2048MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+

<!-- ======================================================= -->


<!-- https://docs.nvidia.com/cuda/cuda-installation-guide-linux/ -->

21:59 $ lspci | grep -i nvidia
 
02:00.0 VGA compatible controller: NVIDIA Corporation GF119 [NVS 310] (rev a1)
02:00.1 Audio device: NVIDIA Corporation GF119 HDMI Audio Controller (rev a1)
03:00.0 VGA compatible controller: NVIDIA Corporation GM206 [GeForce GTX 960] (rev a1)
03:00.1 Audio device: NVIDIA Corporation GM206 High Definition Audio Controller (rev a1)


<!-- ======================================================= -->

hostnamectl

22:02 $ hostnamectl 
 Static hostname: vuong-HP-Z440-Workstation
       Icon name: computer-desktop
         Chassis: desktop 🖥️
      Machine ID: 3ecec3fa885b4bcd96e004be86520a7c
         Boot ID: cd72a078ab7246389f40b6ad2fbdabbc
Operating System: Ubuntu 24.04.2 LTS              
          Kernel: Linux 6.14.0-29-generic
    Architecture: x86-64
 Hardware Vendor: Hewlett-Packard
  Hardware Model: HP Z440 Workstation
Firmware Version: M60 v02.38
   Firmware Date: Wed 2017-11-08
    Firmware Age: 7y 10month 1w 6d                



<!-- ======================================================= -->
Download the NVIDIA CUDA Toolkit
https://developer.nvidia.com/cuda-downloads


sudo dpkg -i cuda-repo-ubuntu2404-13-0-local_13.0.1-580.82.07-1_amd64.deb

<!-- ======================================================= -->


<!-- ======================================================= -->


<!-- ======================================================= -->


<!-- ======================================================= -->


<!-- ======================================================= -->


