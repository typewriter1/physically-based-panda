# physically-based-panda
![Screenshot](https://raw.githubusercontent.com/typewriter1/physically-based-panda/master/car.jpg)

A basic GLSL shading framework for the Panda3D game engine, supporting physically-based rendering (PBR). It will perform well even on integrated GPUs, and is easy to integrate into existing projects.

## How to Use

Copy and paste the contents of the repository into the folder of the project and import from python. Instructions about creating assets with PBR materials can be found on [this wiki page](https://github.com/typewriter1/physically-based-panda/wiki/Creating-Assets-for-physically-based-panda).

To enable, add the following to your code:
```python
#Imports
from panda3d.core import *
from direct.showbase.ShowBase import ShowBase

import pbp
...

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.framework = pbp.ShadingFramework(self.render) # Pass the node to apply the shader to. The shader will also be applied to children

...

game = Game()
game.run()
```

## Features

### Current:
- PBR shading: lambert for diffuse, GGX distribution, GGX-Schlick geometry, Smith geometry and  Schlick fresnel
- Materials and textures  using Panda3D Texture and Material objects (albedo, roughness, metallic): the final value used is the material value multiplied by texture value
- Point  and directional lights, using Panda3D PointLights
- Shadows: __note that when using point lights and shadow mapping together there may be an error thrown every frame &mdash; if this happens either avoid using point lights or disable shadows in the shader__
- Fog, using Panda3D Fog objects

### Planned:
- Spot lights
- Image based lighting (cubemaps)
- AO (maps/SSAO)
- SSR

