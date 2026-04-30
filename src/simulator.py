# OS variables setup
from utils.gpu_launcher import *
force_nvidia()

# Import all the packages
import mujoco
import mujoco.viewer

# Setup XML data
modelXML = """
<mujoco>
  <worldbody>
  <geom type = "box" size = ".1 .1 .1" rgba = "1 1 1 1" />
  </worldbody>
</mujoco>
"""

# Load model and data
model = mujoco.MjModel.from_xml_string(modelXML)
data = mujoco.MjData(model)

# Simulate
mujoco.mj_step(model, data)
print("Mujoco is working")

# Render
mujoco.viewer.launch(model,data)
print("Viewer exit")
