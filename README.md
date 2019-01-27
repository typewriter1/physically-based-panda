# physically-based-panda
![Screenshot](https://raw.githubusercontent.com/typewriter1/physically-based-panda/master/car.jpg)

A basic GLSL shading framework for the Panda3D game engine, supporting physically-based rendering (PBR). It will perform well even on integrated GPUs.

## How to Use

Copy and paste the contents of the repository into the folder of the project and import from python.

## Features

Current:
- PBR shading: lambert for diffuse, GGX distribution, GGX-Schlick geometry, Smith geometry and  Schlick fresnel
- Materials and textures  using Panda3D Texture and Material objects (albedo, roughness, metallic): the final value used is the material value multiplied by texture value
- Point  and directional lights, using Panda3D PointLights

Planned:
- Spot lights
- Image based lighting (cubemaps)
- Shadows (p3d_ShadowViewMatrix)
- Fog
- AO (maps/SSAO)
- SSR

