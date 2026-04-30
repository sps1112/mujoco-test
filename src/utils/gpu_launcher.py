import os

# FORCE NVIDIA GPU while running 
def force_nvidia():
    # For Visualization    
    os.environ["__NV_PRIME_RENDER_OFFLOAD"] = "1"
    os.environ["__GLX_VENDOR_LIBRARY_NAME"] = "nvidia"
    
    # For RL Training w\o visuals
    # os.environ["MUJOCO_GL"] = "egl"
    # os.environ["MUJOCO_EGL_DEVICE_ID"] = "0" # Change for GPU Index

# Another thing we can do
# os.environ["CUDA_VISIBLE_DEVICES"] = "0"

def force_x11():
    # For Wayland Compatability issues
    os.environ["XDG_SESSION_TYPE"] = "x11"
    os.environ["DISPLAY"] = ":0"
