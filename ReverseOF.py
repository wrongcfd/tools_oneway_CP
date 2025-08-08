import numpy as np
import os

vel_data = np.loadtxt('GASCANS_bottom_U.xy')
tur_data = np.loadtxt('GASCANS_bottom_k_nut_epsilon.xy')
# sp=29 # start point to end
Uref=5.66
u_data = vel_data[:, 3] /Uref
v_data = vel_data[:, 5]/Uref
w_data = vel_data[:, 4]/Uref
k_data = tur_data[:, 3]
d = 1.0/10.0*0.04
# 将数据分为坐标和数值列
u_coordinates = vel_data[:, 0]
v_coordinates = vel_data[:, 2]
w_coordinates = vel_data[:, 1]

fcoordname =  'CPvel_hillN10geo_d=0.1' + ".txt"

Nx = len(u_data)
Ny = len(v_data)
Nz = len(w_data)

fcoord = open(fcoordname, "w")
fcoord.write("velocity\n")
fcoord.write("u v w K\n")
for i in range(0,Nx):
			fcoord.write(str(u_data[i]) + " " + str(v_data[i]) + " " + str(w_data[i]) + " " + str(k_data[i]) + "\n")

fcoord.close()

# Read the original file content
input_filename = fcoordname
with open(input_filename, 'r') as file:
    content = file.readlines()

# Write the content to a new file with Unix line endings
unix_filename = 'CPvel_hillN10geo_d=0.1_unix.txt'
with open(unix_filename, 'w', newline='\n') as file:
    file.writelines(content)
# Remove the original file
os.remove(input_filename)
print("vel file completed !!")
#========================coords====================================#
# 将数据分为坐标和数值列
u_coordinates = vel_data[:, 0] /0.04 -5 
v_coordinates = vel_data[:, 2] /0.04 + d/0.04
w_coordinates = vel_data[:, 1] /0.04


fcoordname =  'CPcoords_hillN10geo_d=0.1' + ".txt"

fcoord = open(fcoordname, "w")

for i in range(0,Nx):
			fcoord.write(str(u_coordinates[i]) + " " + str(v_coordinates[i]) + " " + str(w_coordinates[i]) + "\n")

fcoord.close()

# Read the original file content
input_filename = fcoordname
with open(input_filename, 'r') as file:
    content = file.readlines()

# Write the content to a new file with Unix line endings
unix_filename = 'CPcoords_hillN10geo_d=0.1_unix.txt'
with open(unix_filename, 'w', newline='\n') as file:
    file.writelines(content)

# Remove the original file
os.remove(input_filename)
print("coords file completed !!")