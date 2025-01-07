from datatransform import Datatrans 
from sklearn.model_selection import train_test_split

dtf = Datatrans()
x, y = dtf.data_transform()
class DataSpliter:
  def __init__(self):
        pass
  def data_spliter():
        x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42)
        print(x.shape,x_train.shape,x_test.shape)
        return x_train,x_test,y_train,y_test
