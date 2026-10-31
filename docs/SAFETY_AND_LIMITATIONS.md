# Safety, Reliability and Limitations

ExpiryLens is an information-management aid, not a food-safety testing system.

- It cannot determine microbial contamination, spoilage, tampering or whether a product is safe to consume from a label photograph.
- It must not override manufacturer instructions or official food-safety guidance.
- Preserve the exact printed term (EXP, Use By, Best Before, etc.).
- Best-before and use-by/expiry terminology can have different implications; do not collapse them into one generic field.
- Date formats such as 03/04/2027 can be ambiguous. Ask the user to confirm locale/format rather than guessing.
- A shelf-life duration is not an absolute printed date. Any calculated date must be labelled as estimated and show its calculation basis.
- Opening a package, storage temperature and handling conditions affect product life; do not infer them without reliable user/sensor input.
- A low-confidence or conflicting model output must require human review.
- Keep an audit trail of original image, raw recognised text, parsed interpretation and user correction.
- Avoid storing unnecessary personal data. Protect uploaded images and database credentials.
