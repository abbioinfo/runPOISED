#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 11:38:49 2021

@author: abhinav kaushik
"""
import os 
import pandas as pa
import numpy as np
from sklearn.metrics import f1_score
import seaborn as sns


dname = "POISED_26_2_2021_12_37/"
sampleF1 = pa.DataFrame([])
CTF1 = pa.DataFrame([])

# Sample F1 #
for file in os.listdir(dname): 
    if file.endswith("_labelled_expr.csv"):
        print ("reading.."+str(file))
        ID = file.replace('_labelled_expr.csv','')
        fpath = str(dname) + "/" + file
        expmatrix = pa.read_csv(fpath, delimiter=",")
        predictedY = expmatrix.loc[:,'labels'].values
        fpath = str('POISED/POISED_labels/') + str(ID) + ".labels.csv"
        labels = pa.read_csv(fpath, delimiter=",")
        ExpectedY = labels.loc[:,'CellType'].values
        F1sc = f1_score(ExpectedY,predictedY,average="weighted")
        d = {'ID': [ID], 'F1': [F1sc], 'Dataset': 'POISED'}
        sampleF1 = pa.concat([sampleF1, pa.DataFrame(d)], axis=0)
        CTs = np.unique(ExpectedY) ## all expected cell types. lets analyze their F1 one by one 
        for ct in CTs:
            if ct != 'Unknown':
                print ("reading.."+str(ct))
                ExpCTY = ExpectedY[ExpectedY==ct]
                PredCTY = predictedY[ExpectedY==ct]
                F1perCT = f1_score(ExpCTY,PredCTY,average="weighted")
                d = {'ID': [ID],'CellType':ct, 'F1': [F1perCT], 'Dataset': 'POISED'}
                CTF1 = pa.concat([CTF1, pa.DataFrame(d)], axis=0)

ct = 'CD4_PeaReactive'

# Sample F1 ## Usual boxplot
ax = sns.boxplot(x='Dataset', y='F1', data=sampleF1)
ax = sns.swarmplot(x='Dataset', y='F1', data=sampleF1, color="grey").set_title("CyAnno: Per sample F1 score")
fig = ax.get_figure()
fig.savefig(str(dname) + "/" + "F1scorePerPOISEDSample.png")

# Cell Type F1 ## Usual boxplot
ax = sns.boxplot(x='CellType', y='F1', data=CTF1)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
ax = sns.swarmplot(x='CellType', y='F1', data=CTF1, color="grey").set_title("CyAnno: Per Cell type F1 score")
fig = ax.get_figure()
fig.savefig(str(dname) + "/" + "F1scorePerCellTypePOISED.png")
