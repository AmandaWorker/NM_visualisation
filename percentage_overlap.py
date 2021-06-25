#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 13:30:05 2021

@author: amanda
"""

import numpy as np
import pandas as pd
import seaborn as sns
import csv
import json

## Get Z-score data ready for visualisation

############################## Read in data ##################################
 
path = "/Users/amanda/Desktop/OneDrive - King's College London/BRAINCHART_KCL/Analysis/HBR_MODELS_WITH_QC/HBR/Models/GAP_25_basic_HBR_linear_0/"

Z_scores = pd.read_pickle(path + f"Z_transfer_GAP_TEST.pkl")

labels = pd.read_pickle(path + f"labels__transfer_GAP_TRAIN.pkl" )
labels = pd.DataFrame(labels)
labels.columns = ['diagnosis']


############################## Format data ##################################
 
# Rename the z-scores df to regional names - aparc.a2009s
thick_avg = pd.read_csv(path + f"inputs/ThickAvg_transfer.csv")
regions = pd.DataFrame(list(thick_avg.iloc[:,1:].columns))
Z_scores.columns = thick_avg.iloc[:,1:].columns
print(Z_scores)

# Split data into left and right df's
right_z_score = Z_scores.iloc[:, 74:]
left_z_score = Z_scores.iloc[:,:74]

# Map z-scores back to labels
right_data = pd.concat([right_z_score, labels], axis=1)
left_data = pd.concat([left_z_score, labels], axis=1)

# Split into left/right patient/control
right_patient = right_data[right_data['diagnosis'] == 1]
right_control = right_data[right_data['diagnosis'] == 0]
left_control = left_data[left_data['diagnosis'] == 0]
left_patient = left_data[left_data['diagnosis'] == 1]


############################## Count significant deviations ##################################

# Calculate the count
right_count_above_thresh_patient = pd.DataFrame(right_patient[right_patient > 1.96].count())
right_count_above_thresh_patient.columns = ["Count"]

# Calc percent of sample
right_patient_n = len(right_patient)
right_count_above_thresh_patient["pcnt"] = (right_count_above_thresh_patient.Count/right_patient_n)*100
print(right_count_above_thresh_patient)


# Just take the percentage
right_percent_positive_patients = pd.DataFrame(right_count_above_thresh_patient["pcnt"]).reset_index()
right_percent_positive_patients.columns = ["Region", "Percentage positive"]

# Rename to match annotation file
right_percent_positive_patients.Region = right_percent_positive_patients.Region.str.replace("R_", "")
right_percent_positive_patients.Region = right_percent_positive_patients.Region.str.replace("&", "_and_")
right_percent_positive_patients.Region = '"' + right_percent_positive_patients.Region + '"'

right_percent_positive_patients.insert(1, "equals", value="=")
right_percent_positive_patients.insert(3, "comma", value=",")

right_percent_positive_patients = right_percent_positive_patients.astype(str)

right_percent_positive_patients["Rp"] = right_percent_positive_patients["Region"] + right_percent_positive_patients["equals"] 
right_percent_positive_patients["Rp"] = right_percent_positive_patients["Rp"] + right_percent_positive_patients["Percentage positive"] + right_percent_positive_patients["comma"]

print(right_percent_positive_patients)









