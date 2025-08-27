import numpy as np
import os
res = 10
D= 0.5
vel_data = np.loadtxt('CPHIll_inlet_py\GASCANS_bottom_U.xy')
tur_data = np.loadtxt('CPHIll_inlet_py\GASCANS_bottom_k_nut_epsilon.xy')
# sp=29 # start point to end
Uref=5.66
u_data = vel_data[:, 3] /Uref
v_data = vel_data[:, 5]/Uref
w_data = vel_data[:, 4]/Uref
k_data = tur_data[:, 3]
d = 1.0/res*0.04
# 将数据分为坐标和数值列
u_coordinates = vel_data[:, 0]
v_coordinates = vel_data[:, 2]
w_coordinates = vel_data[:, 1]

fcoordname =  'vel_hill' + ".txt"

Nx = len(u_data)
Ny = len(v_data)
Nz = len(w_data)

fcoord = open(fcoordname, "w")
fcoord.write("velocity\n")
fcoord.write("u v w K\n")
for i in range(0, Nx):
			fcoord.write(str(u_data[i]) + " " + str(v_data[i]) + " " + str(w_data[i]) + " " + str(k_data[i]) + "\n")

fcoord.close()

# Read the original file content
input_filename = fcoordname
with open(input_filename, 'r') as file:
    content = file.readlines()

# Write the content to a new file with Unix line endings
unix_filename = f'HYvel_hill_N{res}_D={D}_unix.txt'
with open(unix_filename, 'w', newline='\n') as file:
    file.writelines(content)
# Remove the original file
os.remove(input_filename)
print("vel file completed !!")
#========================coords====================================#
# 将数据分为坐标和数值列
u_coordinates = vel_data[:, 0] /0.04 - 5 
v_coordinates = vel_data[:, 2] /0.04 + d/0.04
w_coordinates = vel_data[:, 1] /0.04


fcoordname =  'coords_hill' + ".txt"
fcoord = open(fcoordname, "w")

for i in range(0,Nx):
			fcoord.write(str(u_coordinates[i]) + " " + str(v_coordinates[i]) + " " + str(w_coordinates[i]) + "\n")

fcoord.close()

# Read the original file content
input_filename = fcoordname
with open(input_filename, 'r') as file:
    content = file.readlines()

# Write the content to a new file with Unix line endings
unix_filename = f'HYcoords_hill_N{res}_D={D}_unix.txt'
with open(unix_filename, 'w', newline='\n') as file:
    file.writelines(content)

# Remove the original file
os.remove(input_filename)
print("coords file completed !!")