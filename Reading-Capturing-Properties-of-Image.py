{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "66fa82e7",
   "metadata": {},
   "outputs": [],
   "source": [
        "import cv2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "49cedd31",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Height : 2767\n",
      "Width : 4425\n",
      "No of Channels : 3\n",
      "Dimensions of the Image: (2767, 4425, 3)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#reading an image using file name\n",
    "img = cv.imread('goku3.jpeg')\n",
    "\n",
    "#getting the height, width and channels from the image\n",
    "height, width, channels = img.shape\n",
    "dimensions = img.shape\n",
    "\n",
    "#printing the above details\n",
    "print(\"Height : {}\".format(height))\n",
    "print(\"Width : {}\".format(width))\n",
    "print(\"No of Channels : {}\".format(channels))\n",
    "print(\"Dimensions of the Image: {}\".format(dimensions))\n",
    "\n",
    "#resizing and showing the image from the default commands of opencv\n",
    "img_res = cv.resize(img, (780, 540))\n",
    "img2 = cv.imshow('Goku', img_res)\n",
    "\n",
    "#to show an image for infinity time\n",
    "cv.waitKey(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "684c4a54",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No of available capture properties are: 275\n",
      "['CAP_PROP_APERTURE', 'CAP_PROP_ARAVIS_AUTOTRIGGER', 'CAP_PROP_AUDIO_BASE_INDEX', 'CAP_PROP_AUDIO_DATA_DEPTH', 'CAP_PROP_AUDIO_POS', 'CAP_PROP_AUDIO_SAMPLES_PER_SECOND', 'CAP_PROP_AUDIO_SHIFT_NSEC', 'CAP_PROP_AUDIO_STREAM', 'CAP_PROP_AUDIO_SYNCHRONIZE', 'CAP_PROP_AUDIO_TOTAL_CHANNELS', 'CAP_PROP_AUDIO_TOTAL_STREAMS', 'CAP_PROP_AUTOFOCUS', 'CAP_PROP_AUTO_EXPOSURE', 'CAP_PROP_AUTO_WB', 'CAP_PROP_BACKEND', 'CAP_PROP_BACKLIGHT', 'CAP_PROP_BITRATE', 'CAP_PROP_BRIGHTNESS', 'CAP_PROP_BUFFERSIZE', 'CAP_PROP_CHANNEL', 'CAP_PROP_CODEC_EXTRADATA_INDEX', 'CAP_PROP_CODEC_PIXEL_FORMAT', 'CAP_PROP_CONTRAST', 'CAP_PROP_CONVERT_RGB', 'CAP_PROP_DC1394_MAX', 'CAP_PROP_DC1394_MODE_AUTO', 'CAP_PROP_DC1394_MODE_MANUAL', 'CAP_PROP_DC1394_MODE_ONE_PUSH_AUTO', 'CAP_PROP_DC1394_OFF', 'CAP_PROP_EXPOSURE', 'CAP_PROP_EXPOSUREPROGRAM', 'CAP_PROP_FOCUS', 'CAP_PROP_FORMAT', 'CAP_PROP_FOURCC', 'CAP_PROP_FPS', 'CAP_PROP_FRAME_COUNT', 'CAP_PROP_FRAME_HEIGHT', 'CAP_PROP_FRAME_WIDTH', 'CAP_PROP_GAIN', 'CAP_PROP_GAMMA', 'CAP_PROP_GIGA_FRAME_HEIGH_MAX', 'CAP_PROP_GIGA_FRAME_OFFSET_X', 'CAP_PROP_GIGA_FRAME_OFFSET_Y', 'CAP_PROP_GIGA_FRAME_SENS_HEIGH', 'CAP_PROP_GIGA_FRAME_SENS_WIDTH', 'CAP_PROP_GIGA_FRAME_WIDTH_MAX', 'CAP_PROP_GPHOTO2_COLLECT_MSGS', 'CAP_PROP_GPHOTO2_FLUSH_MSGS', 'CAP_PROP_GPHOTO2_PREVIEW', 'CAP_PROP_GPHOTO2_RELOAD_CONFIG', 'CAP_PROP_GPHOTO2_RELOAD_ON_CHANGE', 'CAP_PROP_GPHOTO2_WIDGET_ENUMERATE', 'CAP_PROP_GSTREAMER_QUEUE_LENGTH', 'CAP_PROP_GUID', 'CAP_PROP_HUE', 'CAP_PROP_HW_ACCELERATION', 'CAP_PROP_HW_ACCELERATION_USE_OPENCL', 'CAP_PROP_HW_DEVICE', 'CAP_PROP_IMAGES_BASE', 'CAP_PROP_IMAGES_LAST', 'CAP_PROP_INTELPERC_DEPTH_CONFIDENCE_THRESHOLD', 'CAP_PROP_INTELPERC_DEPTH_FOCAL_LENGTH_HORZ', 'CAP_PROP_INTELPERC_DEPTH_FOCAL_LENGTH_VERT', 'CAP_PROP_INTELPERC_DEPTH_LOW_CONFIDENCE_VALUE', 'CAP_PROP_INTELPERC_DEPTH_SATURATION_VALUE', 'CAP_PROP_INTELPERC_PROFILE_COUNT', 'CAP_PROP_INTELPERC_PROFILE_IDX', 'CAP_PROP_IOS_DEVICE_EXPOSURE', 'CAP_PROP_IOS_DEVICE_FLASH', 'CAP_PROP_IOS_DEVICE_FOCUS', 'CAP_PROP_IOS_DEVICE_TORCH', 'CAP_PROP_IOS_DEVICE_WHITEBALANCE', 'CAP_PROP_IRIS', 'CAP_PROP_ISO_SPEED', 'CAP_PROP_LRF_HAS_KEY_FRAME', 'CAP_PROP_MODE', 'CAP_PROP_MONOCHROME', 'CAP_PROP_OPENNI2_MIRROR', 'CAP_PROP_OPENNI2_SYNC', 'CAP_PROP_OPENNI_APPROX_FRAME_SYNC', 'CAP_PROP_OPENNI_BASELINE', 'CAP_PROP_OPENNI_CIRCLE_BUFFER', 'CAP_PROP_OPENNI_FOCAL_LENGTH', 'CAP_PROP_OPENNI_FRAME_MAX_DEPTH', 'CAP_PROP_OPENNI_GENERATOR_PRESENT', 'CAP_PROP_OPENNI_MAX_BUFFER_SIZE', 'CAP_PROP_OPENNI_MAX_TIME_DURATION', 'CAP_PROP_OPENNI_OUTPUT_MODE', 'CAP_PROP_OPENNI_REGISTRATION', 'CAP_PROP_OPENNI_REGISTRATION_ON', 'CAP_PROP_OPEN_TIMEOUT_MSEC', 'CAP_PROP_ORIENTATION_AUTO', 'CAP_PROP_ORIENTATION_META', 'CAP_PROP_PAN', 'CAP_PROP_POS_AVI_RATIO', 'CAP_PROP_POS_FRAMES', 'CAP_PROP_POS_MSEC', 'CAP_PROP_PVAPI_BINNINGX', 'CAP_PROP_PVAPI_BINNINGY', 'CAP_PROP_PVAPI_DECIMATIONHORIZONTAL', 'CAP_PROP_PVAPI_DECIMATIONVERTICAL', 'CAP_PROP_PVAPI_FRAMESTARTTRIGGERMODE', 'CAP_PROP_PVAPI_MULTICASTIP', 'CAP_PROP_PVAPI_PIXELFORMAT', 'CAP_PROP_READ_TIMEOUT_MSEC', 'CAP_PROP_RECTIFICATION', 'CAP_PROP_ROLL', 'CAP_PROP_SAR_DEN', 'CAP_PROP_SAR_NUM', 'CAP_PROP_SATURATION', 'CAP_PROP_SETTINGS', 'CAP_PROP_SHARPNESS', 'CAP_PROP_SPEED', 'CAP_PROP_STREAM_OPEN_TIME_USEC', 'CAP_PROP_TEMPERATURE', 'CAP_PROP_TILT', 'CAP_PROP_TRIGGER', 'CAP_PROP_TRIGGER_DELAY', 'CAP_PROP_VIDEO_STREAM', 'CAP_PROP_VIDEO_TOTAL_CHANNELS', 'CAP_PROP_VIEWFINDER', 'CAP_PROP_WB_TEMPERATURE', 'CAP_PROP_WHITE_BALANCE_BLUE_U', 'CAP_PROP_WHITE_BALANCE_RED_V', 'CAP_PROP_XI_ACQ_BUFFER_SIZE', 'CAP_PROP_XI_ACQ_BUFFER_SIZE_UNIT', 'CAP_PROP_XI_ACQ_FRAME_BURST_COUNT', 'CAP_PROP_XI_ACQ_TIMING_MODE', 'CAP_PROP_XI_ACQ_TRANSPORT_BUFFER_COMMIT', 'CAP_PROP_XI_ACQ_TRANSPORT_BUFFER_SIZE', 'CAP_PROP_XI_AEAG', 'CAP_PROP_XI_AEAG_LEVEL', 'CAP_PROP_XI_AEAG_ROI_HEIGHT', 'CAP_PROP_XI_AEAG_ROI_OFFSET_X', 'CAP_PROP_XI_AEAG_ROI_OFFSET_Y', 'CAP_PROP_XI_AEAG_ROI_WIDTH', 'CAP_PROP_XI_AE_MAX_LIMIT', 'CAP_PROP_XI_AG_MAX_LIMIT', 'CAP_PROP_XI_APPLY_CMS', 'CAP_PROP_XI_AUTO_BANDWIDTH_CALCULATION', 'CAP_PROP_XI_AUTO_WB', 'CAP_PROP_XI_AVAILABLE_BANDWIDTH', 'CAP_PROP_XI_BINNING_HORIZONTAL', 'CAP_PROP_XI_BINNING_PATTERN', 'CAP_PROP_XI_BINNING_SELECTOR', 'CAP_PROP_XI_BINNING_VERTICAL', 'CAP_PROP_XI_BPC', 'CAP_PROP_XI_BUFFERS_QUEUE_SIZE', 'CAP_PROP_XI_BUFFER_POLICY', 'CAP_PROP_XI_CC_MATRIX_00', 'CAP_PROP_XI_CC_MATRIX_01', 'CAP_PROP_XI_CC_MATRIX_02', 'CAP_PROP_XI_CC_MATRIX_03', 'CAP_PROP_XI_CC_MATRIX_10', 'CAP_PROP_XI_CC_MATRIX_11', 'CAP_PROP_XI_CC_MATRIX_12', 'CAP_PROP_XI_CC_MATRIX_13', 'CAP_PROP_XI_CC_MATRIX_20', 'CAP_PROP_XI_CC_MATRIX_21', 'CAP_PROP_XI_CC_MATRIX_22', 'CAP_PROP_XI_CC_MATRIX_23', 'CAP_PROP_XI_CC_MATRIX_30', 'CAP_PROP_XI_CC_MATRIX_31', 'CAP_PROP_XI_CC_MATRIX_32', 'CAP_PROP_XI_CC_MATRIX_33', 'CAP_PROP_XI_CHIP_TEMP', 'CAP_PROP_XI_CMS', 'CAP_PROP_XI_COLOR_FILTER_ARRAY', 'CAP_PROP_XI_COLUMN_FPN_CORRECTION', 'CAP_PROP_XI_COOLING', 'CAP_PROP_XI_COUNTER_SELECTOR', 'CAP_PROP_XI_COUNTER_VALUE', 'CAP_PROP_XI_DATA_FORMAT', 'CAP_PROP_XI_DEBOUNCE_EN', 'CAP_PROP_XI_DEBOUNCE_POL', 'CAP_PROP_XI_DEBOUNCE_T0', 'CAP_PROP_XI_DEBOUNCE_T1', 'CAP_PROP_XI_DEBUG_LEVEL', 'CAP_PROP_XI_DECIMATION_HORIZONTAL', 'CAP_PROP_XI_DECIMATION_PATTERN', 'CAP_PROP_XI_DECIMATION_SELECTOR', 'CAP_PROP_XI_DECIMATION_VERTICAL', 'CAP_PROP_XI_DEFAULT_CC_MATRIX', 'CAP_PROP_XI_DEVICE_MODEL_ID', 'CAP_PROP_XI_DEVICE_RESET', 'CAP_PROP_XI_DEVICE_SN', 'CAP_PROP_XI_DOWNSAMPLING', 'CAP_PROP_XI_DOWNSAMPLING_TYPE', 'CAP_PROP_XI_EXPOSURE', 'CAP_PROP_XI_EXPOSURE_BURST_COUNT', 'CAP_PROP_XI_EXP_PRIORITY', 'CAP_PROP_XI_FFS_ACCESS_KEY', 'CAP_PROP_XI_FFS_FILE_ID', 'CAP_PROP_XI_FFS_FILE_SIZE', 'CAP_PROP_XI_FRAMERATE', 'CAP_PROP_XI_FREE_FFS_SIZE', 'CAP_PROP_XI_GAIN', 'CAP_PROP_XI_GAIN_SELECTOR', 'CAP_PROP_XI_GAMMAC', 'CAP_PROP_XI_GAMMAY', 'CAP_PROP_XI_GPI_LEVEL', 'CAP_PROP_XI_GPI_MODE', 'CAP_PROP_XI_GPI_SELECTOR', 'CAP_PROP_XI_GPO_MODE', 'CAP_PROP_XI_GPO_SELECTOR', 'CAP_PROP_XI_HDR', 'CAP_PROP_XI_HDR_KNEEPOINT_COUNT', 'CAP_PROP_XI_HDR_T1', 'CAP_PROP_XI_HDR_T2', 'CAP_PROP_XI_HEIGHT', 'CAP_PROP_XI_HOUS_BACK_SIDE_TEMP', 'CAP_PROP_XI_HOUS_TEMP', 'CAP_PROP_XI_HW_REVISION', 'CAP_PROP_XI_IMAGE_BLACK_LEVEL', 'CAP_PROP_XI_IMAGE_DATA_BIT_DEPTH', 'CAP_PROP_XI_IMAGE_DATA_FORMAT', 'CAP_PROP_XI_IMAGE_DATA_FORMAT_RGB32_ALPHA', 'CAP_PROP_XI_IMAGE_IS_COLOR', 'CAP_PROP_XI_IMAGE_PAYLOAD_SIZE', 'CAP_PROP_XI_IS_COOLED', 'CAP_PROP_XI_IS_DEVICE_EXIST', 'CAP_PROP_XI_KNEEPOINT1', 'CAP_PROP_XI_KNEEPOINT2', 'CAP_PROP_XI_LED_MODE', 'CAP_PROP_XI_LED_SELECTOR', 'CAP_PROP_XI_LENS_APERTURE_VALUE', 'CAP_PROP_XI_LENS_FEATURE', 'CAP_PROP_XI_LENS_FEATURE_SELECTOR', 'CAP_PROP_XI_LENS_FOCAL_LENGTH', 'CAP_PROP_XI_LENS_FOCUS_DISTANCE', 'CAP_PROP_XI_LENS_FOCUS_MOVE', 'CAP_PROP_XI_LENS_FOCUS_MOVEMENT_VALUE', 'CAP_PROP_XI_LENS_MODE', 'CAP_PROP_XI_LIMIT_BANDWIDTH', 'CAP_PROP_XI_LUT_EN', 'CAP_PROP_XI_LUT_INDEX', 'CAP_PROP_XI_LUT_VALUE', 'CAP_PROP_XI_MANUAL_WB', 'CAP_PROP_XI_OFFSET_X', 'CAP_PROP_XI_OFFSET_Y', 'CAP_PROP_XI_OUTPUT_DATA_BIT_DEPTH', 'CAP_PROP_XI_OUTPUT_DATA_PACKING', 'CAP_PROP_XI_OUTPUT_DATA_PACKING_TYPE', 'CAP_PROP_XI_RECENT_FRAME', 'CAP_PROP_XI_REGION_MODE', 'CAP_PROP_XI_REGION_SELECTOR', 'CAP_PROP_XI_ROW_FPN_CORRECTION', 'CAP_PROP_XI_SENSOR_BOARD_TEMP', 'CAP_PROP_XI_SENSOR_CLOCK_FREQ_HZ', 'CAP_PROP_XI_SENSOR_CLOCK_FREQ_INDEX', 'CAP_PROP_XI_SENSOR_DATA_BIT_DEPTH', 'CAP_PROP_XI_SENSOR_FEATURE_SELECTOR', 'CAP_PROP_XI_SENSOR_FEATURE_VALUE', 'CAP_PROP_XI_SENSOR_MODE', 'CAP_PROP_XI_SENSOR_OUTPUT_CHANNEL_COUNT', 'CAP_PROP_XI_SENSOR_TAPS', 'CAP_PROP_XI_SHARPNESS', 'CAP_PROP_XI_SHUTTER_TYPE', 'CAP_PROP_XI_TARGET_TEMP', 'CAP_PROP_XI_TEST_PATTERN', 'CAP_PROP_XI_TEST_PATTERN_GENERATOR_SELECTOR', 'CAP_PROP_XI_TIMEOUT', 'CAP_PROP_XI_TRANSPORT_PIXEL_FORMAT', 'CAP_PROP_XI_TRG_DELAY', 'CAP_PROP_XI_TRG_SELECTOR', 'CAP_PROP_XI_TRG_SOFTWARE', 'CAP_PROP_XI_TRG_SOURCE', 'CAP_PROP_XI_TS_RST_MODE', 'CAP_PROP_XI_TS_RST_SOURCE', 'CAP_PROP_XI_USED_FFS_SIZE', 'CAP_PROP_XI_WB_KB', 'CAP_PROP_XI_WB_KG', 'CAP_PROP_XI_WB_KR', 'CAP_PROP_XI_WIDTH', 'CAP_PROP_ZOOM']\n",
      "FRAME_WIDTH :   '0.0'\n",
      "FRAME_HEIGHT :  '0.0'\n",
      "FPS :           '0.0'\n",
      "POS_MSEC :      '0.0'\n",
      "FRAME_COUNT :   '0.0'\n",
      "BRIGHTNESS :    '0.0'\n",
      "CONTRAST :      '0.0'\n",
      "SATURATION :    '0.0'\n",
      "HUE :           '0.0'\n",
      "GAIN :          '0.0'\n",
      "RGB :           '0.0'\n"
     ]
    },
    {
     "ename": "error",
     "evalue": "OpenCV(4.6.0) D:\\a\\opencv-python\\opencv-python\\opencv\\modules\\highgui\\src\\window.cpp:967: error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'cv::imshow'\n",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31merror\u001b[0m                                     Traceback (most recent call last)",
      "Input \u001b[1;32mIn [3]\u001b[0m, in \u001b[0;36m<cell line: 24>\u001b[1;34m()\u001b[0m\n\u001b[0;32m     23\u001b[0m \u001b[38;5;28;01mwhile\u001b[39;00m \u001b[38;5;28;01mTrue\u001b[39;00m:\n\u001b[0;32m     24\u001b[0m     isTrue, frame \u001b[38;5;241m=\u001b[39m vid_cap\u001b[38;5;241m.\u001b[39mread()\n\u001b[1;32m---> 25\u001b[0m     \u001b[43mcv\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mimshow\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mvideo\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mframe\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m     27\u001b[0m     \u001b[38;5;66;03m#to show the image for 13ms and quits the output when we press \"q\"\u001b[39;00m\n\u001b[0;32m     28\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m cv\u001b[38;5;241m.\u001b[39mwaitKey(\u001b[38;5;241m13\u001b[39m) \u001b[38;5;241m&\u001b[39m \u001b[38;5;241m0xFF\u001b[39m \u001b[38;5;241m==\u001b[39m \u001b[38;5;28mord\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mq\u001b[39m\u001b[38;5;124m'\u001b[39m):\n",
      "\u001b[1;31merror\u001b[0m: OpenCV(4.6.0) D:\\a\\opencv-python\\opencv-python\\opencv\\modules\\highgui\\src\\window.cpp:967: error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'cv::imshow'\n"
     ]
    }
   ],
   "source": [
    "#reading a video file using the file name\n",
    "vid_cap = cv.VideoCapture('test-vid.MOV')\n",
    "\n",
    "#getting to know the properties of capture\n",
    "prop_flags = [i for i in dir(cv) if i.startswith('CAP_PROP_')]\n",
    "print(\"No of available capture properties are: {}\".format(len(prop_flags)))\n",
    "print(prop_flags)\n",
    "\n",
    "#printing the some major properties\n",
    "print(\"FRAME_WIDTH :   '{}'\".format(vid_cap.get(cv.CAP_PROP_FRAME_WIDTH)))\n",
    "print(\"FRAME_HEIGHT :  '{}'\".format(vid_cap.get(cv.CAP_PROP_FRAME_HEIGHT)))\n",
    "print(\"FPS :           '{}'\".format(vid_cap.get(cv.CAP_PROP_FPS)))\n",
    "print(\"POS_MSEC :      '{}'\".format(vid_cap.get(cv.CAP_PROP_POS_MSEC)))\n",
    "print(\"FRAME_COUNT :   '{}'\".format(vid_cap.get(cv.CAP_PROP_FRAME_COUNT)))\n",
    "print(\"BRIGHTNESS :    '{}'\".format(vid_cap.get(cv.CAP_PROP_BRIGHTNESS)))\n",
    "print(\"CONTRAST :      '{}'\".format(vid_cap.get(cv.CAP_PROP_CONTRAST)))\n",
    "print(\"SATURATION :    '{}'\".format(vid_cap.get(cv.CAP_PROP_SATURATION)))\n",
    "print(\"HUE :           '{}'\".format(vid_cap.get(cv.CAP_PROP_HUE)))\n",
    "print(\"GAIN :          '{}'\".format(vid_cap.get(cv.CAP_PROP_GAIN)))\n",
    "print(\"RGB :           '{}'\".format(vid_cap.get(cv.CAP_PROP_CONVERT_RGB)))\n",
    "\n",
    "#reading the video, frame by frame, if its exists\n",
    "while True:\n",
    "    isTrue, frame = vid_cap.read()\n",
    "    cv.imshow('video', frame)\n",
    "    \n",
    "    #to show the image for 13ms and quits the output when we press \"q\"\n",
    "    if cv.waitKey(13) & 0xFF == ord('q'):\n",
    "        break\n",
    "\n",
    "        \n",
    "#releasing all the frames and windows        \n",
    "vid_cap.release()\n",
    "cv.destroyAllWindows()\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "dec8556c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "FRAME_WIDTH :   '640.0'\n",
      "FRAME_HEIGHT :  '480.0'\n",
      "FPS :           '30.0'\n",
      "POS_MSEC :      '0.0'\n",
      "FRAME_COUNT :   '-1.0'\n",
      "BRIGHTNESS :    '128.0'\n",
      "CONTRAST :      '32.0'\n",
      "SATURATION :    '64.0'\n",
      "HUE :           '0.0'\n",
      "GAIN :          '-1.0'\n",
      "RGB :           '1.0'\n"
     ]
    }
   ],
   "source": [
    "#reading a video from available devices, 0 - default webcam, 1 - additional dvice ...\n",
    "vid_cap = cv.VideoCapture(0)\n",
    "#printing the some major properties\n",
    "print(\"FRAME_WIDTH :   '{}'\".format(vid_cap.get(cv.CAP_PROP_FRAME_WIDTH)))\n",
    "print(\"FRAME_HEIGHT :  '{}'\".format(vid_cap.get(cv.CAP_PROP_FRAME_HEIGHT)))\n",
    "print(\"FPS :           '{}'\".format(vid_cap.get(cv.CAP_PROP_FPS)))\n",
    "print(\"POS_MSEC :      '{}'\".format(vid_cap.get(cv.CAP_PROP_POS_MSEC)))\n",
    "print(\"FRAME_COUNT :   '{}'\".format(vid_cap.get(cv.CAP_PROP_FRAME_COUNT)))\n",
    "print(\"BRIGHTNESS :    '{}'\".format(vid_cap.get(cv.CAP_PROP_BRIGHTNESS)))\n",
    "print(\"CONTRAST :      '{}'\".format(vid_cap.get(cv.CAP_PROP_CONTRAST)))\n",
    "print(\"SATURATION :    '{}'\".format(vid_cap.get(cv.CAP_PROP_SATURATION)))\n",
    "print(\"HUE :           '{}'\".format(vid_cap.get(cv.CAP_PROP_HUE)))\n",
    "print(\"GAIN :          '{}'\".format(vid_cap.get(cv.CAP_PROP_GAIN)))\n",
    "print(\"RGB :           '{}'\".format(vid_cap.get(cv.CAP_PROP_CONVERT_RGB)))\n",
    "#reading the video, frame by frame, if its exists\n",
    "while True:\n",
    "    isTrue, frame = vid_cap.read()\n",
    "    cv.imshow('video', frame)\n",
    "    #to show the image for 13ms and quits the output when we press \"q\"\n",
    "    if cv.waitKey(13) & 0xFF == ord('q'):\n",
    "        break\n",
    "#releasing all the frames and windows        \n",
    "vid_cap.release()\n",
    "cv.destroyAllWindows()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
