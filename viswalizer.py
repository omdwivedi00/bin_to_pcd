import open3d as o3d 
import numpy as np

print("Load a ply point cloud, print it, and render it")
ply_point_cloud = o3d.data.PLYPointCloud()
pcd = o3d.io.read_point_cloud("part_1.pcd")
points = pcd.points

print(np.asarray(points))
    # Print the points
print("Number of points:", len(points))

#o3d.visualization.draw_geometries([pcd])