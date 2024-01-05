import argparse
import copy
import json
import os

import logzero
from logzero import logger

from util import load_json, write_as_json, normalize_text


SENS      = 'sentences'
MENS      = 'mentions'
ENTS      = 'entities'

SEC_ID      = 'section_id'
SEN_ID      = 'sentence_id'
MEN_IDS     = 'mention_ids'
ENT_ID      = 'entity_id'
MEM_MEN_IDS = 'member_mention_ids'

TEXT      = 'text'
SPAN      = 'span'
ENT_TYPE  = 'entity_type'
GENERIC   = 'generic'
SPEC_AMB  = 'ref_spec_amb'
HIE_AMB  = 'ref_hie_amb'

NORM_NAME       = "normalized_name"
ENT_TYPE_MRG    = 'entity_type_merged'
HAS_REF         = "has_reference"
BEST_REF_TYPE   = "best_ref_type"
BEST_REF_URL    = "best_ref_url"
BEST_REF_QUERY  = "best_ref_query"
SEC_A_REF_TYPE  = "second_A_ref_type"
SEC_A_REF_URL   = "second_A_ref_url"
SEC_A_REF_QUERY = "second_A_ref_query"
SEC_B_REF_TYPE  = "second_B_ref_type"
SEC_B_REF_URL   = "second_B_ref_url"
SEC_B_REF_QUERY = "second_B_ref_query"
BEST_REF_IS_OS  = "best_ref_is_overseas"
SEC_A_REF_IS_OS = "second_A_ref_is_overseas"
SEC_B_REF_IS_OS = "second_B_ref_is_overseas"


