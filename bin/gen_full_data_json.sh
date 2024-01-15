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
# [split-118] Merge multiple docs and save them as a json file of all input docs

# main split-118 set-a train1
python src/merge_jsons_into_single_json.py \
       -i atd-mcl/full/main/json_per_doc/set-a \
       -o atd-mcl/full/main/split-118/json/set-a_train1.json \
       -tp doc_id_lists/split-118/set-a_train1_ids.txt

# main split-118 set-b train2
python src/merge_jsons_into_single_json.py \
       -i atd-mcl/full/main/json_per_doc/set-b \
       -o atd-mcl/full/main/split-118/json/set-b_train2.json \
       -tp doc_id_lists/split-118/set-b_train2_ids.txt

# main split-118 set-a train1 & set-b train2
python src/merge_jsons_into_single_json.py \
       -i atd-mcl/full/main/split-118/json \
       -t set-a_train1.json,set-b_train2.json \
       -o atd-mcl/full/main/split-118/json/train-all.json

# main split-118 set-b dev
python src/merge_jsons_into_single_json.py \
       -i atd-mcl/full/main/json_per_doc/set-b \
       -o atd-mcl/full/main/split-118/json/set-b_dev.json \
       -tp doc_id_lists/split-118/set-b_dev_ids.txt

# main split-118 set-b test1
python src/merge_jsons_into_single_json.py \
       -i atd-mcl/full/main/json_per_doc/set-b \
       -o atd-mcl/full/main/split-118/json/set-b_test1.json \
       -tp doc_id_lists/split-118/set-b_test1_ids.txt

# main split-118 set-b test2
python src/merge_jsons_into_single_json.py \
       -i atd-mcl/full/main/json_per_doc/set-b \
       -o atd-mcl/full/main/split-118/json/set-b_test2.json \
       -tp doc_id_lists/split-118/set-b_test2_ids.txt

# main split-118 set-b test1 & test2
python src/merge_jsons_into_single_json.py \
       -i atd-mcl/full/main/split-118/json \
       -t set-b_test1.json,set-b_test2.json \
       -o atd-mcl/full/main/split-118/json/test-all.json

################################################################
# [split-712] Merge multiple docs and save them as a json file of all input docs

# main split-712 set-a train1
python src/merge_jsons_into_single_json.py \
       -i atd-mcl/full/main/json_per_doc/set-a \
       -o atd-mcl/full/main/split-712/json/set-a_train1.json \
       -tp doc_id_lists/split-712/set-a_train1_ids.txt

# main split-712 set-b train2
python src/merge_jsons_into_single_json.py \
       -i atd-mcl/full/main/json_per_doc/set-b \
       -o atd-mcl/full/main/split-712/json/set-b_train2.json \
       -tp doc_id_lists/split-712/set-b_train2_ids.txt

# main split-712 set-a train1 & set-b train2
python src/merge_jsons_into_single_json.py \
       -i atd-mcl/full/main/split-712/json \
       -t set-a_train1.json,set-b_train2.json \
       -o atd-mcl/full/main/split-712/json/train-all.json

# main split-712 set-b dev
python src/merge_jsons_into_single_json.py \
       -i atd-mcl/full/main/json_per_doc/set-b \
       -o atd-mcl/full/main/split-712/json/set-b_dev.json \
       -tp doc_id_lists/split-712/set-b_dev_ids.txt

# main split-712 set-b test1
python src/merge_jsons_into_single_json.py \
       -i atd-mcl/full/main/json_per_doc/set-b \
       -o atd-mcl/full/main/split-712/json/set-b_test1.json \
       -tp doc_id_lists/split-712/set-b_test1_ids.txt

# main split-712 set-b test2
python src/merge_jsons_into_single_json.py \
       -i atd-mcl/full/main/json_per_doc/set-b \
       -o atd-mcl/full/main/split-712/json/set-b_test2.json \
       -tp doc_id_lists/split-712/set-b_test2_ids.txt

# main split-712 set-b test1 & test2
python src/merge_jsons_into_single_json.py \
       -i atd-mcl/full/main/split-712/json \
       -t set-b_test1.json,set-b_test2.json \
       -o atd-mcl/full/main/split-712/json/test-all.json
