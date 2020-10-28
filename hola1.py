# %%
1+1


# %%
import pandas as pd
import numpy as np

# %%
df = pd.read_csv("insurance.csv")
df.head()

# %%
print(df["age"].mean())

# %%
row_count = len(df)

print(row_count)

df[0:0]