# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 15:30:05 2020

@author: Voxon-Ben
"""
from Suzanne import Suzanne
from voxon_python import Runtime

if __name__ == "__main__":		
	sue = Suzanne()
	print("# Indices: {}".format(sue.ICount))
	print("# Vertices: {}".format(sue.PCount))
	runtime = Runtime()
	runtime.addMesh("Sue", Suzanne())
	runtime.Loop()