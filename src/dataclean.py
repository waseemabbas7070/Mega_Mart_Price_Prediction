from .dataload import Loader
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import pandas as pd

PATH = r'artifacts\Train.csv'
loader = Loader
data =loader.data_loader(PATH)

class Clean:
    def __init__(self):
        pass
    def data_clean(self,data=data):
      mylist = []
      for i in data['Item_Fat_Content']:
        if i == 'Low Fat':
         mylist.append('Low Fat')
        elif i == 'low fat':
            mylist.append('Low Fat')
        elif i == 'Regular':
            mylist.append('Regular')
        else:
            mylist.append('Regular')
        data['Item_Fat_Content'] = mylist  
         
        x =data.drop("Item_Outlet_Sales",axis=1)
        y = data["Item_Outlet_Sales"] 
        # categorical and numeric 
        cat = x.select_dtypes(object).columns.tolist()
        num = x.select_dtypes('number').columns.tolist()
        # Imputer for fill null or missing values on Categorical data
        impute= SimpleImputer(strategy='most_frequent')
        impute.fit(x[cat])
        x[cat]=impute.transform(x[cat])
        
        # Imputer for fill null or missing values on Numerical  data
        impute = SimpleImputer(strategy='mean')
        impute.fit(x[num])
        x[num]=impute.transform(x[num])




