# U-net-2D-EM-segmentation
using keras
aim to ISBI Challenge: Segmentation of neuronal structures in EM stacks,http://brainiac2.mit.edu/isbi_challenge/
you can download the data from the website or find data in the data folder
Pre-processing
The images are 3-D volume tiff, you should transfer the stacks into images first.of course the images in the data folder have already be transformed into 2D images. The data for training contains 30 512*512 images, which are far not enough to feed a deep learning neural network.
however without data augmentation we can still get a good result.
You should first run the data.py,then the unet.py
remember to change the file location in both files.
