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

v5=df.loc[df['válvula']=='Aberta']
x5=v5['Vazão volumétrica m3/min']
y5=v5['Pressão total Pa']

v6=df.loc[df['válvula']=='P1']
x6=v6['Vazão volumétrica m3/min']
y6=v6['Pressão total Pa']

v7=df.loc[df['válvula']=='P2']
x7=v7['Vazão volumétrica m3/min']
y7=v7['Pressão total Pa']

v8=df.loc[df['válvula']=='P3']
x8=v8['Vazão volumétrica m3/min']
y8=v8['Pressão total Pa']

v9=df.loc[df['válvula']=='P4']
x9=v9['Vazão volumétrica m3/min']
y9=v9['Pressão total Pa']

v10=df.loc[df['válvula']=='Fechada']
x10=v10['Vazão volumétrica m3/min']
y10=v10['Pressão total Pa']


plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.plot(x4,y4)
plt.plot(x5,y5,'--')
plt.plot(x6,y6,'--')
plt.plot(x7,y7,'--')
plt.plot(x8,y8,'--')
plt.plot(x9,y9,'--')
plt.plot(x10,y10,'--')
plt.legend(["3480 rpm", "2600 rpm", "1740 rpm", "800 rpm","Válv Aberta","Válv P1","Válv P2","Válv P3","Válv P4","Válv Fechada"])
plt.ylabel('Pressão(Pa)')
plt.xlabel('Vazão volumétrica m3/min')
plt.title('Curva Característica do Sistema e Curva de Instalação')
plt.grid()
plt.show()