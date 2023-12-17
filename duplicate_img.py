import hashlib,os
import time
from hashlib import md5


os.chdir('D:\pythonn\images')
os.getcwd()
img_list=os.listdir()
print(len(img_list))

duplicate_img=[]
hash_keys=dict()


#comparing hash of images and separate them

for index,filename in enumerate(os.listdir(('.'))):

	if os.path.isfile(filename):
		with open(filename ,'rb') as f:
			filehash=hashlib.md5(f.read()).hexdigest()
			if filehash not in hash_keys:
				hash_keys[filehash]=index
			else:
				duplicate_img.append((index,hash_keys[filehash]))
# print (duplicate_img)

#remove duplicate images
for index in duplicate_img:
	print ((img_list[index[0]]))	
	os.remove(img_list[index[0]])

os.getcwd()
img_list=os.listdir()
print(len(img_list))
	