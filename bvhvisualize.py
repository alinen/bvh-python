# bvhvisualizer.py, Aline Normoyle, 2024

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from bvh import *

def BVHVisualizeFrame(bvh, frame):
    bvh.readFrame(frame)

    # Visualize global locations of joints
    num = bvh.numJoints()
    x = np.zeros(num)
    y = np.zeros(num)
    z = np.zeros(num)
    for i in range(num):
        p = bvh.jointById(i).globalPos()
        x[i] = p[0]
        y[i] = p[1]
        z[i] = p[2]

    ax = plt.figure().add_subplot(projection='3d')
    ax.view_init(vertical_axis='y', share=True)
    ax.scatter(x, y, z, color="g", edgecolor="k")
    ax.set_title("Frame %d"%frame)
    plt.show()

class BVHAnimator:
    def __init__(self, bvh):
        self.bvh = bvh
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(projection='3d')

        self.ani = animation.FuncAnimation(self.fig, self.update, interval=5, 
            frames = range(bvh.numFrames()), init_func=self.setup_plot, blit=False)
        plt.show()

    def read_frame(self, f):
        self.bvh.readFrame(f)
        num = self.bvh.numJoints()
        x = np.zeros(num)
        y = np.zeros(num)
        z = np.zeros(num)
        for i in range(num):
            p = self.bvh.jointById(i).globalPos()
            x[i] = p[0]
            y[i] = p[1]
            z[i] = p[2]
        return x, y, z

    def setup_plot(self):
        x,y,z = self.read_frame(0)
        
        self.scat = self.ax.scatter(x, y, z, color='g', edgecolor="k")
        self.ax.view_init(vertical_axis='y', share=True)
        self.plot = self.ax.plot([0.0, 100.0], [0.0, 0.0], [0.0, 0.0], color='r')
        self.plot = self.ax.plot([0.0, 0.0], [0.0, 100.0], [0.0, 0.0], color='g')
        self.plot = self.ax.plot([0.0, 0.0], [0.0, 0.0], [0.0, 100.0], color='b')
        self.title = self.ax.set_title('Frame 0')

        # For FuncAnimation's sake, we need to return the artist we'll be using
        # Note that it expects a sequence of artists, thus the trailing comma.
        return self.scat,

    def update(self, i):
        idx = min(i, self.bvh.numFrames()-1)
        x,y,z = self.read_frame(idx)
        self.title.set_text("Frame %d"%idx)
        self.scat._offsets3d = (x,y,z) 
        return self.scat,

