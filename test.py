
import pandas as pd
import pickle

location ='1st Block Jayanagar'
bhk =2
bath = '2'
sqft = '2000'

pipe=pickle.load(open("RidgeModel.pkl","rb"))

input = pd.DataFrame([[location,sqft,bath,bhk]],
columns=['location', 'total_sqft','bath', 'bhk'])

#prediction = pipe.predict(input)[0]
#print(prediction)

import sklearn
print(sklearn.__version__)