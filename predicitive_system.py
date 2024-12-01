import numpy as np
import pandas as pd
import pickle

load_mod = pickle.load(open('model.sav', 'rb'))

def load_model(input):
    
    input_arr = np.asarray(input)
    input_resize = input_arr.reshape(1,-1)
    classifier_input = load_mod.predict(input_resize)
    if classifier_input[0] == 1:
        print("This perosn have Diabetic...")
    else:
        print("This person have'nt Diabetic...")




