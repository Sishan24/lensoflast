# Experiment Plan and Results Log

## Experiment matrix

| ID | Question | Comparison | Main measure |
|---|---|---|---|
| E01 | Can a simple baseline read date crops? | Baseline OCR/rules | CER, exact string accuracy |
| E02 | Does sequence modelling help? | CNN vs CNN-BiLSTM | CER, WER |
| E03 | Which recurrent unit is suitable? | RNN vs LSTM vs GRU | CER, convergence |
| E04 | Does attention help? | CTC vs attention decoder | CER, exact date accuracy |
| E05 | Does denoising help? | Original vs autoencoder output | CER on degraded subset |
| E06 | Which optimiser works best? | SGD vs Momentum vs Nesterov | Validation loss, convergence |
| E07 | Does regularisation improve generalisation? | No regularisation vs L1/L2/dropout | Train-validation gap |
| E08 | What is the effect of augmentation? | No augmentation vs realistic augmentation | Held-out CER |
| E09 | Can semantic date fields be distinguished? | MLP variants | Macro F1, confusion matrix |
| E10 | What information is lost under compression? | PCA/SVD feature experiment | Reconstruction/retained variance |

## Results template

Copy this table into `reports/results/experiment_log.csv` or a spreadsheet.

| Run ID | Date | Dataset version | Model | Seed | Optimiser | LR | Batch | Epochs | Best val metric | Test metric | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|

## Required plots

- Training and validation loss.
- CER/WER by model.
- Confusion matrix for semantic field classes.
- Optimiser convergence curves.
- Performance by image condition (glare, blur, rotation, low light).
- Confidence/review-rate curve.
- Representative correct and incorrect predictions.

Do not fill the results table with expected or invented values. Add values only after running experiments.
