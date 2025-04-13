import bpy

from . import MainAddon
from . import Import_PDSMS_obj
from . import Export_PDSMS_obj
from . import Mix_Textures_VCs
from . import Remove_Unused_Materials
from . import Split_By_VC2

bl_info = {
    "name": "PKMN DS Toolbox: Main Addon",
    "author": "Freshlad",
    "description": "Handy Tools for DS Models",
    "blender": (4, 0, 0),
    "version": (1, 0, 0),
    "doc_url": "https://github.com/PostMalloy/PKMN-DS-Blender-ToolBox/tree/main",
}

classes = (
    MainAddon.ImportExportSubmenu,
    MainAddon.MaterialToolsSubmenu,
    MainAddon.CustomMenu,
    Import_PDSMS_obj.PDSMSImport,
    Export_PDSMS_obj.PDSMSExport,
    Mix_Textures_VCs.VCTextureMix,
    Remove_Unused_Materials.RemoveUnassignedMaterialsOperator,
    Split_By_VC2.SplitByVertexColorOperator,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
