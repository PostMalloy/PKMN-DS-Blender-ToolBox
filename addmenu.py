import bpy

bl_info = {
    'name': 'PKMN DS Toolbox',
    'author': 'Freshlad',
    'version': (0, 3),
    'blender': (4, 0, 0),
    'description': 'Handy Tools for DS Models',
}

class ImportExportSubmenu(bpy.types.Menu):
    bl_label = "Import/Export"
    bl_idname = "OBJECT_MT_import_export_submenu"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.import_pdsms")
        layout.operator("object.export_pdsms")

class MaterialToolsSubmenu(bpy.types.Menu):
    bl_label = "Material Tools"
    bl_idname = "OBJECT_MT_Material_Tool_submenu"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.cut_to_tiles") #Nils pixel look script is housed here if it is installed
        layout.operator("object.mixvctextures")

class CustomMenu(bpy.types.Menu):
    bl_label = "PKMN DS Toolbox"
    bl_idname = "OBJECT_MT_pkmn_ds_toolbox"

    def draw(self, context):
        layout = self.layout
        layout.menu(ImportExportSubmenu.bl_idname)  # Add the submenus
        layout.menu(MaterialToolsSubmenu.bl_idname)
        layout.operator("mesh.split_by_vertex_color")
        layout.operator("object.remove_unassigned_materials")

def draw_item(self, context):
    layout = self.layout
    layout.menu(CustomMenu.bl_idname)

def register():
    bpy.utils.register_class(ImportExportSubmenu)
    bpy.utils.register_class(MaterialToolsSubmenu)
    bpy.utils.register_class(CustomMenu)
    bpy.types.VIEW3D_HT_header.append(draw_item)

def unregister():
    bpy.utils.unregister_class(ImportExportSubmenu)
    bpy.utils.unregister_class(MaterialToolsSubmenu)
    bpy.utils.unregister_class(CustomMenu)
    bpy.types.VIEW3D_HT_header.remove(draw_item)

if __name__ == "__main__":
    register()

    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=CustomMenu.bl_idname)
