# simplification_evaluation

1. Clone Easse:

```
git clone https://github.com/feralvam/easse
```

2. Replace Sari script with the one from this repository (sari.py) so as to enable it to handle samples with a varying number of references:
```
cp sari.py $EASSE_DIR/easse
```

3. Install EASSE:
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
--output_dataset_name $DATASET_NAME \
--output_dir $REFERENCES_DIR
```
5. Run Easse evaluation:
```
easse evaluate \
--test_set custom \
--metrics bleu,sari \
--refs_sents_paths $REFERENCES_DIR/$DATASET_NAME.ref.0,$REFERENCES_DIR/$DATASET_NAME.ref.1,$REFERENCES_DIR/$DATASET_NAME.ref.2,$REFERENCES_DIR/$DATASET_NAME.ref.3,$REFERENCES_DIR/$DATASET_NAME.ref.4,$REFERENCES_DIR/$DATASET_NAME.ref.5,$REFERENCES_DIR/$DATASET_NAME.ref.6,$REFERENCES_DIR/$DATASET_NAME.ref.7,$REFERENCES_DIR/$DATASET_NAME.ref.8,$REFERENCES_DIR/$DATASET_NAME.ref.9,$REFERENCES_DIR/$DATASET_NAME.ref.10,$REFERENCES_DIR/$DATASET_NAME.ref.11,$REFERENCES_DIR/$DATASET_NAME.ref.12,$REFERENCES_DIR/$DATASET_NAME.ref.13,$REFERENCES_DIR/$DATASET_NAME.ref.14,$REFERENCES_DIR/$DATASET_NAME.ref.15,$REFERENCES_DIR/$DATASET_NAME.ref.16,$REFERENCES_DIR/$DATASET_NAME.ref.17,$REFERENCES_DIR/$DATASET_NAME.ref.18,$REFERENCES_DIR/$DATASET_NAME.ref.19,$REFERENCES_DIR/$DATASET_NAME.ref.20  \
-=orig_sents_path $REFERENCES_DIR/$DATASET_NAME.src \
--sys_sents_path $MODEL_PREDICTION_PATH -q
```

