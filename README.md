#### Abstract
The goal of this application is to test the use of 3D Reconstruction on Robotic Perception to manipulate deformable objects. 

#### Installation Instructions

First install ![OpenSfM dependancies and build the library](https://opensfm.org/docs/building.html).

Next, perform the below comands in a bash terminal. 

```bash
# Clone the RMDLO 3D Reconstruction Playground
$ git clone git@github.com:RMDLO/3DReconstruction_Playground.git --recurse-submodules
# Install 3D Reconstruction Playground requirements
$ cd 3DReconstruction_Playground && pip install -r requirements.txt
```

#### Run Instructions



#### Example Output

3D Reconstruction Playground allows users to reconstruct scenes with small objects where depth imagery may not have fine enough resolution or may be impossible to collect. Below is an example image of a small component we used 3D Reconstruction Playground to image.

<p align="center">
  <img src="images/scale.jpg" width="500" title="hover text">
</p>

Below is the pointcloud generated from 3D Reconstruction Playground. This pointcloud was generated using ![26 images](https://github.com/RMDLO/3DReconstruction_Playground/tree/master/images/adafruit)

<p align="center">
  <img src="images/adafruit.png" width="500" title="hover text">
</p>

#### Acknowledgements

Realsense image stream based on [Intel Realsense Documentation](https://dev.intelrealsense.com/docs/python2) and The [Librealsense Git Repository](https://github.com/IntelRealSense/librealsense).

Realsense image capture based on [Coding Shiksha Tutorials](https://codingshiksha.com/)
