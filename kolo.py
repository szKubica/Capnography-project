import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\Lenovo\Downloads\Dane1.csv")
df.drop(columns=['RESP', '125','17.11.21','14:39:09' ], inplace=True)
print(df.head())
df.drop(df.index[137503:], inplace=True)
df.drop(df.index[:130003], inplace=True)
df.insert(0, 'Lp', range(1, 7501))
df['ETCO2']=df['ETCO2'].astype(str).astype(int)
plt.plot(df['Lp'],df['ETCO2'], color='r')
plt.ylabel('ETCO2')
plt.show()

