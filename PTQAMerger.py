#JCUH Phototherapy QA Results Compiler
#v1 for use with the ILT2400
#Andrew Simpson

import glob
import os
import pandas as pd
import tkinter
from tkinter.filedialog import askdirectory
import ctypes

ctypes.windll.user32.MessageBoxW(0, "Please note, this script should only be used for for the ILT2400", "Phototherapy QA Results Compiler v1",0)
# Open QA Results Folder
QAFilesPath = askdirectory(title='Phototherapy QA Results: Select QA Folder') # shows dialog box and return the path
# get all the csv results
csvfiles = glob.glob(os.path.join(QAFilesPath, '*.csv'))
# loop through the files and read them in with pandas
dataframes = []  # a list to hold all the individual pandas DataFrames
for csvfile in csvfiles:
    df = pd.read_csv(csvfile)
    dataframes.append(df)
# concatenate them all together
result = pd.concat(dataframes, ignore_index=True)
# print out to a new csv file
result.to_csv(QAFilesPath + '\\CombinedResults.csv')

ctypes.windll.user32.MessageBoxW(0, "QA results have been combined and can be found within the folder", "Phototherapy QA Results Compiler v1",0)