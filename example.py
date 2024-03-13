from bvh import *
from bvhvisualize import *
import numpy as np
import matplotlib.pyplot as plt
import glm

animation = BVH()
animation.load("samba_dancing.bvh")
BVHAnimator(animation)
