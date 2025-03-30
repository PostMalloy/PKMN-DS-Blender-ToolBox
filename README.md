# PKMN-DS-Blender-ToolBox
A set of simple python scripts that can help when making models for DS games, particularly the core GenIV-V pokemon games.

# Installation (Blender 4.0+)
Download the files, unzip them and install them via the blender addons menu. Make sure all plugins are active.

# How to Use
You'll find the tools to the right of the shading menu:
<img width="737" alt="Screenshot 2025-03-28 at 4 55 05 PM" src="https://github.com/user-attachments/assets/65a413e2-f242-4b3e-b9d4-893154a8226c" />

## Import/Export PDSMS .obj
Trifindo's PDSMS mapping tool accepts importing traditional .obj files into a tileset. It even accepts vertex colored .obj files! Blender can export vertex colors as part of an .obj file, and PDSMS can read them, so why are they stripped as part of the import to PDSMS? The reason is because PDSMS expects vertex colors to be written in a slightly different format than the standard .obj file from the blender export, and vice versa. It's therefore relatively simple to write a blender addon to modify the .obj file into a format that PDSMS expects (in the case of the export script) or a format that blender expects (in the case of the import one). 
### Export
  To use, simply highlight the object in blender and select "export to PDSMS .obj". Choose a path and the resulting object and material file will be written to that path. **However** there is one caveat here: PDSMS cannot properly import **face mode vertex colors** without a little help. 

### Import
  Click "Import to PDSMS .obj", select the .obj file you're importing to blender, and you're done!

## Setup Mix Shader
  By default, blender will only let you see textures or vertex colors in the viewport, not both. To see both, like you would in game, you need to set a mix shader for each material, like so: 
  
  <img width="592" alt="Screenshot 2025-03-30 at 7 14 54 PM" src="https://github.com/user-attachments/assets/9722b364-7b6e-4a23-adae-6953373eaf77" />

This can be a bit tedious for a model with many materials, so this addon will do it for you. In object mode, highlight your object and pick "Setup VCs + Textures" in the menu. You should then be able to see both at once. It'll also automatically set the texture interpolation to "closest", so textures aren't blurry. 

## Split by Vertex Color

