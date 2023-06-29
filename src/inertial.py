#!/usr/bin/env python
# Import necessary module
from stl import mesh
import numpy as np

# Define the density of the material (example: for aluminium it's 2.7 g/cm^3 = 0.0027 g/mm^3)
material_density = 0.0027  

# Load the STL files
your_mesh = mesh.Mesh.from_file('/home/samuel/catkin_ws/src/robotic-arm-refuelling/meshes/dofbot/base_link.stl')  

# Get the volume, center of gravity and the inertia tensor at the origin
volume, cog, inertia = your_mesh.get_mass_properties()

# Calculate mass
mass = material_density * volume

# Print results
print("Volume of the mesh: ", volume, " cubic mm")
print("Mass of the link: ", mass, " g")
print("Center of gravity: ", cog, " mm")
print("Inertia tensor at the origin: ", inertia)

# If you need the inertia tensor at the center of gravity, use the parallel axis theorem
inertia_at_cog = inertia - mass * (np.dot(cog, cog) * np.identity(3) - np.outer(cog, cog))
print("Inertia tensor at the center of gravity: ", inertia_at_cog)
