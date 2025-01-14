from .dataload import Loader
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import pandas as pd

PATH = r'artifacts\Train.csv'
loader = Loader()
data =loader.data_loader(PATH)

class Clean:
    def __init__(self):
        pass
    def data_clean(self,data=data):
        x =data.drop("Item_Outlet_Sales",axis=1)
        y = data["Item_Outlet_Sales"] 
        mylist = []
        for i in x['Item_Fat_Content']:
            if i == 'low fat':
             mylist.append('Low Fat')
            elif i == 'LF':
                mylist.append('Low Fat')
            elif i == 'reg':
                mylist.append('Regular')
            else:
                mylist.append(i) 
        x['Item_Fat_Content']=mylist
        return x,y
  




