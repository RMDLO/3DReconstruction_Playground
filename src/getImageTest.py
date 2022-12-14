import pyrealsense2 as rs
import numpy as np
import cv2
import time
import os

yourPath = "/home/fsamhouri/Documents/" #change this path to the directory your 3Drp file is in
sfmPath = "3DReconstruction_Playground/OpenSfM/data/"
imagePath = "images/"


while True:
    print("Please type in the name of your image folder")
    folderName = input()

    newPath = yourPath + sfmPath + folderName + "/" + imagePath 
    checkPath = yourPath + sfmPath + folderName
    if os.path.exists(checkPath):
        print("This folder already exists. Do you wish use it? [Y/N]")
        ans = input()
        if ans == "Y":
            break
        elif ans == "N":
            continue
        else:
            print("Invalid Response")
            continue
    else:
        os.makedirs(newPath)
        break

pipeline = rs.pipeline()
config = rs.config()

pipeline_wrapper = rs.pipeline_wrapper(pipeline)
pipeline_profile = config.resolve(pipeline_wrapper)
device = pipeline_profile.get_device()
device_product_line = str(device.get_info(rs.camera_info.product_line))

found_rgb = False
for s in device.sensors:
    if s.get_info(rs.camera_info.name) == 'RGB Camera':
        found_rgb = True
        break
if not found_rgb:
    print("The demo requires Depth camera with Color sensor")
    exit(0)

config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

pipeline.start(config)

img_counter = 0
try:
    while True:

        # Wait for a coherent pair of frames: depth and color
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        if not color_frame:
            continue

        # Convert images to numpy arrays
        color_image = np.asanyarray(color_frame.get_data())


        color_colormap_dim = color_image.shape

        # # If depth and color resolutions are different, resize color image to match depth image for display
        # if depth_colormap_dim != color_colormap_dim:
        #     resized_color_image = cv2.resize(color_image, dsize=(depth_colormap_dim[1], depth_colormap_dim[0]), interpolation=cv2.INTER_AREA)
        #     images = np.hstack((resized_color_image, depth_colormap))
        # else:
        #     images = np.hstack((color_image, depth_colormap))

        # Show images
        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RealSense', color_image)
        # ret,frame = color_image.read()
        k = cv2.waitKey(1)

        if k%256 == 27:
            print("Escape hit, closing the app")
            break
        elif k%256 == 32:
            frameNum = 10
            interval = 2
            img_name = newPath + "pic{}.png".format(img_counter)
            cv2.imwrite(img_name, color_image)
            img_counter += 1

finally:

    # Stop streaming
    pipeline.stop()