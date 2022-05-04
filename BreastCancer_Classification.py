#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 10:46:17 2022

@author: jeffersonpasserini
"""
#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import dataset
DATASET_PATH = "/home/jeffersonpasserini/dados/ProjetosTutoriais/Material-Disc-IA/Ativ_kfold_classif_cancer_mama/"
dataset = pd.read_csv(DATASET_PATH+"wdbc.data", 
                      names=['sample_number','clump_tickness','cell_size','cell_shape','marginal_adhesion','single_epithelial_cell_size','components','pcc_knn','acc','f1','roc','extr_time','red_time','train_time','pred_time','column'], skiprows=1)

#define X samples and y results
X = dataset.iloc[:, 1:31].values
y = dataset.iloc[:, 31].values

dataset.describe()

dataset.head()


