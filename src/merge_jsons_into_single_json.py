import argparse
import json
import os

from util import load_json, write_as_json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_dirs', required=True)
    parser.add_argument('-o', '--output_path', required=True)
    parser.add_argument('-t', '--target_file_names')
    parser.add_argument('-tp', '--target_file_names_path')
    args = parser.parse_args()

    if args.target_file_names_path:
        target_file_names = []
        with open(args.target_file_names_path, encoding='utf-8') as f:
            for line in f:
                target_fn = line.rstrip('\n') + '.json'
                target_file_names.append(target_fn)

    elif args.target_file_names:
        target_file_names = args.target_file_names.split(',')

    else:
        target_file_names = None

    data = {}

    for input_dir in args.input_dirs.split(','):
        for file_name in sorted(os.listdir(input_dir)):
            if target_file_names and not file_name in target_file_names:
                continue                    

            if not file_name.endswith('.json'):
                continue

            input_path = os.path.join(input_dir, file_name)
            data_orig = load_json(input_path)
            for doc_id, doc in data_orig.items():
                data[doc_id] = data_orig[doc_id]

    if data:
        write_as_json(data, args.output_path)


if __name__ == '__main__':
    main()
