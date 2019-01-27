import math

from panda3d.core import *
from direct.showbase.ShowBase import ShowBase

load_prc_file_data("",
"""
framebuffer-multisample true
multisamples 2
"""
)
   
def color_from_temperature(temp):
    """Convert a kelvin temperature to RGB. Algorithm from
    http://www.tannerhelland.com/4435/convert-temperature-rgb-algorithm-code/"""
    temp /= 100
    if temp <= 66:
        red = 255
    else:
        red = temp - 60
        red = 329.698727446 * (red ** -0.133047592)
        red = max(0, red)
        red = min(255, red)
    if temp <= 66:
        green = temp
        green = 99.4708025861 * math.log(green) - 161.1195681661
        green = max(0, green)
        green = min(255, green)
    else:
        green = temp - 60
        green = 288.1221695283 * (green ** -0.0755148492)
        green = max(0, green)
        green = min(255, green)
    if temp >= 66:
        blue = 255
    else:
        if temp <= 19:
            blue = 0
        else:
            blue = temp - 10
            blue = 138.5177312231 * math.log(blue) - 305.0447927307
            blue = max(0, blue)
            blue = min(255, blue)
    return (red / 255, green / 255, blue / 255)
            
class Light:
    def __init__(self, pos = (0, 0, 0), color = color_from_temperature(3000), intensity = 700):
        self.pos = pos
        self.color = color
        self.intensity = intensity / 10

    def __repr__(self):
        return "Light at " + str(self.pos) + "of color " + str(self.color)

class ShadingFramework:
    def __init__(self, root):
        self.root = root
        self.root.set_antialias(AntialiasAttrib.MAuto)
        self.lights = []
        base.task_mgr.add(self.update, "update")

    def add_light(self, light):
        self.lights.append(light)
        print(self.lights)

    def update(self, task):
        light_positions = []
        light_colors = []
        light_intensities = []
        for light in self.lights:
            light_positions.append(light.pos)
            light_colors.append(light.color)
            light_intensities.append(light.intensity)
        self.root.set_shader_input("lightPositions", light_positions)
        self.root.set_shader_input("lightColors", light_colors)
        self.root.set_shader_input("lightIntensities", light_intensities)
        p = base.camera.get_pos(render)
        self.root.set_shader_input("camPos", (p[0], p[1], p[2]))
        self.root.set_shader_input("numLights", len(self.lights))
        return task.cont
