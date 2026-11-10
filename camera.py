import cv2                            # openCVを読み込み

camera = cv2.VideoCapture(0)          # 番号0のカメラを起動

try:                                  # ここから先の処理を実行 処理が終わるときは、途中でエラーが起きた場合も、下の finally に
    if not camera.isOpened():           # カメラが開けたかを調べる
        raise RuntimeError("カメラが起動できませんでした") # カメラが開けなかったとき、理由が分かるメッセージ付きでエラーを発生

    while True:
        ok, frame = camera.read()
        if not ok:
            raise RuntimeError("カメラから画像を取得できませんでした")
        
        cv2.imshow("Camera", frame)   # Camera という名前のウィンドウに、今読み取った frame を表示
        if cv2.waitKey(1) == ord("q"):# aitKey(1) でウィンドウの表示更新やキー入力を処理 qで処理を抜ける
            break

finally:                              # tryが終わったら実行される javascritpのエラー時のcatchとは少し違う                      
    camera.release()                  # プログラムが使っていたカメラを解放
    cv2.destroyAllWindows()           # このプログラムがOpenCVで開いた表示ウィンドウをすべて閉じる
        