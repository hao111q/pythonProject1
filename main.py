import matplotlib.pyplot as plt
import numpy
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import os
import open3d as o3d
import open3d_vis_utils as V
import io
import torch
from PIL import Image

def PointCloudDataVisualization(PointCloudData_path):
    points = np.fromfile(str(PointCloudData_path), dtype=np.float32, count=-1).reshape([-1, 4])
    skip = 10  # Skip every n points
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    point_range = range(0, points.shape[0], skip)  # skip points to prevent crash
    ax.scatter(points[point_range, 0],  # x
               points[point_range, 1],  # y
               points[point_range, 2],  # z
               c=points[point_range, 2],  # height data for color
               cmap=plt.get_cmap('Spectral'),
               marker="x")
    ax.axis('auto')  # {equal, scaled}
    plt.show()

if __name__ == '__main__':
    #PointCloudDataVisualization("000013.bin")
    '''
    y = range(3000)
    plt.figure()
    plt.plot(y)
    plt.savefig(os.path.join('../../result', '1.png'))
    plt.figure()
    z = [5,4,8,5,6,8,6,3,8,7,4,5]
    l2 = plt.plot(z)
    plt.savefig(os.path.join('../../result', '2.png'))
    '''

    points1 = np.fromfile(str('5.pcd'), dtype=np.float32, count=-1).reshape([-1, 4])
    points = np.array(points1)

    vis = o3d.visualization.Visualizer()
    vis.create_window(window_name="kitti")
    vis.get_render_option().point_size = 1
    opt = vis.get_render_option()
    opt.background_color = np.asarray([0, 0, 0])

    # 创建点云对象
    pcd = o3d.open3d.geometry.PointCloud()
    # 将点云数据转换为Open3d可以直接使用的数据类型
    pcd.points = o3d.open3d.utility.Vector3dVector(points[:,:3])
    # 设置点的颜色为白色
    pcd.paint_uniform_color([1, 1, 1])
    # 将点云加入到窗口中
    vis.add_geometry(pcd)

    vis.run()
    #vis.capture_screen_image('1.jpg')
    vis.destroy_window()

    color = vis.capture_screen_float_buffer(True)
    depth = vis.capture_depth_float_buffer(True)
    

    color = np.asarray(color)
    depth = np.asarray(depth)

    #plt.imshow(color)
    #plt.show()
    plt.imshow(color)
    plt.show()
    #plt.imsave('out.jpg', color)
    #V.draw_scenes(points = points)
    pass