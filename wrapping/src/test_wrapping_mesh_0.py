#!/usr/bin/env python

#
import sys
import os

import path_setter as ps

#
import openmeeg as om
import numpy as np

V = np.array([
  [  -0.3575,0, 0.5784, 0.525768, 0, -0.850628 ],
  [  0.3575, 0, 0.5784, -0.525768, 0, -0.850628 ],
  [                            -0.3575, 0, -0.5784, 0.525768, 0, 0.850628],
  [ 0.3575, 0, -0.5784, -0.525768, 0, 0.850628],
  [ 0, 0.5784, 0.3575, 0, -0.850628, -0.525768],
  [ 0, 0.5784, -0.3575, 0, -0.850628, 0.525768],
  [ 0, 0.68, 0, 0, -1, 0],
  [ 0.34, 0.5501, -0.2101, -0.50003, -0.808998, 0.309019],
  [ 0.34, 0.5501, 0.2101, -0.50003, -0.808998, -0.309019],
  [ 0.5501, 0.2101, 0.34, -0.808998, -0.309019, -0.50003],
  [ 0.68, 0, 0, -1, 0, 0],
  [                           0.5501, -0.2101, 0.34, -0.808998, 0.309019, -0.50003],
  [ 0.5501, 0.2101, -0.34, -0.808998, -0.309019, 0.50003],
  [                           0.5501, -0.2101, -0.34, -0.808998, 0.309019, 0.50003],
  [ 0.2101, 0.34, -0.5501, -0.309019, -0.50003, 0.808998],
  [                           -0.2101, 0.34, -0.5501, 0.309019, -0.50003, 0.808998],
  [ 0, 0, -0.68, 0, 0, 1],
  [                           -0.2101, -0.34, -0.5501, 0.309019, 0.50003, 0.808998],
  [                           0.2101, -0.34, -0.5501, -0.309019, 0.50003, 0.808998],
  [                           0.34, -0.5501, -0.2101, -0.50003, 0.808998, 0.309019],
  [                           0, -0.68, 0, 0, 1, 0],
  [                           0.34, -0.5501, 0.2101, -0.50003, 0.808998, -0.309019],
  [                           -0.34, -0.5501, -0.2101, 0.50003, 0.808998, 0.309019],
  [                           -0.34, -0.5501, 0.2101, 0.50003, 0.808998, -0.309019],
  [                           -0.5501, -0.2101, 0.34, 0.808998, 0.309019, -0.50003],
  [                           -0.2101, -0.34, 0.5501, 0.309019, 0.50003, -0.808998],
  [                           0.2101, -0.34, 0.5501, -0.309019, 0.50003, -0.808998],
  [                           -0.68, 0, 0, 1, 0, 0],
  [                           -0.5501, -0.2101, -0.34, 0.808998, 0.309019, 0.50003],
  [                           -0.5501, 0.2101, -0.34, 0.808998, -0.309019, 0.50003]
])
I = np.array([[1, 3, 4],
     [2,4,5],
     [10,3,5],
     [21,4,5]])
mesh_1 = om.Mesh(V,I)
mesh_1.info()
# TODO: mesh.read() using numpy arrays
# TODO: mesh == [ double ] , [ int ]
#mesh = om.Mesh()
#mesh.load( fileskel + "tri")
#TODO: V = [...]
# TODO: I = [...]
# TODO: mesh_1 = om.Mesh(V, I)

