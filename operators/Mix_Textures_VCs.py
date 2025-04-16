bl_info = {
    "name": "PKMN DS Toolbox: Setup Shaders",
    "blender": (4, 0, 0),
    "category": "Object",
}


import bpy
from bpy import context

class VCTextureMix(bpy.types.Operator):
    """Setup mix shader to see VCs and Textures at the same time"""          # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.mixvctextures"      # Unique identifier for buttons and menu items to reference.
    bl_label = "Setup VCs + Textures"      # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}      # Enable undo for the operator.

    def execute(self,context):

        def setup_multiply_base_color(mat):
            if not mat.use_nodes:
                return

            nodes = mat.node_tree.nodes
            links = mat.node_tree.links

            # Find the Principled BSDF node
            principled_node = None
            for node in nodes:
                if node.type == 'BSDF_PRINCIPLED':
                    principled_node = node
                    break

            if not principled_node:
                return

            # Find the existing texture connected to Base Color (if any)
            base_color_input = principled_node.inputs['Base Color']

            if not base_color_input.is_linked:
                return

            tex_node = base_color_input.links[0].from_node
            
            # Set interpolation method to closest
            if hasattr(tex_node, 'interpolation'):
                tex_node.interpolation = 'Closest'

            # Create an Attribute node for the color attribute
            attr_node = nodes.new(type='ShaderNodeAttribute')
            attr_node.attribute_name = "Attribute"  # Change this to your actual attribute name
            attr_node.location = (tex_node.location.x - 200, tex_node.location.y - 200)

            # Create a MixRGB node set to Multiply
            mix_node = nodes.new(type='ShaderNodeMixRGB')
            mix_node.blend_type = 'MULTIPLY'
            mix_node.inputs['Fac'].default_value = 1.0
            mix_node.location = (principled_node.location.x - 400, principled_node.location.y)

            # Connect attribute color and texture color to mix node
            links.new(attr_node.outputs['Color'], mix_node.inputs[1])
            links.new(tex_node.outputs['Color'], mix_node.inputs[2])

            # Remove old link
            for link in base_color_input.links:
                mat.node_tree.links.remove(link)

            # Connect mix node output to Principled BSDF Base Color
            links.new(mix_node.outputs['Color'], principled_node.inputs['Base Color'])

        # Process all materials of the active object
        obj = bpy.context.active_object
        if obj and obj.material_slots:
            for slot in obj.material_slots:
                if slot.material:
                    setup_multiply_base_color(slot.material)
                    
        # Switch to Vertex Paint mode if an active object exists
        if obj:
            bpy.ops.object.mode_set(mode='VERTEX_PAINT')
            
        return {'FINISHED'}