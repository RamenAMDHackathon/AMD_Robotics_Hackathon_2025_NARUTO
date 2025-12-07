from ultralytics import YOLO

# YOLOv11n
# model_n = YOLO("yolo11n.pt")
# model_n.train(data="./yolo_dataset/data.yaml", epochs=100, imgsz=640, batch=4, name="yolo11n_bottle_cup")
# model_n.save("yolo11n_bottle_cup.pt")

# YOLOv11s
# model_s = YOLO("yolo11s.pt")
# result_s = model_s.train(data="./yolo_dataset/data.yaml", epochs=100, imgsz=640, batch=4, name="yolo11s_bottle_cup")
# model_s.save("yolo11s_bottle_cup.pt")

model_s = YOLO("yolo11m.pt")
result_s = model_s.train(data="./yolo_dataset/data.yaml", epochs=100, imgsz=1280, batch=4,freeze=10,lr0=0.001, name="yolo11m_bottle_cup")
model_s.save("yolo11m_bottle_cup.pt")