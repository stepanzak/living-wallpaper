from pyora import Project, TYPE_LAYER, Renderer
from PIL import Image
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("path")

args = parser.parse_args()

ora_file_path = Path(args.path)

if not ora_file_path.exists():
    print("The file doesn't exist")
    raise SystemExit(1)

project = Project.load(ora_file_path)

# layers can be referenced in order
for layer in project.children:
    if layer.type == TYPE_LAYER:
        layer.hidden = False

# project.save(ora_file_path)
r = Renderer(project)
final = r.render()  # returns PIL Image()
final.save(ora_file_path.with_suffix(".png"))
