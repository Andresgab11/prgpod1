# %%
import math
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
def distance(obj1, obj2, attributes):
    dist = 0
    for attr in attributes:
        dist += (obj1[attr] - obj2[attr]) ** 2
    return math.sqrt(dist)

df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")

# %%
sns.set_style("white")
sns.scatterplot(data=df, x="Baby%", y="Pets%", hue=kmeans.labels_)
plt.show()

# %%
k = 3
D = df
attributes = ["Baby%", "Pets%"]

centroids = None
new_centroids = D.sample(n=k)[attributes]
print(new_centroids)

while centroids is None or not centroids.equals(new_centroids):
    centroids = new_centroids
    clusters = D.apply(lambda obj: np.argmin(centroids.apply(lambda centroid: distance(centroid, obj, attributes), axis=1)), axis=1)
    new_centroids = pd.DataFrame(D[clusters == index][attributes].mean() for index in range(k))
    sns.scatterplot(data=df, x="Baby%", y="Pets%", hue=clusters)
    plt.show()
    print(new_centroids)
