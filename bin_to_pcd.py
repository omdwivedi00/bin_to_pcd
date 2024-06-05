import struct
import numpy as np
import open3d as o3d
import os 
from tqdm.auto import tqdm
# Define the size of a float in bytes
size_float = 4

# Initialize the list to store point cloud data
list_pcd = []

# Define the path to the binary file
bin_file_path = 'part_1.bin'
# bin_file_path = 'sample.bin'

# Read the binary file
with open(bin_file_path, "rb") as f:

    file_size = os.path.getsize(bin_file_path)
    
    with tqdm(total=file_size, desc="Reading point cloud data") as pbar:
        byte = f.read(size_float * 4)
        while byte:
            x, y, z, intensity = struct.unpack("ffff", byte)
            
            list_pcd.append([x, y, z])
            byte = f.read(size_float*4)
            pbar.update(size_float * 4)
        

# Convert the list to a numpy array
np_pcd = np.asarray(list_pcd)

# Create a PointCloud object
pcd = o3d.geometry.PointCloud()

# Assign points to the PointCloud object
pcd.points = o3d.utility.Vector3dVector(np_pcd)

# Save the point cloud to a file
o3d.io.write_point_cloud("part_12.pcd", pcd)
