import numpy as np
from keras.models import load_model
from scipy.misc import imread, imresize,imshow
from keras import backend as K

def identify_image(image_file):
	model = load_model('#path_to_hemorrhage_identifier_final.h5_file')

	image = imread(image_file,mode='L')	#read in grayscale mode
	image = imresize(image,(128,128))	#resize to 128*128 px
	image = image.reshape(1,128,128,1)	#reshape to (128,128,1)
	
	prediction = model.predict(image / 255.)	#rescale image data to pixels between 0 & 1 and feed to model

	digit = np.argmax(prediction)	#get the index
	digit = prediction[digit][0]	#get the value at the index
	digit=round(digit)	#round off to nearest integer

	K.clear_session()	#close the tensorflow session

	return int(digit)