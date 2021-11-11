import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("分群_10%.csv")
data_eda = df.copy()
num_var = ['coef', 'adjust_price', 'inc_pub']
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
f, a = plt.subplots(2, 2, figsize=(13, 7), dpi=120)
background_color = "#F0F6FC"  # "#ecebe9"
color = "#000000"  # "#FFFFFF"
hue_color = ["#FF5003", "#428bca"]  # ["5981ad","#175a83"]
alpha = .8
hue_order = ['small', 'short']
f.patch.set_facecolor(background_color)

ax = sum(a.tolist(), [])

ax[0].axis("off")
ax[0].text(.5, 0.5, "中文Clustering&The range of price adjustment was 10%(32784 CP)\n", color=color,
           horizontalalignment='center', verticalalignment='center',
           fontsize=15,
           # fontfamily='serif'
           )

ax[0].text(.5, 0.3,
           "Increment and proportion of pulication: 3307.953914 (1.83%%)\nChange rate of overall settlement amount: 9.99%\nAdjustment of unit price:Average:-0.31 Minimum: -5.4  Maximum: 5.4\n",
           color=color, horizontalalignment='center', verticalalignment='center',
           fontsize=10,
           # fontfamily='serif'
           )
print(num_var)
for i in range(len(num_var)):
    sns.histplot(data=data_eda, x=data_eda[num_var[i]], hue='category', kde=True, ax=ax[i + 1], palette=hue_color,
                 alpha=alpha, edgecolor=background_color, hue_order=hue_order)
    ax[i].grid(color=background_color)
    ax[i].set_facecolor(background_color)
    ax[i].grid(color=color, linestyle=':', axis='y', zorder=0, dashes=(1, 5))
    ax[i].spines["top"].set_visible(False)
    ax[i].spines["right"].set_visible(False)
    ax[i].spines["left"].set_visible(False)
    ax[i].spines["bottom"].set_color(color)
    ax[i].xaxis.label.set_color(color)
    ax[i].yaxis.label.set_color(color)
    ax[i].tick_params(axis='x', colors=color)
    ax[i].tick_params(axis='y', colors=color)
    plt.tight_layout()
plt.show()
