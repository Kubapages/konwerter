import sys
import json
import yaml
import xml.etree.ElementTree as ET
from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser(description="Konwerter plików .xml, .json, .yml/.yaml")
    parser.add_argument("input_file", help="Ścieżka do pliku wejściowego")
    parser.add_argument("output_file", help="Ścieżka do pliku wyjściowego")
    return parser.parse_args()

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def save_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

def load_xml(file_path):
    tree = ET.parse(file_path)
    return tree.getroot()

def save_xml(data, file_path):
    tree = ET.ElementTree(data)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)

def convert_data(input_file, output_file):
    data = None
    if input_file.endswith('.json'):
        data = load_json(input_file)
    elif input_file.endswith('.yml') or input_file.endswith('.yaml'):
        data = load_yaml(input_file)
    elif input_file.endswith('.xml'):
        data = load_xml(input_file)
    else:
        print("Nieobsługiwany format pliku wejściowego")
        sys.exit(1)

    if output_file.endswith('.json'):
        save_json(data, output_file)
    elif output_file.endswith('.yml') or output_file.endswith('.yaml'):
        save_yaml(data, output_file)
    elif output_file.endswith('.xml'):
        save_xml(data, output_file)
    else:
        print("Nieobsługiwany format pliku wyjściowego")
        sys.exit(1)

if __name__ == "__main__":
    args = parse_args()
    convert_data(args.input_file, args.output_file)
