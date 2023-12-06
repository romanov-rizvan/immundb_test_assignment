SEARCH_DOCUMENTS = {
    "type": "object",
    "properties": {
        "page": {"type": "number"},
        "perPage": {"type": "number"},
        "revisions": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "document": {
                        "type": "object",
                        "properties": {
                            "_id": {"type": "string"},
                            "_vault_md": {
                                "type": "object",
                                "properties": {
                                    "creator": {"type": "string"},
                                    "ts": {"type": "number"}
                                },
                                "required": ["creator", "ts"]
                            },
                            "account_number": {"type": "integer"},
                            "account_name": {"type": "string"},
                            "address": {"type": "string"},
                            "amount": {"type": "integer"},
                            "iban": {"type": "string"},
                            "type": {"type": "string"},
                        },
                        "required": ["_id", "_vault_md", "account_number", "account_name", "address", "amount", "iban", "type"]
                    },
                    "revision": {"type": "string"},
                    "transactionId": {"type": "string"}
                },
                "required": ["document"]
            }
        }
    },
    "required": ["revisions"]
}

# {
#   'page': 1,
#   'perPage': 10,
#   'revisions': [
#     {
#       'document': {
#         '_id': '656ddaa40000000000000222350e5b20',
#         '_vault_md': {
#           'creator': 'a:0ddd7371-cc51-4449-8eea-057943cebd4a',
#           ' ts': 1701698212
#         },
#         'account_name': 'Tracy Dalton',
#         'account_number': 63937,
#         'address': '60482 Bryan Parks, Port Timothyhaven, IA 06625',
#         'amount': 8695,
#         'iban': 'GB70NVRY23418404201657',
#         'type': 'sending'
#       },
#       'revision': '',
#       'transactionId': ''
#     }
#   ],
#   'searchId': ''
# }