# Solo Project Roadmap

This plan is deliberately scoped for one student. Work in vertical slices and keep a working demonstration at every milestone.

## Milestone 1 — Foundations
- Create the Python environment and install dependencies.
- Start FastAPI and React.
- Finalise annotation schema and date taxonomy.
- Create a project diary and Git repository.
**Deliverable:** app shell, health endpoint, documented dataset format.

## Milestone 2 — Pilot dataset
- Photograph a varied but manageable set of products.
- Capture front/back/side views where dates are printed.
- Annotate date regions and exact text.
- Review labels and group samples by physical package.
**Deliverable:** small versioned pilot dataset and annotation guide.

## Milestone 3 — Baselines
- Build image quality checks and preprocessing.
- Implement deterministic date parser with ambiguity handling.
- Benchmark a baseline OCR method.
- Build an MLP semantic classifier on annotated examples.
**Deliverable:** baseline metrics and error analysis.

## Milestone 4 — Deep Learning core
- Train CNN-based text recognition baseline.
- Add BiLSTM sequence modelling.
- Evaluate CTC decoding.
- Add attention only after a stable baseline exists.
**Deliverable:** reproducible trained model and comparison.

## Milestone 5 — Syllabus experiments
- Denoising autoencoder.
- Optimiser comparison.
- Regularisation and early stopping.
- RNN/LSTM/GRU comparison.
- PCA/SVD notebooks.
**Deliverable:** plots, result tables and explanations.

## Milestone 6 — Product application
- Connect inference endpoint.
- Build scan review screen.
- Build inventory CRUD and expiry dashboard.
- Add reminders and export if time permits.
**Deliverable:** end-to-end demo.

## Milestone 7 — Evaluation and submission
- Freeze test set.
- Run final evaluation.
- Analyse errors and limitations.
- Prepare report, slides and demo script.
**Deliverable:** defensible final-year/semester project submission.

## Solo prioritisation

Must-have: image capture/upload, date-region recognition, semantic date type, ambiguity handling, user confirmation, inventory record, evaluation.

Should-have: denoising experiment, CNN-BiLSTM comparison, optimiser comparison, reminders, dashboard.

Stretch: attention decoder, multiple product views, barcode enrichment, multi-user retail mode, consumption prediction.
