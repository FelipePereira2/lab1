import pandas as pd
import matplotlib.pyplot as plt

uri='https://raw.githubusercontent.com/FelipePereira2/lab1/main/Tabela%20geral%204%20velocidades%20-%20P%C3%A1gina1.csv'
df=pd.read_csv(uri)

v1=df.loc[df['Velocidade do compressor rpm']==3480.0]
x1=v1['Vazão volumétrica m3/min']
y1=v1['Pressão total Pa']

v2=df.loc[df['Velocidade do compressor rpm']==2600.0]
x2=v2['Vazão volumétrica m3/min']
y2=v2['Pressão total Pa']

v3=df.loc[df['Velocidade do compressor rpm']==1740.0]
x3=v3['Vazão volumétrica m3/min']
y3=v3['Pressão total Pa']

v4=df.loc[df['Velocidade do compressor rpm']==800.0]
x4=v4['Vazão volumétrica m3/min']
y4=v4['Pressão total Pa']

plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.plot(x4,y4)
plt.legend(["3480 rpm", "2600 rpm", "1740 rpm", "800 rpm"])
plt.ylabel('Pressão(Pa)')
plt.xlabel('Vazão volumétrica m3/min')
plt.title('Curva Característica do Sistema por Vazão')
plt.grid()
plt.show()
