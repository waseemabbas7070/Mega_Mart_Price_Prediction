from .dataload import Loader
import pandas as pd

PATH = r'artifacts\Train.csv'
loader = Loader
data =loader.data_loader(PATH)

class Clean:
    def __init__(self):
        pass
    def data_clean(self,data=data):
        data
