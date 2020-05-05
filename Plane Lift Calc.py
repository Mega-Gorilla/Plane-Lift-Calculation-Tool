
#defalut value
Air_density = 1.2250 #kg/m^3 空気比質量空気密度
wing_size = 12 #m2 翼面積
Relative_speed = 10 #m/s 流速
Angle_of_attack = 2 #迎え角 2は2°下に傾いてる。

print("値を入力してください。/ Please enter a value.")
print("気圧 日本周辺平均 1013hpa/ Barometric pressure Japan area average 1013hpa" )
print()

Barometric_pressure = float(input("気圧/Barometric Pressure[hpa]："))
temp = float(input("気温/Temperature[°C]]:"))
Air_density = Barometric_pressure/(2.87*(temp+273.15))

#入力データ表示↓
print("気圧/Barometic Pressure[hpa]",Barometric_pressure)
print("気温/Temperature[°C]",temp)
print("空気密度/Air Density[kg/m^3]",Air_density)

#Lift_Coefficient
CL = 0.7
CD = 0.02

#揚力は
#Ｌ＝1/2{1.2(kg/m3)*10^2   (m2/s2)*12(m2)*0.7}=５０４（Ｎ : kg.m/s2）
#抗力は
#Ｄ＝１４（Ｎ : kg.m/s2）

#calc L
L = (1/2)*(Air_density*(Relative_speed**2)*wing_size*CL) #(N)
#calc D
D = (1/2)*(Air_density*(Relative_speed**2)*wing_size*CD) #(N)

print("L=",L,"N  D=",D,"N")