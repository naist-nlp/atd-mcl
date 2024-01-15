#!/bin/bash

ATD_ORIG_DIR=atd/data
ATD_MCL_DIR=atd-mcl

################################################################
# Convert json files to tsv files

# main set-a
python src/convert_json_to_tsv.py \
       -i atd-mcl/full/main/json_per_doc/set-a \
       -o1 atd-mcl/full/main/mention_tsv_per_doc/set-a \
       -o2 atd-mcl/full/main/link_tsv_per_doc/set-a

# main set-b
python src/convert_json_to_tsv.py \
       -i atd-mcl/full/main/json_per_doc/set-b \
       -o1 atd-mcl/full/main/mention_tsv_per_doc/set-b \
       -o2 atd-mcl/full/main/link_tsv_per_doc/set-b
