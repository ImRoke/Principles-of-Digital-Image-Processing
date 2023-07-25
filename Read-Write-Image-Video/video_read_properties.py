import cv2

def read_video(video_path):
    # Reading a video
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Unable to open the video at '{video_path}'")
        return

    # Getting video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))


    # Major capture properties
    # print(f"FRAME_WIDTH :   '{cap.get(cv2.CAP_PROP_FRAME_WIDTH)}'")
    # print(f"FRAME_HEIGHT :  '{cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}'")
    # print(f"FPS :           '{cap.get(cv2.CAP_PROP_FPS)}'")
    # print(f"POS_MSEC :      '{cap.get(cv2.CAP_PROP_POS_MSEC)}'")
    # print(f"FRAME_COUNT :   '{cap.get(cv2.CAP_PROP_FRAME_COUNT)}'")
    # print(f"BRIGHTNESS :    '{cap.get(cv2.CAP_PROP_BRIGHTNESS)}'")
    # print(f"CONTRAST :      '{cap.get(cv2.CAP_PROP_CONTRAST)}'")
    # print(f"SATURATION :    '{cap.get(cv2.CAP_PROP_SATURATION)}'")
    # print(f"HUE :           '{cap.get(cv2.CAP_PROP_HUE)}'")
    # print(f"GAIN :          '{cap.get(cv2.CAP_PROP_GAIN)}'")
    # print(f"RGB :           '{cap.get(cv2.CAP_PROP_CONVERT_RGB)}'")

    print(f"Video Path: {video_path}")
    print(f"Frame Width: {frame_width}")
    print(f"Frame Height: {frame_height}")
    print(f"FPS: {fps}")
    print(f"Total Frame Count: {frame_count}")

    while True:
        isTrue, frame = cap.read()

        if not isTrue:
            break

        cv2.imshow('Video', frame)

        # It'll show the video window for 25ms and quits if the user presses "q"
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # To close the video capture and all the windows        
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = 'place your video file here'
    read_video(video_path)
