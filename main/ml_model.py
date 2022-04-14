import sys
import os
import joblib
import numpy as np
import pandas as pd

# The first step is to get our machine learning dataset:
# 

def logic_layer(x):
	print(x)

	numeric_cols = ['age', 'height', 'weight', 'ap_hi', 'ap_lo']
	categorical_cols = ['gender', 'cholesterol', 'gluc', 'smoke', 'alco', 'active']
	
	tp = pd.DataFrame(columns=['age', 'gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active'])
	tp.loc[0]= x
	scaler = joblib.load('main\scaler.joblib')
	encoder = joblib.load('main\encoder.joblib')
	tp[numeric_cols] = scaler.transform(tp[numeric_cols])
	tp[categorical_cols] = encoder.transform(tp[categorical_cols])

	model = joblib.load('main/rf_clf.joblib')
	y_pred = model.predict(tp)
	
	if y_pred == 0:
		pred = "no cardio stroke"
	else:
		pred = "cardio stroke"
	return pred
