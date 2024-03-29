# Data Split

## Overview

Two types of data splits are defined.

In our dataset papers, we used "split-118", which split 100 Set-B documents into 1:1:8.

|split-118|Source set|#Doc|
|--       |--        |--  |
|train1   |Set-A     | 100|
|train2   |Set-B     |  10|
|dev      |Set-B     |  10|
|test1    |Set-B     |  40|
|test2    |Set-B     |  40|

In our geocoding paper, we used "split-712", which split 100 Set-B documents into 7:1:2.

|split-712|Source set|#Doc|
|--       |--        |--  |
|train1   |Set-A     | 100|
|train2   |Set-B     |  70|
|dev      |Set-B     |  10|
|test1    |Set-B     |  10|
|test2    |Set-B     |  10|

As the difference from the split-118 data, (randomly-sampled) 30 and 30 documents in the split-118 test1 and test2 sets, respectively, have been added to the train2 set in split-712. Thus, the train1 and dev sets were identical for the two splits.

## How to Split

The detailed process of split data creation is as follows.

1. For each entity E in each document D, count the number of documents that the entity occurred except for the document itself (`NumInOtherDocs(E, D)`).
    - For example, if entities with the same link L occur in documents D1, D2, and D3, then the entities are regarded as the same entity E, and `NumInOtherDocs(E, D1)=NumInOtherDocs(E, D2)=NumInOtherDocs(E, D3)=2`.
1. For each document D, calculate `MaxEntNumInOtherDocs(D)`, which is the maximum value of `NumOtherDocs(*, D)`.
    - The lower `MaxEntNumInOtherDocs(D)` value suggests that the document D is the more difficult document in terms of mention recognition and entity disambiguation.
1. 40 Set-B documents with `0 <= MaxEntNumInOtherDocs(D) <= 3` were assigned to split-118 test2 set. The remaining 60 Set-B documents with `3 <= MaxEntNumInOtherDocs(D) <= 17` were randomly split into 10:10:40 (split-118 train2:dev:test1).

## Papers

Dataset Papers
~~~~
@inproceedings{higashiyama-etal-2024-arukikata,
    title = "Arukikata Travelogue Dataset with Geographic Entity Mention, Coreference, and Link Annotation",
    author = "Higashiyama, Shohei and Ouchi, Hiroki and Teranishi, Hiroki and Otomo, Hiroyuki and Ide, Yusuke and Yamamoto, Aitaro and Shindo, Hiroyuki and Matsuda, Yuki and Wakamiya, Shoko and Inoue, Naoya and Yamada, Ikuya and Watanabe, Taro",
    booktitle = "Findings of the Association for Computational Linguistics: EACL 2024",
    month = mar,
    year = "2024",
}
~~~~
~~~~
@inproceedings{higashiyama-etal-2024-nihongo,
    author = "東山翔平 and 大内啓樹 and 寺西裕紀 and 大友寛之 and 井手佑翼 and 山本和太郎 and 進藤裕之 and 渡辺太郎",
    title = "日本語旅行記ジオパージングデータセット{ATD-MCL}",
    booktitle ="言語処理学会第30回年次大会発表論文集",
    year = "2024",
}
~~~~

Geocoding Paper
~~~~
@inproceedings{nakatani-etal-2024-mention,
    author = "中谷響 and 寺西裕紀 and 東山翔平 and 大内啓樹 and 渡辺太郎",
    title = "メンション文脈とエントリ属性を考慮した{T}ransformer Bi-Encoderによるジオコーディング",
    booktitle ="言語処理学会第30回年次大会発表論文集",
    year = "2024",
}
~~~~
