import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy import stats
from math import sqrt
import seaborn as sns
import re

def extract_tag(df):
    new_list = []
    tag_list = []
    tag_number = []
    for i in df['Tags'].dropna().tolist(): #remove )
        pattern = re.split('\)', i.lower())
        new_list += pattern
    for i in [x.strip() for x in new_list if x != '']: #remove (, save to a list
        pattern =re.split('\(', i)
        tag_list.append(pattern[0].strip().capitalize())
        tag_number.append(str(pattern[1]))

    info = {'tag':tag_list,'tag_number':tag_number}
    df = pd.DataFrame(info)
    df['tag'].value_counts().to_frame(name='tag_number')
    return df['tag'].value_counts().to_frame(name='tag_number')

# your file path
src = r"C:\Users\23645\OneDrive\博士阶段-文档\何吉波-RateMyProfessor\Dataset from RateMyProfessor.com for professors' teaching evaluation.csv"
df = pd.read_csv(src)
print(df.head())

#Star rating
print("student_star describe:\n")
print(df["Student_star"].describe())

#Tag
df_tag = extract_tag(df)
print(df_tag)

#course modality
print(df["Online"].value_counts())

#Attendance requirement
print(df["Attendance"].value_counts())

#Course difficulty
print("Difficulty_index describe:\n")
print(df["Difficulty_index"].describe())

#Grade
print(df["Grade"].value_counts())

