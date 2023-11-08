import argparse
import copy
import json
import os

import logzero
from logzero import logger

from util import load_json, write_as_json, normalize_text


SENS      = 'sentences'
MENS      = 'mentions'
SEN_ID    = 'sentence_id'
TEXT      = 'text'
SPAN      = 'span'
SPAN_ORIG = 'span_in_orig_text'


def restore_full_document(
        doc_orig: dict,
        doc_meta: dict,
) -> dict:

    texts_orig = []
    for section in doc_orig:
        for text_orig in section[TEXT]:
            texts_orig.append(normalize_text(text_orig))

    doc_new = copy.deepcopy(doc_meta)
    for sen_id, sen in doc_new[SENS].items():
        if '-' in sen_id:
            span = sen[SPAN_ORIG]
            text_orig_idx = int(sen_id.split('-')[0])-1
            text_orig = texts_orig[text_orig_idx]
            text = text_orig[span[0]:span[1]]
        else:
            text_orig_idx = int(sen_id)-1
            text_orig = texts_orig[text_orig_idx]
            text = text_orig

        sen[TEXT] = text
        logger.debug(f'{sen_id} ({text_orig_idx}): {text}')
        assert sen[TEXT] != ''

    for men_id, men in doc_new[MENS].items():
        sen_id = men[SEN_ID]
        span = men[SPAN]

        sen = doc_new[SENS][sen_id]
        sen_text = sen[TEXT]
        men[TEXT] = sen_text[span[0]:span[1]]
        logger.debug(f'{men_id} text: {text}')
        assert men[TEXT] != ''

    return doc_new


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i1', '--orig_json_dir', required=True)
    parser.add_argument('-i2', '--meta_json_top_dir', required=True)
    parser.add_argument('-o', '--output_top_dir', required=True)
    args = parser.parse_args()

    logzero.loglevel(20)

    for root, dirs, files in os.walk(top=args.meta_json_top_dir):
        for file_name in files:
            if not file_name.endswith('.json'):
                continue

            doc_id = file_name.split('.json')[0]
            part_dirs = root.split(args.meta_json_top_dir)[1].strip('/')

            orig_json_path = os.path.join(args.orig_json_dir, f'{doc_id}.tra.json')
            assert os.path.isfile(orig_json_path), f'File does not exist: {orig_json_path}'
            doc_orig = load_json(orig_json_path)
            
            meta_json_path = os.path.join(root, file_name)
            assert os.path.isfile(meta_json_path), f'File does not exist: {meta_json_path}'
            data_meta = load_json(meta_json_path)
            doc_meta = data_meta[doc_id]

            output_dir = os.path.join(args.output_top_dir, part_dirs)
            assert os.path.isdir(output_dir), f'Directory does not exist: {output_dir}'

            doc_new = restore_full_document(doc_orig, doc_meta)
            data = {doc_id: doc_new}

            output_path = os.path.join(output_dir, file_name)
            write_as_json(data, output_path)


if __name__ == '__main__':
    main()
