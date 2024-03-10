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

import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv(Path("../Data/data_processed_cl.csv"), index_col=0)
data.shape 
#reduced dataset: (4512, 1320)
#cleaned dataset: (4511, 1847)
y = data["BIKESTYLE"]
y_2 = data["category"]
X = data.drop(columns=["BIKESTYLE", "category"])

#%%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)


# Create the correlation matrix, using the absolute values.
# For our purpose, it doesn't matter whether the correlation is positive or negative.
corrMatrix = X_train.corr().abs()

# Plot a heatmap of the correlation matrix.
fig, ax = plt.subplots(figsize=(18,18))
sns.heatmap(corrMatrix, annot=True);


#data_2 = remove_classes_with_less_than_x_percent(data)
#data_2 #shape (4468, 1320)
#data_2.BIKESTYLE.head()

# %%
# Select the upper triangle of the correlation matrix.
upper = corrMatrix.where(np.triu(np.ones(corrMatrix.shape), k=1).astype(bool))
# Find the index of those feature columns with correlation greater than 0.95.
to_drop = [column for column in upper.columns if any(upper[column] > 0.95)]

# Drop the columns from the train set.
X_train_selected = X_train.drop(columns=to_drop)

# Drop the columns from the test set.
X_test_selected = X_test.drop(columns=to_drop)


# %%

#save the new dataset
