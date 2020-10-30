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
df.hist(by ='hour',grid='True',column =['total_items'])

# %%
