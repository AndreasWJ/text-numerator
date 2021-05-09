import bpy


class TextNumerate(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Text Numerate Panel"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        collection = context.collection

        row = layout.row()
        row.label(text="Text Numerator", icon='FONT_DATA')

        row = layout.row()
        row.label(text="Active collection is: " + collection.name)
        row = layout.row()
        row.prop(collection, "name")

        row = layout.row()
        row.operator("mesh.primitive_cube_add")


def register():
    bpy.utils.register_class(TextNumerate)


def unregister():
    bpy.utils.unregister_class(TextNumerate)


if __name__ == "__main__":
    register()
