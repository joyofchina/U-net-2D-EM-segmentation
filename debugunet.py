from keras.models import *
from data import *
from keras.preprocessing.image import array_to_img
import numpy as np
img_rows = 512
img_cols = 512
save_path="./results/"
mydata = dataProcess(img_rows,img_cols)
imgs_test = mydata.load_test_data()
print('predict test data')
model = load_model('unet.hdf5')
imgs_mask_test = model.predict(imgs_test, batch_size=1, verbose=1)
np.save(save_path+ "imgs_mask_test.npy", imgs_mask_test)
print("array to image")
imgs = np.load(save_path+"imgs_mask_test.npy")
for i in range(imgs.shape[0]):
	img = imgs[i]
	if i==0:
		print(img.shape)
	img = array_to_img(img)
	
	img.save("./results/seg/"+ str(i)+".jpg")
