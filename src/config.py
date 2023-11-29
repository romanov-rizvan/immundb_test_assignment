HEADERS = {
        'accept': 'application/json',
        'X-API-Key': "default.PxqtMGGgJrTYRLlNx--IdA.K-9bXoR5--QcuhVQ6etbUxkuC0fsw1xJyGJOWPZpeG6fsy15",
        'Content-Type': 'application/json'
    }
SERVICE_URL = "https://vault.immudb.io/ics/api/v1/ledger/default/collection/"
COLLECTION_NAME = "Transactions"
COLLECTION_SCHEMA = {
    "fields": [
        {
            "name": "account_number",
            "type": "INTEGER"
        },
        {
            "name": "account_name",
            "type": "STRING"
        },
        {
            "name": "iban",
            "type": "STRING"
        },
        {
            "name": "address",
            "type": "STRING"
        },
        {
            "name": "amount",
            "type": "INTEGER"
        },
        {
            "name": "type",
            "type": "STRING"
        }
    ],
    "idFieldName": "_id",
    "indexes": [
        {
            "fields": ["account_number"],
            "isUnique": True
        }
    ]
}