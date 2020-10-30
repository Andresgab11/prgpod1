# %%
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from kneed import KneeLocator

df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")

dfp = df[["Baby%", "Pets%"]]

# %%

ssd=[]
ks = range(1,11)
for k in range(1,11):
    km = KMeans(n_clusters=k)
    km = km.fit(dfp)
    ssd.append(km.inertia_)

kneedle = KneeLocator(ks, ssd, S=1.0, curve="convex", direction="decreasing")
kneedle.plot_knee()
plt.show()

k = round(kneedle.knee)

print(f"Number of clusters: {k}")

# %%
kmeans = KMeans(n_clusters=k).fit(df[["Baby%", "Pets%"]])
sns.scatterplot(data=df, x="Baby%", y="Pets%", hue=kmeans.labels_)
plt.show()

# %%
cluster0 = df[kmeans.labels_ == 0]
cluster0.describe()

# %%
