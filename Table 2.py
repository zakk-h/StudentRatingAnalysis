import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy import stats
from math import sqrt
import seaborn as sns
import re

# extract tags, count tag occurrence，compute tag frequency and dump into dataframe
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
    return df['tag'].value_counts().to_frame(name='tag_number')

def High_low_professor_tag_analysis():
    df = pd.read_csv(src, usecols=['Professor_ID', 'School_name', 'Department_ID','Star_rating', 'Tags'])
    high_rating_professor = df[(df['Star_rating'] >= 3.5) & (df['Star_rating'] <= 5.0)].drop_duplicates(['Professor_ID','School_name','Department_ID'], 'first', False) #high 3.5-5.0
    low_rating_professor  = df[(df['Star_rating'] <= 2.4) & (df['Star_rating'] >= 1.0)].drop_duplicates(['Professor_ID','School_name','Department_ID'], 'first', False) #low 1.0-2.4
    high_professor_number = high_rating_professor ['Professor_ID'].count()
    print('high_professor_number：', high_professor_number)
    low_professor_number = low_rating_professor ['Professor_ID'].count()
    print('low_professor_number：', low_professor_number)
    high_professor_tag_count = extract_tag(high_rating_professor)
    low_professor_tag_count  = extract_tag(low_rating_professor)
    res = pd.concat([high_professor_tag_count,low_professor_tag_count],axis=1)
    res.columns = ["high_professor_tag_count", "low_professor_tag_count"]
    res["high_professor_tag_perc"] = res["high_professor_tag_count"].apply(lambda x: x/res["high_professor_tag_count"].sum())
    res["low_professor_tag_perc"] = res["low_professor_tag_count"].apply(lambda x: x/res["low_professor_tag_count"].sum())
    res.to_csv('tags.csv')
    return res

def chisquare(df): # 610152	110092
    a = df['high_professor_tag_count'].tolist()
    b = df['low_professor_tag_count'].tolist()
    cohen_w=[]
    for i in range(len(a)):
        # goodness of fit https://stackoverflow.com/questions/51894150/python-chi-square-goodness-of-fit-test-to-get-the-best-distribution
        obs = []
        asum = a[i]+b[i]
        bsum = 610152+110092
        obs.append(a[i])
        obs.append(b[i])
        exp = [610152/bsum*asum, 110092/bsum*asum]
        chi_chisquare = stats.chisquare(obs, exp)
        print('stat： {:.2f}，P： {:.3f}'.format(*chi_chisquare))
        cohen_w.append(round(np.sqrt(chi_chisquare[0]/ sum(exp)),2))
    print(cohen_w)
    
if __name__ == '__main__':
    # your file path
    src = r"C:\Users\zheng\OneDrive\博士阶段-文档\何吉波-RateMyProfessor\Dataset from RateMyProfessor.com for professors' teaching evaluation.csv"
    res = High_low_professor_tag_analysis()
    print(res)
    chisquare(res)