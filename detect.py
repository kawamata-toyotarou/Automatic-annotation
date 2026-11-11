from ultralytics import YOLO  # YOLOの読み込み

model = YOLO("yolo26n.pt")     # 学習済みモデルを使えるように
model.predict("capture.jpg", classes=[0], save=True) # model.predictに調べたい画像を入れ、classes=[0]で人だけを表示対象に、save = Trueで枠を描いた結果画像が保存