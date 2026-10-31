# API Contract (Initial)

Base path: `/api/v1`

## Health
`GET /health`
Returns service status.

## Analyse product image
`POST /scan`
- Content type: `multipart/form-data`
- Field: `file` (JPEG, PNG or WEBP; configurable size limit)
- Initial scaffold response: upload accepted and analysis not yet implemented.
- Future response should include image ID, detected regions, raw text, semantic date fields, parse status, confidence/review flag.

## Inventory
Planned endpoints:
- `GET /inventory` — list products
- `POST /inventory` — create a user-confirmed product record
- `GET /inventory/{product_id}` — retrieve one record
- `PATCH /inventory/{product_id}` — correct fields/quantity/location
- `DELETE /inventory/{product_id}` — remove record
- `GET /inventory/expiring?within_days=7` — filter by date policy

## Scan response design (future)

```json
{
  "scan_id": "server-generated-id",
  "status": "needs_review",
  "product": {
    "name": null,
    "category": "food"
  },
  "date_fields": [
    {
      "raw_text": "EXP 12/02/27",
      "semantic_type": "EXP",
      "parsed_date": null,
      "parse_status": "ambiguous",
      "confidence": null,
      "verification_status": "pending"
    }
  ],
  "warnings": ["Date format requires confirmation."]
}
```

The example is a contract illustration, not a prediction output. The date remains unresolved until locale/format is known.
