# ATD-MCL: Arukikata Travelogue Dataset with Geographic Entity Mention, Coreference, and Link Annotation

## How to Restore the ATD-MCL Data

1. Obtain the Arukikata Travelogue Dataset (ATD) original data (`data.zip`) from the NII IDR site <https://www.nii.ac.jp/dsc/idr/arukikata/>.
1. Decompress `data.zip` and then move `data` directory to under `atd` directory (or create a symbolic link to `data` directory in `atd` directory).
1. Excute `bin/gen_full_data.sh`.
    - The restored data will be placed at `atd-mcl/full/main/json` and `atd-mcl/full/main/json_per_doc/`.
    - The data used for calculating inter-annotator aggreement scores will be placed at `atd-mcl/full/agreement/`.

## Data Format

- A document object value is assosiated with a key that represents the  document ID (e.g., `00019`). Each document object has the sets of `sections`, `sentences`, `mentions`, and `entities`.
   ~~~~
    {
      "00019": {
        "sections": {
          "001": {
          ...
          },
        },
        "sentences": {
          "001": {
          ...
          },
        },
        "mentions": {
          "001": {
            ...
          },
        },
        "entities": {
          "C1": {
            ...
          }
        }
      }
    }
    ~~~~
- A section object under `sections` is as follows:
    ~~~~
    "sections": {
      "001": {
        "sentence_ids": [
          "001",
          "002",
          "003"
        ]
      },
    ...
    ~~~~
- A sentence object under `sentences` is as follows:
    - A sentence object may have one or more geographic entity mentions.
    - Some sentences with an ID that has a branch number (e.g., "026-01" and "026-02") indicate that a single sentence in the original ATD data was split into those multiple sentences.
    ~~~~
    "sentences": {
      "001": {
        "section_id": "001",
        "text": "奈良公園のアイドル「しか」で~す。",
        "mention_ids": [
          "001"
        ]
      },
      ...
      "026-01": {
        "section_id": "013",
        "span_in_orig_text": [
          0,
          8
        ],
        "text": "とにかく広~い!",
        "mention_ids": []
      },
      "026-02": {
        "section_id": "013",
        "span_in_orig_text": [
          8,
          16
        ],
        "text": "そして静かです。",
        "mention_ids": []
      },
    ~~~~
- A mention object under `mentions` is as follows:
    - A mention object may be associated with an entity.
    ~~~~
    "mentions": {
      "001": {
        "sentence_id": "001",
        "entity_id": "C1",
        "span": [
          0,
          4
        ],
        "text": "奈良公園",
        "entity_type": "FAC_NAME"
      },
    ~~~~
- An entity object, which corresponds to a coreference cluster of one or more mentions, under `entities` is as follows:
    - An entity object is associated with one or more mentions.
    - `has_name` indicates whether at least one member mention's entity type is `*_NAME` or not.
    ~~~~
    "entities": {
      "C1": {
        "normalized_name": "奈良公園",
        "entity_label_merged": "FAC",
        "has_name": true,
        "has_reference": true,
        "best_ref_type": "OSM",
        "best_ref_url": "https://www.openstreetmap.org/way/456314269",
        "best_ref_query": "奈良公園",
        "member_mention_ids": [
          "001",
          "011"
        ]
      },
    ~~~~

## Data Specification

TODO
- entity type labels
- generic, spec_amb, hie_amb tags
- (best/second_A/second_B)_ref_*

## Official Data Split

## Contact

Geography & Language Project <https://sites.google.com/view/geography-and-language>

## Acknowledgements

## Citation

- Shohei Higashiyama, Hiroki Ouchi, Hiroki Teranishi, Hiroyuki Otomo, Yusuke Ide, Aitaro Yamamoto, Hiroyuki Shindo, Yuki Matsuda, Shoko Wakamiya, Naoya Inoue, Ikuya Yamada, and Taro Watanabe. Arukikata Travelogue Dataset with Geographic Entity Mention, Coreference, and Link Annotation. arXiv:2305.13844, May 2023. https://arxiv.org/abs/2305.13844
