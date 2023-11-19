#!/usr/bin/env python3
# ini2json.py

import sys
import argparse
import json
from configparser import ConfigParser

def ini_to_json(ini_text):
    parser = ConfigParser()
    parser.read_string(ini_text)
    # Convert INI structure to a nested dictionary
    ini_dict = {section: dict(parser.items(section)) for section in parser.sections()}
    return json.dumps(ini_dict, indent=4)

def main():
    parser = argparse.ArgumentParser(description='Convert INI configuration files to JSON format.')
    parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                        help='A filename containing INI or - for STDIN.')

    args = parser.parse_args()

    try:
        ini_input = args.file.read()
        print(ini_to_json(ini_input))
    except Exception as e:
        print(f"Error converting INI to JSON: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
