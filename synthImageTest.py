import numpy as np
import cv2
import time
import photo4d as p4d 

proj = p4d.Photo4d(project_path="/home/fsamhouri/Documents/Project")
proj.sort_picture()
proj.check_picture_quality()
proj.timeSIFT_orentatin()
proj.prepare_gcp_files(path_to_GCP_file,file_format="N_X_Y_Z")
proj.set_selected_set("image.JPG")
proj.pick_initial_gcps()

proj.compute_transform()

proj.pick_all_gcps()

proj.process_all_timesteps()

proj.clean_up_tmp()