import pandas as pd
import matplotlib.pyplot as plt

uri='https://raw.githubusercontent.com/Felpovysk/lab1/main/Tabela%20geral%204%20velocidades%20-%20P%C3%A1gina1.csv'
df=pd.read_csv(uri)

va=df.loc[df['válvula']=='Aberta']
xa=va['Vazão volumétrica m3/min']
ya=va['Pressão total Pa']

v1=df.loc[df['válvula']=='P1']
x1=v1['Vazão volumétrica m3/min']
y1=v1['Pressão total Pa']

v2=df.loc[df['válvula']=='P2']
x2=v2['Vazão volumétrica m3/min']
y2=v2['Pressão total Pa']

v3=df.loc[df['válvula']=='P3']
x3=v3['Vazão volumétrica m3/min']
y3=v3['Pressão total Pa']

v4=df.loc[df['válvula']=='P4']
x4=v4['Vazão volumétrica m3/min']
y4=v4['Pressão total Pa']

vf=df.loc[df['válvula']=='Fechada']
xf=vf['Vazão volumétrica m3/min']
yf=vf['Pressão total Pa']

plt.plot(xa,ya)
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.plot(x4,y4)
plt.plot(xf,yf)
plt.legend(["Válv Aberta","Válv P1","Válv P2","Válv P3","Válv P4","Válv Fechada"])
plt.ylabel('Pressão(Pa)')
plt.xlabel('Vazão volumétrica m3/min')
plt.title('Curva de Instalação por Vazão')
plt.grid()
plt.show()