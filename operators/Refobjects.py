import bpy
import os

class importplayermodelgen4(bpy.types.Operator):
    """Import a reference for the genIV player overworld sprite"""          # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.playermodel_gen4"      # Unique identifier for buttons and menu items to reference.
    bl_label = "Import genIV OW Model"      # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}      # Enable undo for the operator.

    addon_path = os.path.dirname(os.path.realpath(__file__))
    obj_path = os.path.join(addon_path, "objects", "GEN4OW.obj")

    def execute(self,context):

        bpy.ops.wm.obj_import(
            filepath=obj_path, #str(self.filepath)
            forward_axis='-Z',
            up_axis='Y',
        )

        return {'FINISHED'}