# Model and Training Plan

## 1. Proposed system architecture

A modular pipeline is recommended so that each stage can be trained and evaluated independently.

1. Input and quality checks: image decoding, size checks, blur/glare warnings.
2. Preprocessing: orientation correction where possible, resize, normalisation and optional denoising.
3. Text/date-region detection: identify candidate label regions. Begin with annotated crops and a simple baseline; add a trained detector if the dataset supports it.
4. Visual encoder: CNN extracts spatial features from the candidate crop.
5. Sequence model: BiLSTM models left-to-right and right-to-left character context.
6. Decoder: CTC is a practical baseline for unaligned text; attention-based encoder-decoder is a comparison/extension.
7. Semantic classifier: MLP predicts MFD, EXP, BEST_BEFORE, USE_BY, SHELF_LIFE, BATCH_CODE or UNKNOWN using recognized text and context features.
8. Date parser/validator: deterministic rules parse only unambiguous values; return ambiguity instead of guessing.
9. Human review: user confirms/corrects low-confidence or conflicting output.
10. Inventory service: store accepted values and calculate reminder windows.

## 2. Recommended model progression

### Baseline A: deterministic baseline
- Manually crop date regions or use a simple region proposal.
- Use a baseline OCR engine only as a benchmark if permitted.
- Add strict date parsing and semantic keyword rules.
- Record its failure modes. This baseline is not the project's final DL contribution.

### Baseline B: CNN + CTC
- Input: cropped date/label image.
- CNN: visual feature maps.
- Sequence projection: map feature columns to time steps.
- CTC loss: train without character-level alignment.
- Output: character sequence.

### Proposed model C: CNN + BiLSTM + CTC
- CNN visual feature extractor.
- BiLSTM sequence context.
- Linear character classifier.
- CTC loss and greedy/beam decoding.
- Compare against Baseline B.

### Extension D: attention-based recognition
- Add attention decoder if data and time permit.
- Compare CER/WER and error types against CTC.

### Semantic field classifier
- Input features: recognised text tokens/characters, nearby keyword context and optional crop-level visual features.
- Output: semantic date-field category.
- Start with an MLP on a small engineered feature vector; then consider learned text/visual embeddings.

### Denoising autoencoder
- Train on clean label crops with synthetically corrupted inputs.
- Reconstruct the clean crop.
- Compare recognition performance on clean and degraded images before/after denoising.

## 3. Training discipline

- Split by package identity, not random image alone.
- Fix and record random seeds.
- Track train and validation loss/metrics.
- Use early stopping based on validation metric.
- Save best model checkpoint and training configuration.
- Never tune against the final test set.
- Report multiple runs or confidence intervals if feasible.
- Preserve a reproducible experiment log.

## 4. Metrics

Recognition:
- Character Error Rate (CER)
- Word Error Rate (WER)
- Exact date-string accuracy

Semantic interpretation:
- Accuracy, macro precision, macro recall, macro F1
- Confusion matrix, especially EXP vs MFD vs batch code

End-to-end:
- Exact date + correct semantic type accuracy
- Percentage sent to human review
- False accepted-date rate
- Average inference latency

Denoising:
- PSNR/SSIM may be reported, but recognition improvement is more relevant to the application.

## 5. Confidence and abstention

Do not rely on a raw neural-network score as a calibrated probability without calibration testing. Define a review policy using validation data. Low-confidence, invalid, conflicting or ambiguous dates must be sent to user confirmation. The application should retain original text and corrected text for audit.
