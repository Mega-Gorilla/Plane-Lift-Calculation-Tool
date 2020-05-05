#defalut value
Flude_density = 1.2250 #kg/m3
wing_area = 12 #m2
Relative_speed = 10 #m/s
Angle_of_attack = 2 #迎え角 2は2°下に傾いてる。

#Lift_Coefficient
CL = 0.7
CD = 0.02

#揚力は
#Ｌ＝1/2{1.2(kg/m3)*10^2   (m2/s2)*12(m2)*0.7}=５０４（Ｎ : kg.m/s2）
#抗力は
#Ｄ＝１４（Ｎ : kg.m/s2）

#calc L
L = (1/2)*(Flude_density*(Relative_speed**2)*wing_area*CL) #(N)
#calc D
D = (1/2)*(Flude_density*(Relative_speed**2)*wing_area*CD) #(N)

print("L=",L,"N  D=",D,"N")