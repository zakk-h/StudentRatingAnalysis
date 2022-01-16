import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy import stats
from math import sqrt
import seaborn as sns
import re
# your file path
src = r"Dataset from RateMyProfessor.com for professors' teaching evaluation.csv"
df=pd.read_csv(src)
df["Online"] = df["Online"].map({0:"In-person",1:"Online"})
plt.style.use("seaborn-white")

fig, ax = plt.subplots(1, 3, figsize=(9, 4))
ax[0].set_ylim([1.0, 5.0])
sns.violinplot(x="Attendance", y="Student_star", linewidth=0.8, width=0.8,
                   data=df[["Attendance","Student_star"]],palette = ["#DEE9F3", "#C0D5E5"],ax=ax[0])
ax[0].set_xlabel("Attendance requirement",fontsize=12)
ax[0].set_ylabel("Star rating given by students",fontsize=12)
ax[0].text(-0.9, 4.8, 'A', size=12, fontweight='bold')

ax[1].set_ylim([1.0, 5.0])
sns.violinplot(x="Online", y="Student_star", linewidth=0.8, width=0.8,
                   data=df[["Online", "Student_star"]],palette=  ["#DEE9F3", "#C0D5E5"],ax=ax[1])
ax[1].set_xlabel("Delivery mode",fontsize=12)
ax[1].set_ylabel("Star rating given by students",fontsize=12)
ax[1].text(-0.9, 4.8, 'B', size=12, fontweight='bold')

ax[2].set_ylim([1.0, 5.0])
sns.violinplot(x="Online", y="Difficulty_index", linewidth=0.8, width=0.8,
                   data=df[["Online", "Difficulty_index"]],palette =  ["#DEE9F3", "#C0D5E5"],ax=ax[2])
ax[2].set_xlabel("Delivery mode",fontsize=12)
ax[2].set_ylabel("Course difficulty",fontsize=12)
ax[2].text(-0.9, 4.8, 'C', size=12, fontweight='bold')

fig.subplots_adjust(wspace=0.6)
fig.tight_layout()
plt.show()
fig.savefig('violinplot_attend_online.tiff', dpi=300)
