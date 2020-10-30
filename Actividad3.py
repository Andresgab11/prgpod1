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
g = sns.histplot(data=df, x="total_items", multiple="stack", hue="dicount%")
for q in df.age.quantile([.25, .5, .75]):
    g.axvline(q, linestyle=":")
    g.text(q, 5, q)