#%%
import pandas as pd

#Read Data
data = pd.read_csv("Data/BIKED_processed.csv", index_col=0).copy()
reduced = pd.read_csv("Data/BIKED_reduced.csv", index_col=0).copy()

# check missing values # HIER KÖNNTE ICH LERNEN WIE ICH ES KÜRZER SCHREIBE
missing_values_col = reduced.isna().sum()
missing_values_col = pd.DataFrame(missing_values_col)
missing_values_col.columns = ["Missing_values_Count"]

missing_values_col = missing_values_col.loc[missing_values_col["Missing_values_Count"] > 0, :]
print(len(missing_values_col))
missing_values_col
# %%

reduced["SIZE"].isna().value_counts()

# %%
