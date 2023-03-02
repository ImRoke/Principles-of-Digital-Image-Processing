import cv2

# Reading a video by giving the exact file name
# You can also read stored video in system by giving the address like 'C:/Users/username/...'
# To read a video from available devices, 
# put (0) for default webcam and put (1) and so on for additional connected capturing devices 
cap = cv2.VideoCapture('vid.MOV')

#cap = cv2.VideoCapture(0)

# Some of the major properties of capture
print(f"FRAME_WIDTH :   '{cap.get(cv2.CAP_PROP_FRAME_WIDTH)}'")
print(f"FRAME_HEIGHT :  '{cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}'")
print(f"FPS :           '{cap.get(cv2.CAP_PROP_FPS)}'")
print(f"POS_MSEC :      '{cap.get(cv2.CAP_PROP_POS_MSEC)}'")
print(f"FRAME_COUNT :   '{cap.get(cv2.CAP_PROP_FRAME_COUNT)}'")
print(f"BRIGHTNESS :    '{cap.get(cv2.CAP_PROP_BRIGHTNESS)}'")
print(f"CONTRAST :      '{cap.get(cv2.CAP_PROP_CONTRAST)}'")
print(f"SATURATION :    '{cap.get(cv2.CAP_PROP_SATURATION)}'")
print(f"HUE :           '{cap.get(cv2.CAP_PROP_HUE)}'")
print(f"GAIN :          '{cap.get(cv2.CAP_PROP_GAIN)}'")
print(f"RGB :           '{cap.get(cv2.CAP_PROP_CONVERT_RGB)}'")


# To know the properties
# props = [i for i in dir(cv2) if i.startswith('CAP_PROP_')]
# print(f"\n No of available capture properties are: {len(props)}")

# print(props)

# If there exists a frame, it'll take that by frame-by-frame
while True:
    isTrue, frame = cap.read()
    cv2.imshow('video', frame)
    
    # It'll show the image window for 13ms and quits if the user presses "q"
    if cv2.waitKey(13) & 0xFF == ord('q'):
        break

        
# To close all the frames and windows        
cap.release()
cv2.destroyAllWindows()