def read_and_write(
        data: dict,
        output_tsv1_path: str,
        output_tsv2_path: str,
) -> None:

    fw1 = open(output_tsv1_path, 'w', encoding='utf-8')
    fw2 = open(output_tsv2_path, 'w', encoding='utf-8')
    fw2.write(f'#document_id\tentity_id\tmention_id\t{BEST_REF_TYPE}\t{BEST_REF_URL}\t{BEST_REF_QUERY}\t{BEST_REF_IS_OS}\t{SEC_A_REF_TYPE}\{SEC_A_REF_URL}\t{SEC_A_REF_QUERY}\t{SEC_A_REF_IS_OS}\t{SEC_B_REF_TYPE}\t{SEC_B_REF_URL}\t{SEC_B_REF_QUERY}\t{SEC_B_REF_IS_OS}\t{ENT_TYPE}\t{SPAN}\t{NORM_NAME}\tmention_text\t{HIE_AMB}\t{SEN_ID}\tsentence_text\n')

    for doc_id, doc in data.items():
        sentences = doc[SENS]
        mentions  = doc[MENS]

        for sen_id, sen in sentences.items():
            sec_id      = sen[SEC_ID]
            full_sen_id = f'{sec_id}:{sen_id}'
            sen_text    = sen[TEXT]

            mention_info_list = []
            for men_id in sen[MEN_IDS]:
                men      = mentions[men_id]
                men_type = men[ENT_TYPE]
                men_text = men[TEXT]
                span     = men[SPAN]
                ent_id   = men[ENT_ID]
                gen      = GENERIC  if GENERIC  in men and men[GENERIC]  else ''
                spec_amb = SPEC_AMB if SPEC_AMB in men and men[SPEC_AMB] else ''
                hie_amb  = HIE_AMB  if HIE_AMB  in men and men[HIE_AMB]  else ''
                mention_info_list.append(f'{men_id},{span[0]}:{span[1]},{men_type},{men_text},{ent_id},{gen},{spec_amb},{hie_amb}')

            mention_info = ';'.join(mention_info_list)
            fw1.write(f'{doc_id}\t{full_sen_id}\t{sen_text}\t{mention_info}\n')

        for ent_id, ent in doc[ENTS].items():
            ent_type  = ent[ENT_TYPE_MRG]
            norm_name = ent[NORM_NAME]       if NORM_NAME       in ent else ''
            has_ref   = ent[HAS_REF]         if HAS_REF         in ent else ''
            b_type    = ent[BEST_REF_TYPE]   if BEST_REF_TYPE   in ent else ''
            b_url     = ent[BEST_REF_URL]    if BEST_REF_URL    in ent else ''
            b_que     = ent[BEST_REF_QUERY]  if BEST_REF_QUERY  in ent else ''
            s_a_type  = ent[SEC_A_REF_TYPE]  if SEC_A_REF_TYPE  in ent else ''
            s_a_url   = ent[SEC_A_REF_URL]   if SEC_A_REF_URL   in ent else ''
            s_a_que   = ent[SEC_A_REF_QUERY] if SEC_A_REF_QUERY in ent else ''
            s_b_type  = ent[SEC_B_REF_TYPE]  if SEC_B_REF_TYPE  in ent else ''
            s_b_url   = ent[SEC_B_REF_URL]   if SEC_B_REF_URL   in ent else ''
            s_b_que   = ent[SEC_B_REF_QUERY] if SEC_B_REF_QUERY in ent else ''

            b_os   = 'overseas' if BEST_REF_IS_OS  in ent and ent[BEST_REF_IS_OS]  else ''
            s_a_os = 'overseas' if SEC_A_REF_IS_OS in ent and ent[SEC_A_REF_IS_OS] else ''
            s_b_os = 'overseas' if SEC_B_REF_IS_OS in ent and ent[SEC_B_REF_IS_OS] else ''

            fw2.write(f'{doc_id}\t{ent_id}\t-\t{b_type}\t{b_url}\t{b_que}\t{b_os}\t{s_a_type}\t{s_a_url}\t{s_a_que}\t{s_a_os}\t{s_b_type}\t{s_b_url}\t{s_b_que}\t{s_b_os}\t{ent_type}\t-\t{norm_name}\t-\t-\n')

            for men_id in ent[MEM_MEN_IDS]:
                men         = mentions[men_id]
                sen_id      = men[SEN_ID]
                sen         = sentences[sen_id]
                sen_text    = sen[TEXT]
                sec_id      = sen[SEC_ID]
                full_sen_id = f'{sec_id}:{sen_id}'
                
                men_type = men[ENT_TYPE]
                men_text = men[TEXT]
                span     = men[SPAN]
                gen      = GENERIC  if GENERIC  in men and men[GENERIC]  else ''
                assert gen == ''
                spec_amb = SPEC_AMB if SPEC_AMB in men and men[SPEC_AMB] else ''
                assert spec_amb == ''
                hie_amb  = HIE_AMB  if HIE_AMB  in men and men[HIE_AMB]  else ''

                fw2.write(f'{doc_id}\t-\t{ent_id}:{men_id}\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t{men_type}\t{span[0]}:{span[1]}\t-\t{men_text}\t{hie_amb}\t{full_sen_id}\t{sen_text}\n')

    fw1.close()
    fw2.close()
    logger.info(f'Saved: {output_tsv1_path}')
    logger.info(f'Saved: {output_tsv2_path}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_json_dir', required=True)
    parser.add_argument('-o1', '--output_tsv1_dir', required=True)
    parser.add_argument('-o2', '--output_tsv2_dir', required=True)
    args = parser.parse_args()

    logzero.loglevel(20)

    for root, dirs, files in os.walk(top=args.input_json_dir):
        for file_name in files:
            if not file_name.endswith('.json'):
                continue

            file_id = file_name.split('.json')[0]
            json_path = os.path.join(args.input_json_dir, file_name)
            data = load_json(json_path)

            tsv1_path = os.path.join(args.output_tsv1_dir, f'{file_id}.tsv')
            tsv2_path = os.path.join(args.output_tsv2_dir, f'{file_id}.tsv')
            read_and_write(data, tsv1_path, tsv2_path)


if __name__ == '__main__':
    main()
