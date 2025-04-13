bl_info = {
    "name": "PKMN DS Toolbox: Import PDSMS Object",
    "blender": (4, 0, 0),
    "category": "Object",
}

import bpy
import os
from bpy import context
from bpy.props import StringProperty, BoolProperty
from bpy.types import Operator

class PDSMSImport(bpy.types.Operator):
    bl_idname = "object.import_pdsms"
    bl_label = "Import PDSMS .obj"
    bl_options = {'REGISTER', 'UNDO'}      # Enable undo for the operator.

    filepath : bpy.props.StringProperty(subtype="FILE_PATH")
    directory : bpy.props.StringProperty(subtype="DIR_PATH") 
    #somewhere to remember the address of the file

    def invoke(self, context, event): # See comments at end  [1]

        context.window_manager.fileselect_add(self) 
        #Open browser, take reference to 'self' 
        #read the path to selected file, 
        #put path in declared string type data structure self.filepath

        return {'RUNNING_MODAL'}  
        # Tells Blender to hang on for the slow user input

    def execute(self, context):

        input_filepath = str(self.filepath)
        output_filepath = str(self.directory)+"_conversion.obj"
        v_lines = []
        c_lines = []
        other_lines = []

        # Read file and categorize lines
        with open(input_filepath, 'r') as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line.startswith('v'):
                    v_lines.append(stripped_line)
                elif stripped_line.startswith('c'):
                    c_lines.append(stripped_line[1:].strip())  # Remove 'c' before storing
                else:
                    other_lines.append(stripped_line)

        # Match and merge
        min_length = min(len(v_lines), len(c_lines))
        merged_lines = [f"{v_lines[i]} {c_lines[i]}" for i in range(min_length)]

        # Add unmatched v_lines and c_lines if any
        merged_lines.extend(v_lines[min_length:])
        merged_lines.extend(c_lines[min_length:])

        # Combine everything and write to output file
        with open(output_filepath, 'w') as outfile:
            for line in merged_lines + other_lines:
                outfile.write(line + '\n')
        #import modified obj
        bpy.ops.wm.obj_import(
            filepath=output_filepath, #str(self.filepath)
            forward_axis='Y',
            up_axis='Z',
        )
        os.remove(output_filepath)

        return {'FINISHED'}