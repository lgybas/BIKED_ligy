#%%
#BIKED classification 2
#doing more with functions

# imports
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.compose import ColumnTransformer

# prepocessing
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler

# classifiers
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

# performance measures
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline
from sklearn import set_config


def remove_classes_with_less_than_x_percent(data, label_col = "BIKESTYLE", percentage=0.1):
    # get the classes and their percentages
    classes = data[label_col].value_counts()
    classes = classes.reset_index()
    
    # new column 'percent'
    classes["percent"] = (classes[label_col] / data.shape[0] * 100).round(2)
    classes = classes.loc[classes["percent"] >= percentage, :]

    # keep all rows that have a lable that is in classes
    classes.columns = ["BIKESTYLE", "COUNT", "PERCENT"]
    #data = data.loc[data[label_col].isin(list(classes["BIKESTYLE"])), :] # doesn't work
    data = data.merge(classes, on="BIKESTYLE")
    data = data.iloc[:, :-3]

    return data
# %%

# code for tests

# import data
#data = pd.read_csv(Path("../BIKED_reduced.csv"), index_col=0)
#data.shape #reduced dataset: (4512, 1320)


#data_2 = remove_classes_with_less_than_x_percent(data)
#data_2 #shape (4468, 1320)
#data_2.BIKESTYLE.head()

# %%



# %%
