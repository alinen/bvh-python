# bvh-python
Python utilities for reading, writing, and visualizing BVH files 

## Getting Started

Runs with Python 3 and requires the dependencies [PyGLM](https://pypi.org/project/PyGLM/), [matplotlib](https://matplotlib.org/), and [NumPy](https://numpy.org/).

```
python3 -m pip install --upgrade pip
python3 -m pip install PyGLM
python3 -m pip install numpy
python3 -m pip install matplotlib
```

To visualize a BVH file, use the following code

```
animation = BVH()
animation.load(bvhfilename)
BVHAnimator(animation)
```

See `example.py` for an example. 

![samba](https://github.com/alinen/bvh-python/assets/259657/62856bdc-c08b-420f-ab06-a8af99ffd61e)
