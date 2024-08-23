import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
def convert_dos_to_unix(input_file, output_file):
    with open(input_file, 'r', newline='') as infile:
        content = infile.read()

    content_unix = content.replace('\r\n', '\n')

    with open(output_file, 'w', newline='\n') as outfile:
        outfile.write(content_unix)

def generate_3d_sine_hill(amplitude_xy, length_xy, height_xy, height_3d, resolution):
    # nx = int(resolution * length_xy)
    # ny = int(resolution * height_xy)
    # nz = int(resolution * height_3d)

    with open(f"hill_2d.pc", "w") as ocout:
        for x in np.arange(0, length_xy+resolution, resolution):
            for y in np.arange(resolution/2, height_xy+resolution, resolution):
                for z in np.arange(0, height_3d+resolution, resolution):  # Extend to 3D by varying z
                    # Calculate the 3D sine hill function
                    sine_hill_xy = amplitude_xy * np.cos( np.pi *((x-2.5)/ length_xy))**2
                    if x <5 and x>0:
                    # Check if the point is within the sine hill in XY plane
                        # if y <= sine_hill_xy and not (np.isclose(x, 2.5) and np.isclose(y, 1)):
                        if y <= sine_hill_xy:
                         ocout.write(f"{x}\t{y}\t{z}\n")
                    # else:
                    #      ocout.write(f"{x}\t{0}\t{z}\n")  

# Example usage
amplitude_value_xy = 1.0  # Change this to the desired amplitude of the sine hill in XY plane
length_value_xy = 5.0  # Change this to the desired length of the sine hill in XY plane
height_value_xy = 1.0  # Change this to the desired height of the sine hill in XY plane
height_value_3d = 6.0  # Z length
res =1.0/5.0 # N+1

generate_3d_sine_hill(amplitude_value_xy,length_value_xy, height_value_xy, height_value_3d, res)

convert_dos_to_unix("hill_2d.pc", "hill_2dNnew2_unix.pc")

# # Delete the "hill_2d.pc" file
# file_to_delete = "hill_2d.pc"

# try:
#     os.remove(file_to_delete)
#     print(f"{file_to_delete} deleted successfully")
# except OSError as e:
#     print(f"Deletion failed: {e}")
# # Load data from the file
file_path = "hill_2d.pc"  # Change this to the correct filcat e path
data = np.loadtxt(file_path)

# Extract coordinates
x = data[:, 0]
y = data[:, 1]
z = data[:, 2]

# Create line data for the sine hill
x_line = np.arange(0, length_value_xy + res, res)
y_line = amplitude_value_xy * np.cos(np.pi * ((x_line - 2.5) / length_value_xy))**2
z_line = np.zeros_like(x_line)

# Plot the 3D sine hill
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, s=1, c='blue', marker='o')
ax.plot(x_line, y_line, z_line, c='red', linewidth=2, label='Sine Hill Line')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Sine Hill')
ax.legend()

plt.show()