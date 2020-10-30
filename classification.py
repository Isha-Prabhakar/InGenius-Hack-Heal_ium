import cv2
import os
from skimage.feature import local_binary_pattern
from scipy.stats import itemfreq
from sklearn.preprocessing import normalize
import cvutils
import pickle
import numpy as np
from PIL import Image



class CanClass(object):

    def __init__(self):
        self.x_name = None
        self.x_train = None
        self.y_train = None


    def model_loading(self):
        with open('pkl_files/X_name_final.pkl','rb') as f:
            self.x_name = pickle.load(f)

        with open('pkl_files/X_train_final.pkl','rb') as f:
            self.x_train = pickle.load(f)

        with open('pkl_files/Y_train_final.pkl','rb') as f:
            self.y_train = pickle.load(f)

    def preprocess_image(self, test_image):
        im = cv2.imread(test_image)
        im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        return im_gray

    def crop_image(self, test_image):
        image1 = Image.open(test_image)
        width, height = image1.size

        if width > 224 or height > 224:
            left = 0
            top = 0
            right = 224
            bottom = 224
            im1 = image1.crop((left, top, right, bottom)) 
            im1.show()
            im1.save(test_image)

        return test_image
        
    def fit_image(self, test_image):
        self.model_loading()

        cropped_image = self.crop_image(test_image)
        im_gray = self.preprocess_image(cropped_image)

        radius = 3
        no_points = 8 * radius

        lbp = local_binary_pattern(im_gray, no_points, radius, method = 'uniform')

        return lbp
    

    def classify_image(self, test_image):
        lbp = self.fit_image(test_image)

        x = itemfreq(lbp.ravel())
        hist = x[:, 1]/sum(x[:, 1])
        results = list()

        for index,x in enumerate(self.x_train):
            score = cv2.compareHist(np.array(x, dtype = np.float32), np.array(hist, dtype = np.float32), cv2.HISTCMP_CORREL)
            results.append((self.x_name[index], round(score, 3), self.y_train[index]))

        results = sorted(results, key = lambda score: score[1], reverse = True)
        return results[0][2],results[0][1]

    def predict_class(self, test_image):
        result, score = self.classify_image(test_image)
        canc_map = {0 : 'Non-Melanomic Cancer', 
                    1 : 'Melanomic Cancer', 
                    2 : 'Non-Cancerous'}

        return (canc_map[result], score)