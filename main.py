from builtins import dict, list, str
from typing import Any, Dict
from pyora import Project, TYPE_LAYER, Renderer
from PIL import Image
import argparse
from pathlib import Path
from ruamel.yaml import YAML
import random

yaml = YAML()

parser = argparse.ArgumentParser()

_ = parser.add_argument("path_to_ora_file")
_ = parser.add_argument("path_to_yaml_config")

args = parser.parse_args()

ora_file_path = Path(args.path_to_ora_file)
yaml_config_path = Path(args.path_to_yaml_config)

if not ora_file_path.exists():
    print(f"The ora file {ora_file_path} doesn't exist")
    raise SystemExit(1)

if not yaml_config_path.exists():
    print(f"The yaml config file {yaml_config_path} doesn't exist")
    raise SystemExit(1)


def loadYamlConfig(yaml_config_path) -> dict[str, Any]:
    with open(yaml_config_path, "r") as f:
        return yaml.load(f)


def parseConfig(
    config: dict[str, Any],
) -> list[str]:  # returns a list of layers to be shown in the final image
    for item in config:
        print(item)
    return ["a"]


def renderORAwithOnlySomeLayers(
    ora_file_path: Path, layers: list[str], exported_png_path: Path
):
    project = Project.load(ora_file_path)

    # layers can be referenced in order
    for layer in project.children:
        if layer.type == TYPE_LAYER:
            layer.hidden = False

    # project.save(ora_file_path)
    r = Renderer(project)
    final = r.render()  # returns PIL Image()
    final.save(ora_file_path.with_suffix(".png"))


# from https://maxhalford.github.io/blog/weighted-sampling-without-replacement/
def weighted_sample_without_replacement(population, weights, k):
    v = [random.random() ** (1 / w) for w in weights]
    order = sorted(range(len(population)), key=lambda i: v[i])
    return [population[i] for i in order[-k:]]


parseConfig(loadYamlConfig(yaml_config_path))
