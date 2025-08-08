import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import os


D=0.5
Ny = 5

name =f'_D={D}'
d=1.0/ 10

Line=np.loadtxt('tool_cp/Uf.xy')
ur=0.1
h=1
nuf=5.399e-06
u = Line[0:49,1] /ur; y = Line[0:49,0]/h
Linek=np.loadtxt('tool_cp/k.xy')
k = Linek[0:49,1] / ur/ur

# Fit interpolation (cubic spline)
fit_func = interp1d(y, u, kind='cubic', fill_value='extrapolate')
fit_funck = interp1d(y, k, kind='cubic', fill_value='extrapolate')

# New y values
newy = np.arange(d/2 , D , d)
newu = fit_func(newy)
newk = fit_funck(newy)

# Grid size
Nx = int(4 * 10)

Nz = Nx
print(newy, Ny)

# Write to file
rname = "CPvel" + name + '.txt'
with open('vel.txt' , 'w') as f:
    f.write("velocity\n")
    f.write("u v w K\n")
    for i in range(Nx):
        for j in range(Ny):
            for k in range(Nz):
                u_val = newu[j]
                k_val = newk[j]
                f.write(f"{u_val:.6e} 0.0 0.0 {k_val:.6e}\n")
# # --- Write top wall to file ---
# fname_top = "CPvel_top" + name + '.txt'
# with open(fname_top, 'w') as f:
#     for i in range(Nx):
#         for j in reversed(range(Ny)):
#             for k in range(Nz):
#                 u_val = newu[j]
#                 k_val = newk[j]
#                 f.write(f"{u_val:.6e} 0.0 0.0 {k_val:.6e}\n")
                
# Function to convert DOS to UNIX format
def convert_dos_to_unix(input_file, output_file):
    with open(input_file, 'r', newline='') as infile:
        content = infile.read()

    content_unix = content.replace('\r\n', '\n')

    with open(output_file, 'w', newline='\n') as outfile:
        outfile.write(content_unix)
            # Remove the original file
    os.remove(input_file)

# Convert the file to UNIX format
convert_dos_to_unix('vel.txt', rname)

# # Optional plot
# plt.plot(y, u, 'o', label='Original')
# plt.plot(newy, newu, '-x', label='Fitted')
# plt.xlabel('y/h')
# plt.ylabel('u/ur')
# plt.legend()
# plt.grid()
# plt.show()