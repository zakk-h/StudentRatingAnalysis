import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy import stats
from math import sqrt
import seaborn as sns
import re

def student_grade_test(src):
    df = pd.read_csv(src,  usecols=['Student_star', 'Grade'])
    # df = df.dropna(axis=0)
    student_grades =['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F', 'WD', 'INC', 'Not','Audit/No']
    subdfs = [df.loc[(df['Grade'] == grade) & (df['Student_star'] >= 1.0),"Student_star"] for grade in student_grades]
    
    h_test = stats.kruskal(*subdfs)
    print('Kruskal-Wallis H',h_test)

    for i in range(len(subdfs)):
        subdf = subdfs[i]
        print(df[i])
        print(subdf.describe())
    
if __name__ == '__main__':
    # your file path
    src = r"Dataset from RateMyProfessor.com for professors' teaching evaluation.csv"
    student_grade_test(src)
