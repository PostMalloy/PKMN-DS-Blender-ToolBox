import bpy

from .operators import Split_By_VC2, Import_PDSMS_obj, Mix_Textures_VCs, Remove_Unused_Materials, Export_PDSMS_obj, Split_and_Export, Set_Camera, VC_Shortcuts, Refobjects

bl_info = {
    "name": "PKMN DS Toolbox: Main Addon",
    "author": "Freshlad",
    "description": "Handy Tools for DS Models",
    "blender": (4, 0, 0),
    "version": (1, 1, 0),
    "doc_url": "https://github.com/PostMalloy/PKMN-DS-Blender-ToolBox/tree/main",
}

# Register classes

classes = (
    Import_PDSMS_obj.PDSMSImport,
    Split_and_Export.PDSMSSplitExport,
    Export_PDSMS_obj.PDSMSExport,
    Mix_Textures_VCs.VCTextureMix,
    Remove_Unused_Materials.RemoveUnassignedMaterialsOperator,
    Split_By_VC2.SplitByVertexColorOperator,
    Set_Camera.SetCameraHGSSInterior,
    VC_Shortcuts.vcdark,
    VC_Shortcuts.vclight,
    Refobjects.importplayermodelgen4
)

# Register menus

class ImportExportSubmenu(bpy.types.Menu):
    bl_label = "Import/Export"
    bl_idname = "OBJECT_MT_import_export_submenu"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.import_pdsms")
        layout.operator("object.export_pdsms")
        layout.operator("object.export_and_split")

class MaterialToolsSubmenu(bpy.types.Menu):
    bl_label = "Material Tools"
    bl_idname = "OBJECT_MT_Material_Tool_submenu"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.cut_to_tiles") #Nils pixel look script is housed here if it is installed
        layout.operator("object.mixvctextures")
        layout.operator("object.remove_unassigned_materials")

class CameraSubmenu(bpy.types.Menu):
    bl_label = "Camera Tools"
    bl_idname = "OBJECT_Camera_Tool_submenu"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.set_camera_hgss_interior")

class VCSubmenu(bpy.types.Menu):
    bl_label = "VC Tools"
    bl_idname = "OBJECT_VC_Tool_submenu"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.set_vc_brush_gflight")
        layout.operator("object.set_vc_brush_gfdark")

class RefSubmenu(bpy.types.Menu):
    bl_label = "Reference Objects"
    bl_idname = "OBJECT_Reference_submenu"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.playermodel_gen4")

class CustomMenu(bpy.types.Menu):
    bl_label = "PKMN DS Toolbox"
    bl_idname = "OBJECT_MT_pkmn_ds_toolbox"

    def draw(self, context):
        layout = self.layout
        layout.menu(ImportExportSubmenu.bl_idname)  # Add the submenus
        layout.menu(MaterialToolsSubmenu.bl_idname)
        layout.menu(CameraSubmenu.bl_idname)
        layout.menu(VCSubmenu.bl_idname)
        layout.menu(RefSubmenu.bl_idname)
        layout.operator("mesh.split_by_vertex_color")

def draw_item(self, context):
    layout = self.layout
    layout.menu(CustomMenu.bl_idname)

menus = (
    ImportExportSubmenu,
    MaterialToolsSubmenu,
    CameraSubmenu,
    VCSubmenu,
    RefSubmenu,
    CustomMenu
)

def register():
    bpy.types.VIEW3D_HT_header.append(draw_item)
    for cls in classes:
        bpy.utils.register_class(cls)
    for mns in menus:
        bpy.utils.register_class(mns)


def unregister():
    bpy.types.VIEW3D_HT_header.remove(draw_item)
    for cls in classes:
        bpy.utils.unregister_class(cls)
    for mns in menus:
        bpy.utils.unregister_class(mns)


if __name__ == "__main__":
    register()
