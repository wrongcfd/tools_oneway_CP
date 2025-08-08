import os
# User input: cell size
grid=10
h=0.5

d = 1.0/grid 
xmin = d / 2.0
zmin = d / 2.0
# User input: List of the maximum x value (xmax), y value (ymax) and z value (zmax) for each of the GASCANS boundaries. In this example there are 4 boundaries. 
xmax = 4.0 - d / 2.0
zmax = 4.0 - d / 2.0
# --- Bottom wall Y bounds ---
ymin_bot = 3 * d / 2.0
ymax_bot = h + d / 2.0
# --- Top wall Y bounds (mirrored) ---
ymin_top = 2 + 2*d - h - d / 2.0
ymax_top = 2 + 2*d - d / 2.0

# --- Grid sizes (same in both cases) ---
Nx = int((xmax - xmin) / d + 1.5)
Ny = int((ymax_bot - ymin_bot) / d + 1.5)
Nz = int((zmax - zmin) / d + 1.5)

# --- Filenames ---
real_namet = f'CPtop_D={h}.txt'
real_nameb= f'CPbot_D={h}.txt'
fcoordname_bot = f'GASCANS_bot.txt'
fcoordname_top = f'GASCANSt_top.txt'


# --- Write bottom wall ---
with open(fcoordname_bot, "w") as fcoord:
    for i in range(Nx):
        for j in range(Ny):
            for k in range(Nz):
                x = xmin + i * d
                y = ymin_bot + j * d
                z = zmin + k * d
                fcoord.write(f"{x:.6f} {y:.6f} {z:.6f}\n")

# --- Write top wall ---
with open(fcoordname_top, "w") as fcoord:
    for i in range(Nx):
        for j in reversed(range(Ny)):
            for k in range(Nz):
                x = xmin + i * d
                y = ymin_top + j * d
                z = zmin + k * d
                fcoord.write(f"{x:.6f} {y:.6f} {z:.6f}\n")

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
convert_dos_to_unix(fcoordname_top, real_namet)
convert_dos_to_unix(fcoordname_bot, real_nameb)

