import bpy
import math

class SetCameraHGSSInterior(bpy.types.Operator):
    """Set camera perspective, zoom and angle to match HGSS interior camera"""          # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.set_camera_hgss_interior"      # Unique identifier for buttons and menu items to reference.
    bl_label = "Set Camera - HGSS Interior"      # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}      # Enable undo for the operator.

    def execute(self,context):

        def set_viewport_angle_and_zoom(angle_z=50): #angle from melonds ripper
            for area in bpy.context.screen.areas:
                if area.type == 'VIEW_3D':
                    for space in area.spaces:
                        if space.type == 'VIEW_3D':
                            region_3d = space.region_3d
                            region_3d.view_rotation = (math.radians(angle_z), 0.15, 0.0, 0.0) #dial in exact settings later
                            region_3d.view_distance = 11 #dial in later
                            region_3d.view_perspective = 'ORTHO'
                            return

        set_viewport_angle_and_zoom()

        return {'FINISHED'}