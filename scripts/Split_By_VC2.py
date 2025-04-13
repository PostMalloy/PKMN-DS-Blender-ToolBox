import bpy
from mathutils import Color

bl_info = {
    'name': 'PKMN DS Toolbox: Split By Color',
    'author': 'FreshLad, largely based on the work of Tamas Kemenczy and Piotr Zgodziński',
    'blender': (4, 0, 0),
    'location': 'View3D > Specials > Split by Color',
    'description': 'Split object by vertex color',
    'category': 'Mesh'
}
def get_unique_vertex_colors(obj):
    """Extract unique vertex colors from the object."""
    color_set = set()
    colors = obj.data.vertex_colors.active.data # Get the active vertex color data
    
    for poly in obj.data.polygons:
        face_colors = set()
        for i in poly.loop_indices:
            r1, g1, b1, a1 = colors[i].color
            face_colors.add((r1, g1, b1))
        
        if len(face_colors) == 1:  # Ensure all vertices have the same color
            color_set.add(next(iter(face_colors)))
    
    return [Color(c) for c in color_set]

def select_faces_by_color(obj, target_color, threshold=0.01):
    """Select faces where all vertices match the target vertex color within a threshold."""
    colors = obj.data.vertex_colors.active.data
    
    for poly in obj.data.polygons:
        face_colors = set()
        for i in poly.loop_indices:
            r1, g1, b1, a1 = colors[i].color
            face_colors.add((r1, g1, b1))
        
        if len(face_colors) != 1:  # Skip faces with two or more vertex colors
            continue
        
        source_color = Color(next(iter(face_colors)))
        
        if (abs(source_color.r - target_color.r) < threshold and
            abs(source_color.g - target_color.g) < threshold and
            abs(source_color.b - target_color.b) < threshold):
            poly.select = True

def split_faces_by_vertex_color():
    """Splits the object into separate objects based on vertex colors, only if all vertices have the same color."""
    obj = bpy.context.active_object
    if obj is None or obj.type != 'MESH':
        return
    
    bpy.ops.object.mode_set(mode='OBJECT')
    unique_colors = get_unique_vertex_colors(obj)
    
    for color in unique_colors:
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.mode_set(mode='OBJECT')
        select_faces_by_color(obj, color)
        bpy.ops.object.mode_set(mode='EDIT')
        
        bpy.ops.mesh.separate(type='SELECTED')
        bpy.ops.object.mode_set(mode='OBJECT')

class SplitByVertexColorOperator(bpy.types.Operator):
    bl_label = "Split By Vertex Color"
    bl_idname = "mesh.split_by_vertex_color"
    bl_options = {'REGISTER', 'UNDO'}
    threshold: bpy.props.FloatProperty(name='Threshold', default=0.01, min=0.001, max=1.0, step=1)

    def execute(self, context):
        split_faces_by_vertex_color()
        return {'FINISHED'}