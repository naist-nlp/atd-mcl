#!/bin/bash

ATD_ORIG_DIR=atd/data
ATD_MCL_DIR=atd-mcl

################################################################
# Convert json files to tsv files

# merged set
python src/convert_json_to_tsv.py \
       -i atd-mcl/full/main/json \
       -o1 atd-mcl/full/main/mention_tsv \
       -o2 atd-mcl/full/main/link_tsv

# main set-a train1
python src/convert_json_to_tsv.py \
       -i atd-mcl/full/main/json_per_doc/set-a/train1 \
       -o1 atd-mcl/full/main/mention_tsv_per_doc/set-a/train1 \
       -o2 atd-mcl/full/main/link_tsv_per_doc/set-a/train1

# main set-b train2
python src/convert_json_to_tsv.py \
       -i atd-mcl/full/main/json_per_doc/set-b/train2 \
       -o1 atd-mcl/full/main/mention_tsv_per_doc/set-b/train2 \
       -o2 atd-mcl/full/main/link_tsv_per_doc/set-b/train2

# main set-b dev
python src/convert_json_to_tsv.py \
       -i atd-mcl/full/main/json_per_doc/set-b/dev \
       -o1 atd-mcl/full/main/mention_tsv_per_doc/set-b/dev \
       -o2 atd-mcl/full/main/link_tsv_per_doc/set-b/dev

# main set-b test1
python src/convert_json_to_tsv.py \
       -i atd-mcl/full/main/json_per_doc/set-b/test1 \
       -o1 atd-mcl/full/main/mention_tsv_per_doc/set-b/test1 \
       -o2 atd-mcl/full/main/link_tsv_per_doc/set-b/test1

# main set-b test2
python src/convert_json_to_tsv.py \
       -i atd-mcl/full/main/json_per_doc/set-b/test2 \
       -o1 atd-mcl/full/main/mention_tsv_per_doc/set-b/test2 \
       -o2 atd-mcl/full/main/link_tsv_per_doc/set-b/test2
