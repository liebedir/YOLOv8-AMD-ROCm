# YOLOv8-AMD-ROCm

## Introduction
YOLOv8-AMD-ROCM is a demo to show how to deloy YOLOV8 on AMD GPU&iGPU.

This picture shows the time consumption of CPU inference and iGPU inference on AMD HX370.

<div style = "text-align: center">
	<image src = "./images/res.png">
</div>


## Installation
The most necessary dependencies for deploying onnx model on AMD GPU are:
- [ROCm](https://github.com/ROCm/ROCm)
- [ROCm-onnxruntime](https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/native_linux/install-onnx.html)

Now we know which ROCm and Onnxruntime-ROCm version should be installed.

Install ROCm, follow [the link]( https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html) to install the ROCm. We need to change the url https://repo.radeon.com/amdgpu-install/6.4.3/ubuntu/jammy/amdgpu-install_6.4.60403-1_all.deb to install the ROCm you want.
<div style="text-align: center">
    <image src = "./images/rocm-version.png">
</div>

If you are using AMD Ryzen CPU and want to use the iGPU to do inference, need to set a environment variable and the value of variable is based on the iGPU architecture. If you are using Ryzen 8000 or HX 300 series CPU, your iGPU architecture is RDNA3, you need to do "export HSA_OVERRIDE_GFX_VERISON=11.0.0". This step is important, you iGPU can support Pytorch and other AI framework by doing this.

<div style="text-align: center">
    <image src = "./images/HSA.png">
</div>

Install the onnxruntime-rocm. 
```bash
pip3 install onnxruntime-rocm -f https://repo.radeon.com/rocm/manylinux/rocm-rel-x.x.x/
```

Set the url based the ROCm verison installed. Please refer to [this link]( https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/native_linux/install-onnx.html)

Start YOLOv8 test
```bash
python yolo-onnx.py
```

<div style = "text-align: center">
	<image src = "./images/res.png">
</div>
