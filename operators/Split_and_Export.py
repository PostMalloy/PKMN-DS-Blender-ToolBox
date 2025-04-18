import bpy
import os

from bpy import context
from bpy.props import StringProperty, BoolProperty
from bpy.types import Operator

from . import Split_By_VC2, Export_PDSMS_obj

class PDSMSSplitExport(bpy.types.Operator):
    """Split object by VC and export all resulting meshes at once"""          # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.export_and_split"      # Unique identifier for buttons and menu items to reference.
    bl_label = "Split and Export all as .obj"      # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}      # Enable undo for the operator.

   #def execute(self,context):
        #tbd
    #return {'FINISHED'}