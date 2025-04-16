bl_info = {
    "name": "PKMN DS Toolbox: Export as PDSMS Object",
    'author': 'Freshlad',
    "blender": (4, 0, 0),
    "category": "Object",
}

import bpy
import os
from bpy import context
from bpy.props import StringProperty, BoolProperty
from bpy.types import Operator

class PDSMSExport(bpy.types.Operator):
    bl_idname = "object.export_pdsms"      # Unique identifier for buttons and menu items to reference.
    bl_label = "Export PDSMS .obj"      # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}      # Enable undo for the operator.

    # # Define this to tell 'fileselect_add' that we want a directoy
    filepath : bpy.props.StringProperty(subtype="FILE_PATH")
    directory : bpy.props.StringProperty(subtype="DIR_PATH") 

    def invoke(self, context, event):
        # Open browser, take reference to 'self' read the path to selected
        # file, put path in predetermined self fields.
        # See: https://docs.blender.org/api/current/bpy.types.WindowManager.html#bpy.types.WindowManager.fileselect_add
        context.window_manager.fileselect_add(self)
        # Tells Blender to hang on for the slow user input
        return {'RUNNING_MODAL'}

    def execute(self, context):        # execute() is called when running the operator.

        # Function to process each line starting with 'f' (like 'f 1/5/3 2/3/4 3/2/6')
        def process_f_line(line):
            parts = line.split()
            
            # Check if the line starts with 'f'
            if parts[0] == 'f':
                # Process each word block in the line
                for i in range(1, len(parts)):
                    numbers = parts[i].split('/')
                    # Append the first number to the end of the word block
                    numbers.append(numbers[0])
                    parts[i] = '/'.join(numbers)
                
                # Rejoin and return the modified line
                return ' '.join(parts)
            else:
                return line

        # Set the file path for export
        filepath = self.filepath + ".obj"

        obj = bpy.context.object
        
        mesh = obj.data
        used_materials = set()

    # Handle unused materials:

        # Check which materials are actually assigned to faces
        for poly in mesh.polygons:
            used_materials.add(poly.material_index)
        
        # Identify unused material slots
        unused_materials = [i for i in range(len(obj.material_slots)) if i not in used_materials]
        
        # Remove unassigned materials without affecting assigned ones
        for i in reversed(unused_materials):
            mesh.materials.pop(index=i)


    # Export

        # Ensure the active object is selected for export
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)

        # Export the .obj file with vertex colors
        bpy.ops.wm.obj_export(
            filepath=filepath,
            export_selected_objects=True,
            forward_axis='Y',
            up_axis='Z',
            export_colors=True  # vertex colors exported
        )

        # Input and output file paths
        input_filepath = filepath
        output_filepath = self.directory + ".conversioninprogress"

        with open(input_filepath, 'r') as infile, open(output_filepath, 'w') as outfile:
            for line in infile:
                parts = line.strip().split()
                
                # If line starts with 'v' and has more than 4 elements (indicating vertex colors are included)
                if parts and parts[0] == 'v' and len(parts) > 4:
                    coords = parts[1:4]  # First three are coordinates
                    colors = parts[4:7]  # Last three are vertex colors
                    
                    # Write vertex position line
                    outfile.write(f"v {' '.join(coords)}\n")
                    
                    # Write vertex color line separately
                    outfile.write(f"c {' '.join(colors)}\n")
                elif parts and parts[0] == 'f':
                    # Process lines starting with 'f'
                    modified_line = process_f_line(line.strip())
                    outfile.write(modified_line + "\n")
                else:
                    # Write the line as is if it doesn't match the vertex format with colors or 'f' format
                    outfile.write(line)
        os.remove(input_filepath)
        os.rename(output_filepath, input_filepath)

        #fix material file if using mix shaders in blender

        filepath = self.filepath + ".mtl"
        input_filepath = filepath
        output_filepath = self.filepath + ".conversioninprogress"

        with open(input_filepath, 'r') as infile, open(output_filepath, 'w') as outfile:
            for line in infile:
                if not line.startswith("Kd"):
                    outfile.write(line)
                    if line.startswith("map_d"):
                        filepath = line.split(maxsplit=1)[1] if len(line.split(maxsplit=1)) > 1 else ""
                        outfile.write(f"map_Kd {filepath}")
        os.remove(input_filepath)
        os.rename(output_filepath, input_filepath)

        return {'FINISHED'}