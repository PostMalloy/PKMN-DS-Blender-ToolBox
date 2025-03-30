bl_info = {
    "name": "Remove Unassigned Materials",
    'author': 'Freshlad',
    "blender": (4, 0, 0),
    "category": "Object",
}

import bpy

def remove_unassigned_materials():
    obj = bpy.context.object
    
    mesh = obj.data
    used_materials = set()
    
    # Check which materials are actually assigned to faces
    for poly in mesh.polygons:
        used_materials.add(poly.material_index)
    
    # Identify unused material slots
    unused_materials = [i for i in range(len(obj.material_slots)) if i not in used_materials]
    
    # Remove unassigned materials without affecting assigned ones
    for i in reversed(unused_materials):
        obj.data.materials.pop(index=i)
    
class RemoveUnassignedMaterialsOperator(bpy.types.Operator):
    """Remove Unassigned Materials from Selected Object"""
    bl_idname = "object.remove_unassigned_materials"
    bl_label = "Remove Unassigned Materials"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        remove_unassigned_materials()
        return {'FINISHED'}

# Register classes
def register():
    bpy.utils.register_class(RemoveUnassignedMaterialsOperator)

def unregister():
    bpy.utils.unregister_class(RemoveUnassignedMaterialsOperator)

if __name__ == "__main__":
    register()