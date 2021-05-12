import bpy


# Based on https://blender.stackexchange.com/questions/148550
class NumeratedOutputField(bpy.types.PropertyGroup):
    output_directory: bpy.props.StringProperty(
        name="Output",
        default="",
        subtype="FILE_PATH",
    )

class RenderText(bpy.types.Operator):
    bl_idname = "collection.render_text"
    bl_label = "Render numerated text from collection"
    
    def execute(self, context):
        selected = context.collection
        print("Collection selected: " + selected.name)
        
        # Text can be retrieved and written to object.data.body
        text_reference = selected.all_objects[0]
        print("Storing original text: " + text_reference.data.body)
        original_data = text_reference.data.body
        
        # Hide all objects except selected collection, camera, and lights
        self.set_other_objects(True, [selected])
        
        # range second argument is exclusive
        for number in range(0, 10):
            # A text can be composed of multiple objects
            # Alter each object to represent the current number
            self.write_collection_texts(selected, str(number))
            
            # Render
            # Follows naming convention: Text_col1_0.png, Text_col1_1.png, and so on
            self.render(
                context.scene.numerated_output["output_directory"],
                f"Text_{selected.name}_{number}.png"
            )
        
        # Reset text objects to its original state
        self.write_collection_texts(selected, original_data)
        # Show all other objects in the scene again
        self.set_other_objects(False, [])

        return {"FINISHED"}

    # Sets all collection objects' .data.body property to the argument text
    def write_collection_texts(self, collection, text):
        for text_object in collection.all_objects:
                text_object.data.body = text
    
    # If set = 1, display objects, if set = 0, hide objects
    # TODO: Rewrite ignore_collections
    def set_other_objects(self, set, ignore_collections):
        # Flattens list of collections into list of objects
        ignore_objects = [object.name for collection in ignore_collections for object in collection.all_objects]

        for c in bpy.data.collections:
            for o in c.all_objects:
                if o.name in ignore_objects:
                    continue
                # Only hide object types that could interfere with the numerator render
                if o.type not in ["MESH", "CURVE", "SURFACE", "FONT"]:
                    continue
                # Set or unset object
                if set is True:
                    print("Hiding: " + o.name)
                else:
                    print("Displaying: " + o.name)

                o.hide_render = set

    def render(self, output_directory, filename):
        print("Render arguments:")
        print(output_directory)
        print(filename)
        bpy.context.scene.render.filepath = output_directory + filename
        bpy.ops.render.render(use_viewport = True, write_still=True)

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
        
        row = layout.row()
        row.operator(RenderText.bl_idname, text="Render", icon="CONSOLE")


classes = [NumeratedOutputField, RenderText, TextNumerate]

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
