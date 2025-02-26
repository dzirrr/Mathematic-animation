from scene import *

#PIXEL_HEIGHT = 720
RENDER_CONFIG = {
    "save_last_frame": True,
    "frame_rate": 60,
    "pixel_width": 1920,
    "pixel_height": 1080,  
    "preview": False,
    "disable_caching": True,
    "progress_bars": "leave",
    "verbose": "WARNING", 
}

with tempconfig(RENDER_CONFIG):
    SCENE_TO_RENDER().render()