import bpy

class vclight(bpy.types.Operator):
    """Set vertex brush color to the typical light tone that gf uses"""          # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.set_vc_brush_gflight"      # Unique identifier for buttons and menu items to reference.
    bl_label = "Set brush to RGB(214,214,214)"      # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}      # Enable undo for the operator.

    def execute(self,context):
        # Ensure we are in Vertex Paint mode
        if bpy.context.object.mode != 'VERTEX_PAINT':
            bpy.ops.object.mode_set(mode='VERTEX_PAINT')

        # Set the vertex paint brush color
        bpy.context.tool_settings.vertex_paint.brush.color = (0.8392, 0.8392, 0.8392)

        return {'FINISHED'}

class vcdark(bpy.types.Operator):
    """Set vertex brush color to the typical dark tone that gf uses"""          # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.set_vc_brush_gfdark"      # Unique identifier for buttons and menu items to reference.
    bl_label = "Set brush to RGB(184,184,184)"      # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}      # Enable undo for the operator.

    def execute(self,context):
        # Ensure we are in Vertex Paint mode
        if bpy.context.object.mode != 'VERTEX_PAINT':
            bpy.ops.object.mode_set(mode='VERTEX_PAINT')

        # Set the vertex paint brush color
        bpy.context.tool_settings.vertex_paint.brush.color = (0.7216, 0.7216, 0.7216)

        return {'FINISHED'}