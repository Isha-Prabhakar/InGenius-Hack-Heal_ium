import webbrowser
import random as rd
import time

class RemedySugg(object):
    
    def __init__(self):
        self.non_cancerous = ['https://www.webmd.com/allergies/treating-your-skin-allergies-at-home',
                              'https://www.healthline.com/health/skin-allergy-home-remedy',
                              'https://www.ncbi.nlm.nih.gov/books/NBK92761/']

        self.cancerous_malig = ['https://www.cancer.net/cancer-types/melanoma',
                                'https://www.mayoclinic.org/diseases-conditions/melanoma/diagnosis-treatment/drc-20374888',
                                'https://www.cancer.org/cancer/melanoma-skin-cancer/causes-risks-prevention.html']

        self.cancerous_ben = ['https://www.cancer.net/cancer-types/skin-cancer-non-melanoma',
                              'https://www.mayoclinic.org/diseases-conditions/nonmelanoma-skin-cancer/symptoms-causes/syc-20355397',
                              'https://www.cancer.org/cancer/basal-and-squamous-cell-skin-cancer.html']

    
    def suggest_remedy(self, type):
        type_web_match = {'Non-Melanomic Cancer' : rd.choice(self.cancerous_malig),
                          'Melanomic Cancer' : rd.choice(self.cancerous_malig),
                          'Non-Cancerous' : rd.choice(self.non_cancerous)
                          }

        print("Cancer Details and Remedies -")
        print("")
        print("Searching and Opening Website...")

        time.sleep(7)

        print("Website Opened!")

        webbrowser.open(type_web_match[type[0]])