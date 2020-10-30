# %%
import math
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def distance(obj1, obj2, attributes):
    dist = 0
    for attr in attributes:
        dist += (obj1[attr] - obj2[attr]) ** 2
    return math.sqrt(dist)

df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")

# %%
sns.set_style("white")
sns.scatterplot(data=df, x="weekday", y="hour", hue="total_items")
plt.show()

# %%
