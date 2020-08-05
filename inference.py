import argparse

parser = argparse.ArgumentParser('Classify food images')
parser.add_argument('--dir', type=str, required=True, help='Directory of images')
parser.add_argument('--model', type=str, required=True, help='Path to model')

args = parser.parse_args()

image_DIR = args.dir
model_DIR = args.model

import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

files_in_dir = os.listdir(image_DIR)
image_formats = ['.jpg', '.jpeg', '.png', 'JPEG', '.PNG', '.JPG']

print('Reading images...')

image_paths = []
for file in files_in_dir:
    for image_format in image_formats:
        if image_format in file:
            image_paths.append(image_DIR + '/' + file)
                    
X = []
for image in image_paths:
    img = plt.imread(image)
    X.append(img)
X = np.array(X)
X = X/255

print('Loading model...')

model = load_model(model_DIR)

print('Running model on images...')

y = model.predict(X)

print('Images classified...')

threshold = 0.37

y_copy = np.copy(y)
y_copy[y_copy < threshold] = 0
y_copy[y_copy >= threshold] = 1

classes_ = np.array(['apple', 'banana', 'bread', 'bruscitt', 'cake', 'carrot', 'cutlet',
       'fennel_gratin', 'fillet_fish', 'fries', 'green_beans',
       'lasagna_bolognese', 'meat', 'orange', 'pasta', 'pears', 'peas',
       'pizza', 'pizzoccheri', 'potatoes', 'pudding', 'rice', 'salad',
       'salmon', 'salty_cake', 'savory_pie', 'scallops', 'soup',
       'spinach', 'squid_stew', 'tangerine', 'wet_zucchini', 'yogurt'])

classified_labels = []
for i in range(len(y_copy)):
    classified_labels.append(str(classes_[(y_copy == 1)[i]]))

print('Saving Results...')
    
result = pd.DataFrame(classified_labels).rename(columns={0:'labels'})

image_names = pd.Series(image_paths, name='image').apply(lambda x:x.strip(image_DIR).strip('.jpepngJPEPNG'))

result = pd.concat([image_names, result], axis=1)

result.to_csv(image_DIR + '/result.csv', index=False)

print('Results saved at {}'.format(image_DIR + '/result.csv'))