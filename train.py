from ultralytics import YOLO

model = YOLO("yolo26n.pt")
model.train(data="dataset/data.yaml", epochs=1, batch=1, device="cpu", workers=0, project="runs", name="person_smoke_test", )