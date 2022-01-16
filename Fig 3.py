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
df = pd.read_csv(src, usecols=['Professor_ID','School_name', 'Department_ID','Star_rating', 'Difficulty_index'])
df = df.drop_duplicates(subset=['Professor_ID','School_name', 'Department_ID','Star_rating', 'Difficulty_index'])
df = df.rename(columns={'Difficulty_index': 'Course difficulty', 'Star_rating': 'Star rating'})

print(df.describe().round(2))

# regression equation
data = df[['Course difficulty', 'Star rating']].dropna()
print(len(data),data.corr())
regression = stats.linregress(x=data['Course difficulty'], y=data["Star rating"])
print("R2：", regression[2] ** 2) # 0.20
print('reg fitting: Y= %.2fX + %.2f, rvalue: %.2f, p-values: %.3f, std: %.2f' % regression)
#reg fitting: Y= -0.501X + 5.179, rvalue: -0.449, p-values: 0.0, std: 0.00

plt.style.use("seaborn-white")
g = sns.set("paper", font_scale =1.3)
g = sns.set_style("white", {"xtick.major.size": 4, "ytick.major.size": 4})
g = sns.jointplot(x = 'Course difficulty',
                  y = 'Star rating',
                  data=data,
                  fill=True,
                  thresh=0,
                  height=6,
                  ratio=8,
                  kind="kde",
                  cbar= False,
                  xlim=(1,5),
                  ylim=(1.0, 5.0),
                  space=0,
                  color='b')
g = sns.regplot(data['Course difficulty'], data['Star rating'], scatter=False, ax=g.ax_joint)
plt.text(-1.4, 1.5, r"Y=-0.50X+5.18", fontsize=10)
plt.text(-1.4, 1.3, r'$R^2$=0.20', fontsize=10)

fig = g.get_figure()
plt.show()
fig.savefig('rating_take_again_correlation.tiff', dpi=300)
