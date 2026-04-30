# OS variables setup
from utils.gpu_launcher import *
force_nvidia()
# force_x11()

# Import all the packages
import mujoco
import mujoco.viewer
print("Mujoco Version: "+mujoco.__version__)

# Load model and data
model = mujoco.MjModel.from_xml_path("models/basic_scene.xml")
data = mujoco.MjData(model)
print(f"Model has {model.nbody} bodies, {model.ngeom} geoms, {model.njnt} joints")

# Simulate
mujoco.mj_step(model, data)
print("Mujoco is working")

# Render
mujoco.viewer.launch(model,data)
print("Viewer closed. Exit simulator")
