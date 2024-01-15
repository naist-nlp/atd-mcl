# ATD-MCL: Arukikata Travelogue Dataset with Geographic Entity Mention, Coreference, and Link Annotation

## How to Restore the ATD-MCL Data

1. Install necessary Python libraries, for example, using `pip install -r requirements.txt`.
1. Obtain the Arukikata Travelogue Dataset (ATD) original data (`data.zip`) from the NII IDR site <https://www.nii.ac.jp/dsc/idr/arukikata/>.
1. Decompress `data.zip` and then move `data` directory to under `atd` directory (or create a symbolic link to `data` directory in `atd` directory).
1. Excute `bin/gen_full_data_json.sh`.
    - The restored data will be placed at `atd-mcl/full/main/json` and `atd-mcl/full/main/json_per_doc/`.
    - The data used for calculating inter-annotator aggreement scores will be placed at `atd-mcl/full/agreement/`.
1. Excute `bin/gen_full_data_tsv.sh`.
    - The restored data will be placed at `atd-mcl/full/main/link_tsv`, `atd-mcl/full/main/link_tsv_per_doc`, `atd-mcl/full/main/mention_tsv`, and `atd-mcl/full/main/mention_tsv_per_doc`.

## Data Statistics

The Set-A data consists of 100 documents annotated only with mention and coreference information. The Set-B data consists of 100 documents annotated with mention, coreference, and link information. (An entity corresponds to a coreference cluster of mentions.)

|     |#Doc|#Sent |#Word  |#Mention|#Entity|
|--   |--  |--    |--     |--      |--     |
|Set-A| 100| 5,949| 85,741|   6,052|  3,131|
|Set-B| 100| 6,324| 87,074|   6,119|  3,208|
|Total| 200|12,273|172,815|  12,171|  6,339|

## Official Data Split

We used the following data split in the experiments in [our paper](https://arxiv.org/abs/2305.13844).

|      |Source set|#Doc|
|--    |--        |--  |
|train1|A         | 100|
|train2|B         |  10|
|dev   |B         |  10|
|test1 |B         |  40|
|test2 |B         |  40|

## Data Format

### JSON Data Format

The JSON data (`atd-mcl/full/main/json` and `atd-mcl/full/main/json_per_doc`) holds full annotation information as follows.

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
          "M001": {
            ...
          },
        },
        "entities": {
          "E001": {
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
    - Some sentences with an ID that has a branch number (e.g., "026-01" and "026-02") indicate that a text in the original ATD data was split into those multiple sentences.
    ~~~~
    "sentences": {
      "001": {
        "section_id": "001",
        "text": "奈良公園のアイドル「しか」で~す。",
        "mention_ids": [
          "M001"
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
      "M001": {
        "sentence_id": "001",
        "entity_id": "E001",
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
      "E001": {
        "original_entity_id": "C1",
        "entity_type_merged": "FAC",
        "has_name": true,
        "has_reference": true,
        "best_ref_type": "OSM",
        "best_ref_url": "https://www.openstreetmap.org/way/456314269",
        "best_ref_query": "奈良公園",
        "member_mention_ids": [
          "M001",
          "M011"
        ]
      },
    ~~~~

### Mention TSV Data Format

The mention TSV data (`atd-mcl/full/main/mention_tsv` and `atd-mcl/full/main/mention_tsv_per_doc`) holds mention-related annotation information as follows.

- 1st column: document_id
- 2nd column: section_id:sentence_id
- 3rd column: Sentence `text`
- 4th column: Mention information with the following elements. Multiple mentions are enumerated with ";".
  - 1st element: mention_id
  - 2nd element: `span`
  - 3rd element: `entity_type`
  - 4th element: mention `text`
  - 5th element: `entity_id`
  - 6th element: `generic`
  - 7th element: `ref_spec_amb`
  - 8th element: `ref_hie_amb`

Example:
~~~~
00019	002:004	奈良の有名スポットですよね!	M002,0:2,LOC_NAME,奈良,E002,,,ref_hie_amb;M011,3:9,LOC_OR_FAC,有名スポット,E001,,,
~~~~
### Link TSV Data Format

The link TSV data (`atd-mcl/full/main/link_tsv` and `atd-mcl/full/main/link_tsv_per_doc`) holds link-related annotation information.
Specifically, entities and their member mentions (except for GENERIC and SPEC_AMB entities/mentions) are listed in TSV rows.
The column with a non-empty `entity_id` value corresponds to an entity, and the column with a non-empty `mention_id` value corresponds to a member mention of the preceding entity column.

Example:

|#document_id|entity_id|mention_id|best_ref_type|best_ref_url|best_ref_query|best_ref_is_overseas|second_A_ref_type|second_A_ref_url|second_A_ref_query|second_A_ref_is_overseas|second_B_ref_type|second_B_ref_url|second_B_ref_query|second_B_ref_is_overseas|entity_type|span|normalized_name|mention_text|ref_hie_amb|sentence_id|sentence_text|
|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
|00019|E002|-|OSM|https://www.openstreetmap.org/relation/3227707|奈良市||OSM|https://www.openstreetmap.org/relation/358631|奈良県||||||LOC|-|奈良|-|-|
|00019|-|E002:M002|-|-|-|-|-|-|-|-|-|-|-|-|LOC_NAME|0:2|-|奈良|ref_hie_amb|002:004|奈良の有名スポットですよね!|

Notes:
- `mention_id` column values acutally represent "entity_id:mention_id".
- `sentence_id` column values acutally represent "section_id:sentence_id".

## Detailed Data Specification

See `docs/data_specification`.

## Contact

- Shohei Higashiyama <shohei.higashiyama [at] nict.go.jp>
- Hiroki Ouchi <hiroki.ouchi [at] is.naist.jp>

## Acknowledgements

This study was supported by JSPS KAKENHI Grant Number JP22H03648.

## Citation

- Shohei Higashiyama, Hiroki Ouchi, Hiroki Teranishi, Hiroyuki Otomo, Yusuke Ide, Aitaro Yamamoto, Hiroyuki Shindo, Yuki Matsuda, Shoko Wakamiya, Naoya Inoue, Ikuya Yamada, and Taro Watanabe. Arukikata Travelogue Dataset with Geographic Entity Mention, Coreference, and Link Annotation. arXiv:2305.13844, May 2023. https://arxiv.org/abs/2305.13844
