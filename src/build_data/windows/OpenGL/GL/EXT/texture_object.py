'''OpenGL extension EXT.texture_object

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.texture_object to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension introduces named texture objects.  The only way to name
	a texture in GL 1.0 is by defining it as a single display list.  Because
	display lists cannot be edited, these objects are static.  Yet it is
	important to be able to change the images and parameters of a texture.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/texture_object.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.EXT.texture_object import *
### END AUTOGENERATED SECTION