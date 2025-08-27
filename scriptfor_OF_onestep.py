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
        for i in range(1, n):
            new_y = y + i * res
            new_points.append({'x': x, 'y': new_y, 'z': z})
    return pd.concat([df, pd.DataFrame(new_points)], ignore_index=True)

res = 10
region = 0.5

d = 1.0 / res  # grid resolution
celln = n = int(res * region)   # flat wall cell number   # n = Number of points to add in y direction coupling

print(f"Dataset  flat wall cell number: {celln}  coupling cell= {n} ")

h = 0.04
res = d * h

# Read data from file into a DataFrame
df = pd.read_csv('hill_2d.pc', sep='\s+', header=None, names=['x', 'y', 'z'])
df['x'] += 17.5   # start of the hill in OF domain

# Find maximum 'y' values for each 'x'
max_y_values = df.groupby('x')['y'].transform('max')

# Filter the DataFrame to keep rows with maximum 'y' values for each 'x'
max_y_data = df[df['y'] == max_y_values].copy()
# Multiply filtered data (x, y, z) by 0.04
max_y_data[['x', 'y', 'z']] *= h
max_y_data[['y']] += h * region

# Add more points based on resolution and increase y coordinates
extended_data = add_points(max_y_data, res, n)

# Plotting
# plt.figure(figsize=(10, 6))
# plt.scatter(df['x']*h, df['y']*h, color='blue', label='Original Data', alpha=0.5)
# plt.scatter(max_y_data['x'], max_y_data['y'], color='red', label='Filtered Data', marker='x')
# plt.scatter(extended_data['x'], extended_data['y'], color='green', label='Extended Data', marker='o', alpha=0.5)

# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Original Data, Filtered Data, and Extended Data')
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()

# Save the extended data to a new file
extended_data.to_csv('hill_extended.pc', sep=' ', header=False, index=False, columns=['x', 'y', 'z'])
print("step1 completed !!")

# ---------------- step2 ----------------

# User input : domain bounds
xmin = 5 + d / 2.0 + d
zmin = d / 2.0
ymin = d / 2.0

xmax = 35 - d / 2.0
zmax = d * celln - d / 2.0  # vertical
ymax = 6.0 - d / 2.0        # spanwise

wall_name = 'OF_bottom '

Nx = int((xmax - xmin) / d + 1.5)
Ny = int((zmax - zmin) / d + 1.5)
Nz = int((ymax - ymin) / d + 1.5)
print(f"Dataset  NY= {Ny}  Nx= {Nx}  Nz={Nz}")

# -------- Collect all points here --------
all_points = []

# Grid points
for i in range(0, Nx-1):
        for j in range(0, Ny):
            for k in range(0, Nz):
                all_points.append([
                    h * (xmin + i*d),
                    h * (ymin + k*d),
                    h * (zmin + j*d)
                ])

# Curve points
with open("hill_extended.pc", "r") as curve_f:
    for line in curve_f:
        coords = line.strip().split()
        # Swap y and z
        coords[1], coords[2] = coords[2], coords[1]
        all_points.append([float(c) for c in coords])

# -------- Remove duplicates --------
points_df = pd.DataFrame(all_points, columns=["x", "y", "z"])
points_df = points_df.drop_duplicates()

# -------- Write back to file --------
fname = "sampleDictCoord_" + wall_name.strip()
with open(fname, "w") as f:
    for _, row in points_df.iterrows():
        f.write(f"( {row['x']} {row['y']} {row['z']} )\n")

print("step2 completed !!")
