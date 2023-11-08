import json
import unicodedata

from logzero import logger


SPACES    = ''.join([' ', chr(0x2028), '　'])
CTRL_CHR1 = '\x7f'


def load_json(
        input_path: str,
) -> dict:

    with open(input_path) as f:
        logger.info(f'Read: {input_path}')
        data = json.load(f)
    return data


def write_as_json(
        data: dict,
        output_path: str,
) -> None:

    with open(output_path, 'w') as fw:
        json.dump(data, fw, ensure_ascii=False, indent=2)
    logger.info(f'Saved: {output_path}')


def normalize_text(
        text: str,
) -> str:

    return (unicodedata.normalize('NFKC', text)
            .replace(CTRL_CHR1, ' ').replace(' ', '　').strip(SPACES))
