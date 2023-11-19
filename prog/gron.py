#!/usr/bin/env python3
# gron.py

import json
import argparse
import sys

def flatten_json_iteratively_ordered(json_obj, obj_name):
    stack = [("", json_obj)]  # Initialize stack with the root object
    result = []

    # Process the stack until empty
    while stack:
        path, current = stack.pop()
        if isinstance(current, dict):
            for k, v in current.items():
                new_path = f"{path}{k}." if path else f"{obj_name}{k}."
                stack.append((new_path, v))
        elif isinstance(current, list):
            for i, v in enumerate(current):
                new_path = f"{path}{i}."
                stack.append((new_path, v))
        else:
            # Remove the trailing '.' for non-iterable types
            path = path.rstrip('.')
            value = json.dumps(current)
            result.append(f"{path} = {value}")

    # Reverse the result to get the correct order
    return "\n".join(reversed(result))

def main():
    parser = argparse.ArgumentParser(description='Flatten JSON for easy grepping.')
    parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                        help='A filename containing JSON or - for STDIN.')
    parser.add_argument('--obj', default='', help='Optional base object name.')

    args = parser.parse_args()

    try:
        json_input = args.file.read()
        print(flatten_json_iteratively_ordered(json.loads(json_input), args.obj))
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
