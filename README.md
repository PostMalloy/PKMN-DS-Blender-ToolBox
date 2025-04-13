# PKMN-DS-Blender-ToolBox
A set of simple python scripts that can help when making models for DS games, particularly the core GenIV-V pokemon games.

# Installation (Blender 4.0+)
Download the files as zip, and add the whole .zip via the blender addons menu. Make sure the plugin labeled "PKMN DS Toolbox" is active. 

# How to Use
You'll find the tools to the right of the shading menu:

<img width="737" alt="Screenshot 2025-03-28 at 4 55 05 PM" src="https://github.com/user-attachments/assets/65a413e2-f242-4b3e-b9d4-893154a8226c" />

Additional information about the .obj file format, blender and PDSMS interact is available in the wiki section. 

## Import/Export PDSMS .obj

### Export
  To use, simply highlight the object in blender (object view) and select "export to PDSMS .obj". Choose a path and the resulting object and material file will be written to that path with the names PDSMS.obj and PDSMS.mtl. 
  
  There is one caveat here: PDSMS cannot properly import **face mode vertex colors** without splitting the mesh up. This is unfortunately a limitation on the PDSMS side which I can't fix. If you're coloring in face mode, make sure to run the **"Split by Vertex Color"** addon and export each object separately. Import them into PDSMS as separate tiles, then place them together on the grid to recreate the mesh as it was in blender. More info about this operation, and why it's neccesary, is available in the wiki section (TBD).

  Even if you aren't using vertex colors, this is a handy tool because it automatically selects the correct .obj settings so the model is imported with the correct orientation, material settings, etc. in PDSMS. 

### Import
  Click "Import to PDSMS .obj", select the .obj file you're importing to blender, and you're done! Vertex colors from PDSMS will be parsed correctly and show up on the mesh. If you don't see them, make sure to set up your shaders properly for each material.

## Setup Mix Shader
  By default, blender will only let you see textures or vertex colors in the viewport, not both. To see both, like you would in game, you need to set a mix shader for each material, like so: 
  
  <img width="592" alt="Screenshot 2025-03-30 at 7 14 54 PM" src="https://github.com/user-attachments/assets/9722b364-7b6e-4a23-adae-6953373eaf77" />

This can be a bit tedious for a model with many materials, so this addon will do it for you. In object mode, highlight your object and pick "Setup VCs + Textures" in the menu. You should then be able to see both at once. It'll also automatically set the texture interpolation to "closest", so textures aren't blurry. 

## Remove Unassigned Materials

PDSMS refuse to load an .obj file if the .mtl file contains references to textures that aren't actually included in the model. This can happen if you split an object into pieces and don't remove the unused materials. This script solves that issue by removing unassigned materials from a model. Select in object mode, run "Remove Unassigned Materials", done.
