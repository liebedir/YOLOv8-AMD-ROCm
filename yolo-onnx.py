from ultralytics import YOLO
import torch, time
import onnxruntime as ort

# 设定推理设备为CPU，可根据实际情况改为"GPU"或"NPU"

device = "GPU"

if device == "GPU":
        providers = providers=['ROCMExecutionProvider']
else:
        providers = providers = ['CPUExecutionProvider']

IMAGE_PATH = r"/home/avnet/yolo/images/train2017/000000000143.jpg"

# 用Ultralytics工具包 API实现yolov8-seg模型推理程序
seg_model = YOLO("yolov8n-seg.pt",task="segment")
seg_model(IMAGE_PATH)


ovep_model = ort.InferenceSession("yolov8n-seg.onnx", None, 
                           providers=["ROCMExecutionProvider"])
input_names = ovep_model.get_inputs()[0].name
outputs = ovep_model.get_outputs()
output_names = list(map(lambda output:output.name, outputs))

# 2. 用onnxruntime替代YOLOv8-seg的原生推理计算方法
def ovep_infer(*args):
    result = ovep_model.run(output_names, {input_names: args[0].cpu().numpy()})
    return torch.from_numpy(result[0]), torch.from_numpy(result[1])

seg_model.predictor.inference = ovep_infer
seg_model.predictor.model.pt = False

# 复用YOLOv8-seg的原生前后处理程序
for i in range(1000):

        seg_model(IMAGE_PATH, show=True)

# 让推理结果显示6秒
        # time.sleep()