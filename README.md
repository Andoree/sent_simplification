# simplification_evaluation

1. Clonning Easse:

```
git clone https://github.com/feralvam/easse
```

2. Replacing Sari script with the one from this repository (sari.py) so as to enable it to handle samples with a varying number of references:
```
cp sari.py $EASSE_DIR/easse
```

3. Installing EASSE:
```
cd $EASSE_DIR
pip install .
```

4. Reformat data to easse format:
```
refs_to_easse_format.py \
--input_path $PATH_TO_ANNOTATED_DATA_CSV \
--src_column $SOURCE_COLUMN_NAME \
--trg_column $TARGET_COLUMN_NAME \
--output_dataset_name $OUTPUT_DATASET_NAME \
--output_dir $OUTPUT_DIR

```
