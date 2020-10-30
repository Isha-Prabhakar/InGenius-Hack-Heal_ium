import glob
import pandas as pd
from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator
from PIL import Image
from sklearn.model_selection import train_test_split
import random
import numpy as np
import cv2
import pickle


class DataFeat(object):

    def __init__(self):
        pass

    def width_height(self, im):
        data = cv2.imread(im)
        data = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)
        data = np.reshape(data, (1, data.shape[0], data.shape[1], data.shape[2]))
        datagen = ImageDataGenerator(width_shift_range = 0.2, height_shift_range = 0.2)
        aug_iter = datagen.flow(data, batch_size = 1)
        image = next(aug_iter)[0].astype('uint8')
        return image

    def rotation(self, im):
        data = cv2.imread(im)
        data = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)
        data = np.reshape(data, (1, data.shape[0], data.shape[1], data.shape[2]))
        datagen = ImageDataGenerator(rotation_range = 30, fill_mode = 'nearest')
        aug_iter = datagen.flow(data, batch_size = 1)
        image = next(aug_iter)[0].astype('uint8')
        return image

    def horiz_vert(self, im):
        data = cv2.imread(im)
        data = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)
        data = np.reshape(data, (1, data.shape[0], data.shape[1], data.shape[2]))
        datagen = ImageDataGenerator(horizontal_flip = True, vertical_flip = True)
        aug_iter = datagen.flow(data, batch_size = 1)
        image = next(aug_iter)[0].astype('uint8')
        return image

    def bright(self, im):
        data = cv2.imread(im)
        data = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)
        data = np.reshape(data, (1, data.shape[0], data.shape[1], data.shape[2]))
        datagen = ImageDataGenerator(brightness_range = [0.4,1.5])
        aug_iter = datagen.flow(data, batch_size = 1)
        image = next(aug_iter)[0].astype('uint8')
        return image

    def zoom(self, im):
        data = cv2.imread(im)
        data = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)
        data = np.reshape(data, (1, data.shape[0], data.shape[1], data.shape[2]))
        datagen = ImageDataGenerator(zoom_range = 0.4)
        aug_iter = datagen.flow(data, batch_size = 1)
        image = next(aug_iter)[0].astype('uint8')
        return image

    def feat_ext_mal_ben_part(self, path, num):
        c = 0
        training_data_path = list()

        for i in glob.glob(path):
            if c > num: break
            training_data_path.append(i)
            c += 1

        return training_data_path

    def feat_ext_mal_ben(self, path):
        training_data_path = [i for i in glob.glob(path)]

        return training_data_path

    def extract(self, train_data):
        l_train_y = [0]*328
        l_train_y.extend([1]*328)
        l_train_y.extend([2]*330)

        train_x, test_x, train_y, test_y = train_test_split(np.array(train_data), np.array(l_train_y), test_size = 0.2, random_state = 42)

        X_train = list()
        X_name = list()
        y_train = list()

        for train_image in range(len(train_x)):
            im = cv2.imread(train_x[train_image])
            im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

            radius = 3 
            no_points = 8 * radius
            lbp = local_binary_pattern(im_gray, no_points, radius, method='uniform')
            x = itemfreq(lbp.ravel())
            hist = x[:, 1]/sum(x[:, 1])

            X_name.append(train_x[train_image])
            X_train.append(hist)
            y_train.append(train_y[train_image])

        return (X_name, X_train, y_train)

        


data_feat = DataFeat()
train_data = list()

canc_ben = data_feat.feat_ext_mal_ben_part('data/train/benign/*.*', 328)
train_data.append(canc_ben)

canc_mal = data_feat.feat_ext_mal_ben_part('data/train/malignant/*.*', 328)
train_data.append(canc_mal)

skin_data = data_feat.feat_ext_mal_ben_part('data/skin1/*.*', 226)
train_data.append(skin_data)

no_allergy = data_feat.feat_ext_mal_ben('data/no_allergy/*.*')
train_data.append(no_allergy)

feat_ext = data_feat.extract(train_data)

X_name = feat_ext[0]
X_train = feat_ext[1]
y_train = feat_ext[2]

with open('/content/X_name_final.pkl','wb') as f:
    pickle.dump(X_name,f)
with open('/content/X_train_final.pkl','wb') as f:
    pickle.dump(X_train,f)
with open('/content/Y_train_final.pkl','wb') as f:
    pickle.dump(y_train,f)
