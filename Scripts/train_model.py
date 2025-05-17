from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # Nano version
model.train(data='dataset/data.yaml', epochs=30, imgsz=640)
model.export(format='onnx')  # Optional
