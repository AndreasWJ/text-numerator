import bpy


# Based on https://blender.stackexchange.com/questions/148550
class NumeratedOutputField(bpy.types.PropertyGroup):
    output_directory: bpy.props.StringProperty(
        name="Output",
        default="",
        subtype="FILE_PATH",
    )

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
        output_field = context.scene.numerated_output
        row.prop(output_field, "output_directory")


classes = [NumeratedOutputField, TextNumerate]

def register():
    for i_class in classes:
        bpy.utils.register_class(i_class)

    # Add a property to select output directory
    bpy.types.Scene.numerated_output = bpy.props.PointerProperty(type=NumeratedOutputField)


def unregister():
    del bpy.types.Scene.numerated_output
    
    for i_class in classes:
        bpy.utils.unregister_class(i_class)


if __name__ == "__main__":
    register()
