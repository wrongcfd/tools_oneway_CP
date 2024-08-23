import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Function to add points based on resolution
def add_points(df, res, n):
    new_points = []
    for index, row in df.iterrows():
        x = row['x']
        y = row['y']
        z = row['z']
        for i in range(1, n+1):
            new_y = y + i * res
            new_points.append({'x': x, 'y': new_y, 'z': z})
    return pd.concat([df, pd.DataFrame(new_points)], ignore_index=True)

d = 1.0/5.0
h=0.04
res = d*h
n = 2 # Number of points to add in y direction
# Read data from file into a DataFrame
df = pd.read_csv('hill_2d.pc', sep='\s+', header=None, names=['x', 'y', 'z'])
df['x'] += 27.5
# Find maximum 'y' values for each 'x'
max_y_values = df.groupby('x')['y'].transform('max')

# Filter the DataFrame to keep rows with maximum 'y' values for each 'x'
max_y_data = df[df['y'] == max_y_values]
# Multiply filtered data (x, y, z) by 0.04
max_y_data[['x', 'y', 'z']] *= h
max_y_data[['z']] += h*0.1
# Define resolution and number of points to add

# Add more points based on resolution and increase y coordinates
extended_data = add_points(max_y_data, res, n)

# Plotting
plt.figure(figsize=(10, 6))
# Original Data
plt.scatter(df['x']*h, df['y']*h, color='blue', label='Original Data', alpha=0.5)
# Filtered Data
plt.scatter(max_y_data['x'], max_y_data['y'], color='red', label='Filtered Data', marker='x')
# Extended Data
plt.scatter(extended_data['x'], extended_data['y'], color='green', label='Extended Data', marker='o', alpha=0.5)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Original Data, Filtered Data, and Extended Data')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Save the extended data to a new file (e.g., curve_extended.pc)
extended_data.to_csv('curve_extended.pc', sep=' ', header=False, index=False, columns=['x', 'y', 'z'])

print("step1 completed !!")
# User input : cell size

# User input : List of the minium x value ( xmin ), y value ( ymin ) and z value ( zmin ) for
xmin =20 + d / 2.0 +d -5#  20 + d / 2.0 
zmin = 0 + d / 2.0
ymin =  d / 2.0 
# User input : List of the maximum x value ( xmax ), y value ( ymax ) and z value ( zmax ) for
xmax =  40- d / 2.0 +5 #40- d / 2.0 
zmax = d*10- d / 2.0 
ymax =  6.0 - d / 2.0 
# User input : Name of the GASCANS boundaries . The names are used in the file name for
wall_name ='LB_bottom '

Nx = int (( xmax - xmin) / d + 1.5)
Ny = int (( zmax - zmin) / d + 1.5)
Nz = int (( ymax - ymin) / d + 1.5)
print(f"Dataset  NY= {Ny}  Nx= {Nx} ")

fname = " sampleDictCoord " + wall_name
f = open ( fname , "w")

for i in range (0 , Nx ) : 
    if i <= (Nx/2)-2.5/d +1 or i >= (Nx/2)+2.5/d -3: 
        st = int (Ny/2)+1 
     #   print(f"Dataset st={st}, NY= {Ny} ")
        for j in range (0 , Ny ) :
                for k in range (0 , Nz ) :
                    f.write ("( " + str ( h*(xmin  + i*d)) + " " + str (h*(ymin  + k*d) )+ " " +  str( h*(zmin + j *d))  + " )\n")         

# File to append
curve_file = "curve_extended.pc"
with open(fname, "a") as f:
    with open(curve_file, "r") as curve_f:
        for line in curve_f:
            # Split the line into coordinates
            coords = line.strip().split()
            # Exchange column 2 and 3 (indexing from 0)
            coords[1], coords[2] = coords[2], coords[1]
            # Write the modified line to fname
            f.write("( " + " ".join(coords) + " )\n")

f.close ()

print("step2 completed !!")