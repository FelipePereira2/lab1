import matplotlib.pyplot as plt
import pandas as pd
uri='https://raw.githubusercontent.com/Felpovysk/lab1/main/Tabela%20geral%204%20velocidades%20-%20P%C3%A1gina1.csv'
df=pd.read_csv(uri)

va=df.loc[df['válvula']=='Aberta']
x=va['Vazão volumétrica m3/min']
y=va['FP']

vp1=df.loc[df['válvula']=='P1']
x1=vp1['Vazão volumétrica m3/min']
y1=vp1['FP']

vp2=df.loc[df['válvula']=='P2']
x2=vp2['Vazão volumétrica m3/min']
y2=vp2['FP']

vp3=df.loc[df['válvula']=='P3']
x3=vp3['Vazão volumétrica m3/min']
y3=vp3['FP']

vp4=df.loc[df['válvula']=='P4']
x4=vp4['Vazão volumétrica m3/min']
y4=vp4['FP']

vf=df.loc[df['válvula']=='Fechada']
xf=vf['Vazão volumétrica m3/min']
yf=vf['FP']

v5=df.loc[df['Velocidade do compressor rpm']==3480.0]
x5=v5['Vazão volumétrica m3/min']
y5=v5['FP']

v6=df.loc[df['Velocidade do compressor rpm']==2600.0]
x6=v6['Vazão volumétrica m3/min']
y6=v6['FP']

v7=df.loc[df['Velocidade do compressor rpm']==1740.0]
x7=v7['Vazão volumétrica m3/min']
y7=v7['FP']

v8=df.loc[df['Velocidade do compressor rpm']==800.0]
x8=v8['Vazão volumétrica m3/min']
y8=v8['FP']

plt.plot(x,y)
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.plot(x4,y4)
plt.plot(xf,yf)
plt.plot(x5,y5,'--')
plt.plot(x6,y6,'--')
plt.plot(x7,y7,'--')
plt.plot(x8,y8,'--')
plt.legend(["Válv Aberta","Válv P1","Válv P2","Válv P3","Válv P4","Válv Fechada","3480 rpm", "2600 rpm", "1740 rpm", "800 rpm"])
plt.ylabel('Fator de Potência')
plt.xlabel('Vazão volumétrica m3/min')
plt.title('Fator de Potência por Vazão')
plt.show()
