from  .dataclean import Clean
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

obj = Clean()
x,y = obj.data_clean()
class Datatrans:
    def __init__(self):
        pass
    def data_transform(self,x=x,y=y):
   
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
                # Scaling of the Numeric Data
         scaler = StandardScaler()
         scaler.fit(x[num])
         x[num] = scaler.transform(x[num])   
                #  encoder = LabelEncoder()
         encoder = LabelEncoder()
         for i in cat:
          x[i] = encoder.fit_transform(x[i])
         return x,y