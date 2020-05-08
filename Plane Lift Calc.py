
#import
import matplotlib.pyplot as plt
import math 
import numpy as np

#defalut value
Air_density = 1.2250 #kg/m^3 空気比質量空気密度
wing_size = 12 #m2 翼面積
Relative_speed = list(range(1,101)) #m/s 流速
Angle_of_attack = 2 #迎え角 2は2°下に傾いてる。

print("値を入力してください。/ Please enter a value.")
print("気圧 日本周辺平均 1013hpa/ Barometric pressure Japan area average 1013hpa" )
print()

Barometric_pressure = float(input("気圧/Barometric Pressure[hpa]："))
temp = float(input("気温/Temperature[°C]]:"))
Air_density = Barometric_pressure/(2.87*(temp+273.15))
wing_size = float(input("翼面積/Airfoil Area[cm2]:"))/10000
#Relative_speed = float(input("流速/Flow Rate:[m/s]"))
#Angle_of_attack = float(input("迎え角/angle of attack[°]"))

#入力データ表示↓
print("気圧/Barometic Pressure[hpa]",Barometric_pressure)
print("気温/Temperature[°C]",temp)
print("空気密度/Air Density[kg/m^3]",Air_density)

#Lift_Coefficient
CL = 0.9
CD = 0.04

#揚力は
#Ｌ＝1/2{1.2(kg/m3)*10^2   (m2/s2)*12(m2)*0.7}=５０４（Ｎ : kg.m/s2）
#抗力は
#Ｄ＝１４（Ｎ : kg.m/s2）

#calc L
#L = (1/2)*(Air_density*(Relative_speed**2)*wing_size*CL) #(N)
#calc D
#D = (1/2)*(Air_density*(Relative_speed**2)*wing_size*CD) #(N)
#P = L * Relative_speed
#print("揚力L=",L,"N  抗力D=",D,"N")
#print("必要動力P=",P,"W")

L = []
D = []
P = []
for speed in Relative_speed :
    L.append((1/2)*(Air_density*(speed**2)*wing_size*CL))
    D.append((1/2)*(Air_density*(speed**2)*wing_size*CD))
    P.append((1/2)*(Air_density*(speed**2)*wing_size*CL)*speed)

plt.plot(Relative_speed,L,label='Lifting Power')
plt.plot(Relative_speed,D,label='Drag')
plt.title('Lift Calculation')
plt.xlabel('Speed(m/s)')
plt.ylabel('Lifting / Drag Power (N)')
plt.grid(True) #罫線の表示
plt.legend()#凡例の表示
plt.show()