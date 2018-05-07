import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer

def CaptureVideo(video_path):
    video=cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    while True:
        grabbed, frame=video.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            # print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.putText(frame, 'Press Q To Quit', (50,50), cv2.FONT_HERSHEY_DUPLEX, 0.8, 255)
        cv2.imshow(video_path.split("\\")[len(video_path.split("\\"))-1].split(".")[0], frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    video.release()
    cv2.destroyAllWindows()