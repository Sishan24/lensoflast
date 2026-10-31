# Project Blueprint

## 1. Problem statement

Packaged consumer products display date and batch information in inconsistent layouts, formats, fonts and print quality. People often need to inspect each item manually and may overlook products in storage. ExpiryLens aims to convert product-label photographs into verified, structured inventory records and provide expiry-aware monitoring.

## 2. Aim

To design and evaluate a Deep Learning-based system that detects and recognises date-related information on packaged product labels, interprets the semantic role of each field, and supports digital inventory and lifecycle tracking.

## 3. Objectives

- Build a labelled image dataset of real product packages and date regions.
- Preprocess photographs under varied lighting, orientation, blur and perspective.
- Develop and evaluate a CNN-based visual feature extractor.
- Explore sequence recognition using BiLSTM with CTC or an attention-based decoder.
- Classify extracted text into semantic categories such as MFD, EXP, Best Before and Use By.
- Validate date strings and preserve uncertainty for human review.
- Store product records and provide expiry-aware inventory views.
- Compare optimisers, regularisation methods and model variants using reproducible experiments.

## 4. Scope

### Included in the first version
- Single product image upload/capture.
- Product-label/date-region processing.
- Recognition of printed date text and nearby date keywords.
- Date type classification.
- User confirmation/editing of uncertain fields.
- Inventory record creation and expiry dashboard.
- Basic reminders/near-expiry filters.

### Stretch goals
- Batch scanning and multiple products per session.
- Barcode-assisted product metadata enrichment.
- Multi-user household/store profiles.
- Consumption trend estimates from user-entered usage history.
- Retail batch-level inventory and CSV export.

### Out of scope for the first version
- Guaranteeing food safety or edibility.
- Predicting microbiological spoilage from a package photograph.
- Inferring storage temperature or whether a package has been opened without user/sensor input.
- Automatically making disposal or consumption decisions.
- Universal support for every language, package type or handwritten label.

## 5. Users and use cases

- Household: register pantry/fridge products and receive reminders.
- Hostel/cafeteria: maintain a shared inventory and review upcoming dates.
- Small retailer: record package/batch dates and identify stock requiring attention.

## 6. Success criteria

A successful academic prototype should:
- Work end-to-end on a documented test set of unseen product packages.
- Report date text recognition and semantic classification separately.
- Flag low-confidence or contradictory outputs.
- Store the original image reference and user-corrected ground truth.
- Include baseline comparisons, ablation experiments and error analysis.
- Avoid claims that exceed measured results.
