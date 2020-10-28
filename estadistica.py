# %%
import pandas as pd
import numpy as np

# %%
df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")
df.shape


# %%
df.info()

# %%
df.min()

# %%
df.max()

# %%
df.mean()

# %%
df.mode()

# %%
df.median()

# %%
df.std()

# %%
df.quantile(0.25)

# %%
df.quantile(0.5)


# %%
df.quantile(0.75)

# %%
df.quantile(1)

# %%
