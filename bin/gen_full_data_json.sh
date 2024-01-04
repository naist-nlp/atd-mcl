#!/bin/bash

ATD_ORIG_DIR=atd/data
ATD_MCL_DIR=atd-mcl

################################################################
# Restore full-data docs from original and meta data, 
# and save them as a json file for each doc.

# main
python src/restore_full_documents.py \
       -i1 $ATD_ORIG_DIR/domestic/with_schedules \
       -i2 atd-mcl/meta/main/json_per_doc \
       -o atd-mcl/full/main/json_per_doc

# agreement
python src/restore_full_documents.py \
       -i1 $ATD_ORIG_DIR/domestic/with_schedules \
       -i2 atd-mcl/meta/agreement/json_per_doc \
       -o atd-mcl/full/agreement/json_per_doc

################################################################
# Merge multiple docs and save them as a json file of all input docs

# main set-a train1
python src/merge_jsons_into_single_json.py \
       -i atd-mcl/full/main/json_per_doc/set-a/train1 \
       -o atd-mcl/full/main/json/set-a_train1.json

# main set-b train2
python src/merge_jsons_into_single_json.py \
       -i atd-mcl/full/main/json_per_doc/set-b/train2 \
       -o atd-mcl/full/main/json/set-b_train2.json

# main set-a train1 & set-b train2
python src/merge_jsons_into_single_json.py \
       -i atd-mcl/full/main/json \
       -t set-a_train1.json,set-b_train2.json \
       -o atd-mcl/full/main/json/train-all.json

# main set-b dev
python src/merge_jsons_into_single_json.py \
       -i atd-mcl/full/main/json_per_doc/set-b/dev \
       -o atd-mcl/full/main/json/set-b_dev.json

# main set-b test1
python src/merge_jsons_into_single_json.py \
       -i atd-mcl/full/main/json_per_doc/set-b/test1 \
       -o atd-mcl/full/main/json/set-b_test1.json

# main set-b test2
python src/merge_jsons_into_single_json.py \
       -i atd-mcl/full/main/json_per_doc/set-b/test2 \
       -o atd-mcl/full/main/json/set-b_test2.json

# main set-b test1 & test2
python src/merge_jsons_into_single_json.py \
       -i atd-mcl/full/main/json \
       -t set-b_test1.json,set-b_test2.json \
       -o atd-mcl/full/main/json/test-all.json
