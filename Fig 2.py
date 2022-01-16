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
df = pd.read_csv(src)
df = df.rename(index=str, columns={'Student_star': "Star rating given by students", 'Grade':'Student grade'})
print(df['Student grade'].count())
print(df['Student grade'].value_counts())

plt.style.use("seaborn-white")
fig = plt.figure(figsize=(10, 6))

plt.ylabel("Star rating given by students", fontsize=12)
plt.xlabel("Student grade", fontsize=12)

l = 0.8
w = 0.8

ax1 = plt.subplot(2, 3, 1)
ax1.set_ylim([1.0, 5.0])
g = sns.violinplot( x="Student grade", y="Star rating given by students", linewidth=l, width=w,
                   data=df[["Student grade", "Star rating given by students"]], order=['A+', 'A', 'A-'],
                   palette=sns.color_palette('Blues'))
ax1.set_xlabel("Student grade", fontsize=12)
ax1.set_ylabel("Star rating given by students", fontsize=12)

ax2=plt.subplot(2, 3, 2)
ax2.set_ylim([1.0, 5.0])
g = sns.violinplot(x="Student grade", y="Star rating given by students", linewidth=l, width=w,
                   data=df[["Student grade", "Star rating given by students"]], order=['B+', 'B', 'B-'],
                   palette=sns.color_palette('Blues'))
ax2.set_xlabel("Student grade", fontsize=12)
ax2.set_ylabel("Star rating given by students", fontsize=12)

ax3 = plt.subplot(2, 3, 3)
ax3.set_ylim([1.0, 5.0])
g = sns.violinplot(x="Student grade", y="Star rating given by students", linewidth=l, width=w,
                   data=df[["Student grade", "Star rating given by students"]], order=['C+', 'C', 'C-'],
                   palette=sns.color_palette('Blues'))
ax3.set_xlabel("Student grade", fontsize=12)
ax3.set_ylabel("Star rating given by students", fontsize=12)

ax4 = plt.subplot(2, 3, 4)
ax4.set_ylim([1.0, 5.0])
g = sns.violinplot(x="Student grade", y="Star rating given by students", linewidth=l, width=w,
                   data=df[["Student grade", "Star rating given by students"]], order=['D+', 'D', 'D-'],
                   palette=sns.color_palette('Blues'))
ax4.set_xlabel("Student grade", fontsize=12)
ax4.set_ylabel("Star rating given by students", fontsize=12)

ax5 = plt.subplot(2, 3, 5)
ax5.set_ylim([1.0, 5.0])
g = sns.violinplot(x="Student grade", y="Star rating given by students", linewidth=l, width=w,
                   data=df[["Student grade", "Star rating given by students"]],
                   order=['F', 'WD', 'INC'],
                   palette=sns.color_palette('Blues'))
ax5.set_xticklabels(['F','Drop/Withdrawal', 'Incomplete'])
ax5.set_xlabel("Student grade", fontsize=12)
ax5.set_ylabel("Star rating given by students", fontsize=12)

ax6 = plt.subplot(2, 3, 6)
ax6.set_ylim([1.0, 5.0])
g = sns.violinplot(x="Student grade", y="Star rating given by students", linewidth=l, width=w,
                   data=df[["Student grade", "Star rating given by students"]], order=['Not', 'Audit/No'],
                   palette=sns.color_palette('Blues'))
ax6.set_xticklabels(['Not sure yet','Audit/No Grade'])
ax6.set_xlabel("Student grade", fontsize=12)
ax6.set_ylabel("Star rating given by students", fontsize=12)

fig.subplots_adjust(wspace=1)
fig.tight_layout()
plt.show()
fig.savefig('violinplot_rating_grades.tiff', dpi=300)
