# %%
import pandas as pd

df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")
df.head()

# %%
df.describe()

# %%
import seaborn as sns
sn =  sns.read_csv("ulabox_orders_with_categories_partials_2017.csv")
sns.set_theme(style="white")

# %%
sns.displot(x="customer", data=df)

# %%
sn.boxplot(by ='discount',grid='True',column =['weekday'], color='red')

# %%
