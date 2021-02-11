import codecs
import os
import re
from argparse import ArgumentParser
from collections import OrderedDict

import pandas as pd


def main():
    parser = ArgumentParser()
    parser.add_argument('--input_path',
                        default=r"toloka_all/toloka_all_results_24-01.csv")
    parser.add_argument('--src_column', default="INPUT:source")
    parser.add_argument('--trg_column', default="OUTPUT:output")
    parser.add_argument('--output_dataset_name', default="all")
    parser.add_argument('--output_dir', default="toloka_data_24.01_easse/")
    args = parser.parse_args()

    input_path = args.input_path
    src_column = args.src_column
    trg_column = args.trg_column
    output_dir = args.output_dir
    output_dataset_name = args.output_dataset_name
    if not os.path.exists(output_dir) and output_dir != '':
        os.makedirs(output_dir)
    output_source_path = os.path.join(output_dir, f"{output_dataset_name}.src")
    output_references_prefix = os.path.join(output_dir, f"{output_dataset_name}.ref")


    data_df = pd.read_csv(input_path, sep='\t')
    data_df[src_column] = data_df[src_column].apply(lambda x: re.sub(r"[\n\t\r]+", " ", x))
    data_df[trg_column] = data_df[trg_column].apply(lambda x: re.sub(r"[\n\t\r]+", " ", x))

    print(len(data_df[src_column].unique()))
    print(data_df.shape[0])
    data_df.drop_duplicates(subset=[src_column, trg_column], inplace=True)
    print(data_df.shape[0])

    data_dict = OrderedDict()
    for ind, row in data_df.iterrows():
        source_sentence = row[src_column]
        reference_sentence = row[trg_column]
        if data_dict.get(source_sentence) is None:
            data_dict[source_sentence] = []
        data_dict[source_sentence].append(reference_sentence)
    max_num_reference_sentences = max([len(x) for x in data_dict.values()])

    with codecs.open(output_source_path, 'w+', encoding="utf-8") as source_file:
        for i, source_sentence in enumerate(data_dict.keys()):
            source_file.write(f"{source_sentence}\n")
    ref_counter = 0
    for i in range(max_num_reference_sentences):
        output_references_path = f"{output_references_prefix}.{i}"
        with codecs.open(output_references_path, 'w+', encoding="utf-8") as references_file:
            for j, references_list in enumerate(data_dict.values()):

                if i < len(references_list):
                    ref_counter += 1
                    references_file.write(f"{references_list[i]}\n")
                else:
                    references_file.write(f"\n")
    print(f"Overall number of references: {ref_counter}")




if __name__ == '__main__':
    main()
