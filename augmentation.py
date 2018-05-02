import os
import glob
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img,array_to_img
    
def augmentation(path_aug='./results/aug'):
    
	#read images
    train_path="./data/train"
    label_path="./data/label"
    img_type="tif"
    train_imgs = glob.glob(train_path+"/*."+img_type)
    label_imgs = glob.glob(label_path+"/*."+img_type)
    slices = len(train_imgs)
    if len(train_imgs) != len(label_imgs) or len(train_imgs) == 0:
        print ("trains can't match labels")
        return 0
    
   # This will do preprocessing and realtime data augmentation:
    datagen = ImageDataGenerator(rotation_range=20,width_shift_range=0.2,height_shift_range=0.2,zoom_range=0.05,horizontal_flip=True)
	# merge label and train
    print('Using real-time data augmentation.')
    #one by one augmentation
    for i in range(slices):
        img_t = load_img(train_path+"/"+str(i)+".tif",grayscale=True)
        img_l = load_img(label_path+"/"+str(i)+".tif",grayscale=True)
        x_t = img_to_array(img_t)
        x_l = img_to_array(img_l)
        img = np.zeros([np.shape(x_t)[:2],3])
        img[:,:,0]=x_t
        img[:,:,2]=x_l
        	# here's a more "manual" example
        batches = 0
        for batch in datagen.flow(img, batch_size=1,save_to_dir=path_aug,save_prefix=str(i),save_format='tif'):
            batches += 1
            if batches >= 30:
                break
            # we need to break the loop by hand because
            # the generator loops indefinitely
    aug_imgs = glob.glob(path_aug+"/*.tif")
    savedir = path_aug + "/train"
    if not os.path.lexists(savedir):
        os.mkdir(savedir)
    savedir = path_aug + "/label"
    if not os.path.lexists(savedir):
        os.mkdir(savedir)
    i=0
    for imgname in aug_imgs:
        img =load_img(imgname)
        img_train = img[:,:,0]
        img_label = img[:,:,2]
        img_train = array_to_img(img_train)
        img_label = array_to_img(img_label)
        img_train.save(path_aug+"/train/"+str(i)+".tif")
        img_label.save(path_aug+"/label/"+str(i)+".tif")
        i+=1
	
if __name__ == "__main__":
    augmentation()
