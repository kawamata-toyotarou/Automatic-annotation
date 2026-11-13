import time          #time.sleep関数を使用するため

import pyrealsense2  #

pipeline = pyrealsense2.pipeline() # pipeline はカメラからデータを受け取るためのオブジェクト
config = pyrealsense2.config()
config.enable_stream(pyrealsense2, 640, 480, pyrealsense2.stream.depth, 640, 480, pyrealsense2.format.z16, 30)

pipeline.start(config)

try:
    while True:
        frames = pipeline.wait_for_frames()
        depth = frames.get_depth_frame()
        if not depth:
            continue

        x = depth.get_width()  // 2
        y = depth.get_height() // 2
        distance = depth.get_distance(x, y)

        if distance > 0:
            print(f"中央の深度: {distance:.2f} m")
        else:
            print("中央の深度: 測定できません")

        time.sleep(0.2)
except KeyboardInterrupt:
    pass
finally:
    pipeline.stop()