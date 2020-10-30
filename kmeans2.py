# %%
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from kneed import KneeLocator

df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")

dfp = df[["total_items", "weekday"]]
kmeans = KMeans(n_clusters=3).fit(df[["total_items", "weekday"]])
sns.scatterplot(data=df, x="weekday", y="total_items", hue=kmeans.labels_)
plt.show()

# %%
