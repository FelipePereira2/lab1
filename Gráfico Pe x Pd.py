import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
uri='https://raw.githubusercontent.com/Felpovysk/lab1/main/Compressor%20a%203480%20rpm(corrigido).csv'
df=pd.read_csv(uri)

va=df.loc[df['Valvula']=='Aberta']
x=va['Pressão estática Pa']
y=va['Pressão dinâmica Pa']

vp1=df.loc[df['Valvula']=='P1']
x1=vp1['Pressão estática Pa']
y1=vp1['Pressão dinâmica Pa']

vp2=df.loc[df['Valvula']=='P2']
x2=vp2['Pressão estática Pa']
y2=vp2['Pressão dinâmica Pa']

vp3=df.loc[df['Valvula']=='P3']
x3=vp3['Pressão estática Pa']
y3=vp3['Pressão dinâmica Pa']

vp4=df.loc[df['Valvula']=='P4']
x4=vp4['Pressão estática Pa']
y4=vp4['Pressão dinâmica Pa']

vf=df.loc[df['Valvula']=='Fechada']
x5=vf['Pressão estática Pa']
y5=vf['Pressão dinâmica Pa']

plt.plot(x,y,'b', label = "Válvula Aberta")
plt.plot(x1,y1,'g', label = "Válvula P1")
plt.plot(x2,y2,'r', label = "Válvula P2")
plt.plot(x3,y3, label = "Válvula P3")
plt.plot(x4,y4,'m', label = "Válvula P4")
plt.plot(x5,y5,'y', label = "Válvula Fechada")
plt.legend()
plt.ylabel('Pressão Dinâmica(Pa)')
plt.xlabel('Pressão Estática(Pa)')
plt.title('3480 RPM')
plt.grid()
plt.show()