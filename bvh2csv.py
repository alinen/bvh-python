from bvh import *
import numpy as np
import glm

def OutputPositionsCSV(filename, bvh):
    file = open(filename, "w")

    # Write header
    joint = bvh.jointById(0)
    file.writelines(f"{joint.name}")
    for i in range(1,bvh.numJoints()):
        joint = bvh.jointById(i)
        file.writelines(f",{joint.name}")
    file.writelines("\n")

    # Write data
    for f in range(bvh.numFrames()):
      bvh.readFrame(f)
      joint = bvh.jointById(0)
      pos = joint.globalPos()
      file.writelines(f"{pos[0]}, {pos[1]}, {pos[2]}")
      for i in range(1,bvh.numJoints()):
          joint = bvh.jointById(i)
          pos = joint.globalPos()
          file.writelines(f",{pos[0]}, {pos[1]}, {pos[2]}")
      file.writelines("\n")

animation = BVH()
animation.load("samba_dancing.bvh")
OutputPositionsCSV("samba_dancing_pos.csv", animation)

