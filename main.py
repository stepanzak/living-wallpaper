from pyora import Project, TYPE_LAYER
from PIL import Image

project = Project.load("testORA.ora")
width, height = project.dimensions
print(width, height)

# layers can be referenced in order
for layer in project.children:
    if layer.type == TYPE_LAYER:
        print(layer.name)
        print(layer.z_index, layer.z_index_global, layer.opacity, layer.visible, layer.hidden)

