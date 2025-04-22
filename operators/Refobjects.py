import bpy
import os
import addon_utils

class importplayermodelgen4(bpy.types.Operator):
    """Import a reference for the genIV player overworld sprite"""          # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.playermodel_gen4"      # Unique identifier for buttons and menu items to reference.
    bl_label = "Import genIV OW Model"      # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}      # Enable undo for the operator.

    def execute(self,context):

        # for mod in addon_utils.modules():
        #     if mod.bl_info['name'] == "PKMN DS Toolbox: Main Addon":
        #         filepath = mod.__file__
        #     else:
        #         pass
        #
        # obj_path = os.path.join(os.path.dirname(filepath), "objects", "GEN4OW.obj")

        obj_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "objects", "GEN4OW.obj")

        bpy.ops.wm.obj_import(
            filepath=obj_path, #str(self.filepath)
            forward_axis='NEGATIVE_Z',
            up_axis='Y',
        )


        # Set interpolation method to closest
        obj = bpy.context.active_object
        for mat_slot in obj.material_slots:
            mat = mat_slot.material
            if mat and mat.use_nodes:
                for node in mat.node_tree.nodes:
                    if node.type == 'TEX_IMAGE':
                        node.interpolation = 'Closest'

        return {'FINISHED'}