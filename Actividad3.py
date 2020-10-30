# %%
import pandas as pd

df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")
df.head()

# %%
df.describe()

# %%
import seaborn as sns
sns.set_theme(style="white")

# %%
sns.displot(x="customer", data=df)

# %%
df.boxplot(by ='hour',grid='True',column =['total_items'], color='red')

# %%
sns.histplot(data=df, x="hour", y="total_items")

# %%
g = sns.histplot(data=df, x="hour", multiple="stack", hue="weekday")
for q in df.hour.quantile([.25, .5, .75]):
    g.axvline(q, linestyle=":")
    g.text(q, 5, q)

# %%
df.corr()

# %%
sns.heatmap(df.corr(), annot=True)

# %%
