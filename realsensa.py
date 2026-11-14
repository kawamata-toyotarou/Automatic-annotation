import time          # time.sleep関数を使用するため

import pyrealsense2  # PythonからRealSenseを操作するためのライブラリを読み込み

pipeline = pyrealsense2.pipeline() # pipeline はカメラからデータを受け取るためのオブジェクトを作成
config = pyrealsense2.config()     # どの種類のデータを、どんな設定で受け取るかを指定するオブジェクトを作成
config.enable_stream(pyrealsense2.stream.depth, 640, 480, pyrealsense2.format.z16, 30) # 深度画像・幅640・高さ480・16ビット形式・毎秒30フレームの順で指定

pipeline.start(config)             # config の設定を使って、カメラからのデータ受信を開始

try:
    while True:
        frames = pipeline.wait_for_frames() # 新しいフレームのまとまりが届くまで待つ、5秒でタイムアウト
        depth = frames.get_depth_frame()    # 届いたフレームのまとまりから、深度画像を取り出し
        if not depth:
            continue

        x = depth.get_width()  // 2         # 画像の幅を半分にして、中央の横座標を求める
        y = depth.get_height() // 2         # 画像の高さを半分にして、中央の縦座標を求める
        distance = depth.get_distance(x, y) # (x, y) にある1ピクセルの深度をメートルで取得

        if distance > 0:
            print(f"中央の深度: {distance:.2f} m")
        else:
            print("中央の深度: 測定できません")

        time.sleep(0.2)                     # 0.2秒待ち
except KeyboardInterrupt:                   # Ctrl+C による中断を受け取る
    pass
finally:
    pipeline.stop()                         #ストリームを停止し、カメラを解放