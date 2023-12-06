import json
import requests
from faker import Faker
from random import sample
from jsonschema import validate

from src.enums.global_enums import GlobalErrorMessages

fake = Faker()


class Response:
    def __init__(self, response):
        self.response = response
        self.response_status = response.status_code
        try:
            self.response_json = response.json()
        except:
            pass

    def validate(self, schema):
        validate(self.response_json, schema)
        return self

    def assert_status_code(self, status_code: int):
        assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value + str(self.response_status)
        return self


def get_random_type(trans_type):
    if trans_type:
        return "sending"
    else:
        return "receiving"


def get_payload(account_number):
    payload = {
        "account_number": account_number,
        "account_name": fake.name(),
        "iban": fake.iban(),
        "address": fake.address().replace("\n", ", "),
        "amount": fake.pyint(0, 9999),
        "type": get_random_type(fake.pybool())
    }
    return payload


def get_payload_with_random_an():
    return get_payload(fake.pyint(10000, 99999))


def get_multiple_transaction_payload(count):
    lst = sample(range(10000, 99999 + 1), count)
    with open('src/schemas/multiple_payload.json') as f:
        payload = json.load(f)
        for item in lst:
            new_payload = get_payload(item)
            payload["documents"].append(new_payload)
        return payload


def get_constant_payload():
    with open("src/schemas/constant_payload.json") as f:
        payload = json.load(f)
    return payload


def create_collection(json_doc, url, headers, collection):
    return Response(requests.put(url=url + f"{collection}", json=json_doc, headers=headers, verify=True))


def delete_collection(url, headers, collection):
    return Response(requests.delete(url=url + f"{collection}", headers=headers, verify=True))


def get_collection(url, headers, collection):
    return Response(requests.get(url=url + f"{collection}", headers=headers, verify=True))


def get_collections(headers):
    url = "https://vault.immudb.io/ics/api/v1/ledger/default/collections"
    return Response(requests.get(url=url, headers=headers, verify=True))


def create_transaction(url, json_doc, headers, collection):
    return Response(requests.put(url + f"{collection}/document", json=json_doc, headers=headers, verify=True))


def create_multiple_transactions(url, json_doc, headers, collection):
    return Response(requests.put(url + f"{collection}/documents", json=json_doc, headers=headers, verify=True))


def search_transaction_by_account_number(url, doc, headers, collection):
    json_doc = {
        "query": {
            "expressions": [{
                "fieldComparisons": [{
                    "field": "account_number",
                    "operator": "EQ",
                    "value": doc["account_number"]
                }]
            }]
        },
        "page": 1,
        "perPage": 10
    }
    return Response(requests.post(url + f"{collection}/documents/search", json=json_doc, headers=headers, verify=True))


def search_all_transactions_in_page(url, page, headers, collection):
    json_doc = {
        "query": {
            "expressions": [{
                "fieldComparisons": [{
                    "field": "account_number",
                    "operator": "GT",
                    "value": 0
                }]
            }]
        },
        "page": page,
        "perPage": 100
    }
    return Response(requests.post(url + f"{collection}/documents/search", json=json_doc, headers=headers, verify=True))


def get_collection_count(url, headers, collection):
    json_doc = {
        "query": {
            "expressions": [{
                "fieldComparisons": [{
                    "field": "account_number",
                    "operator": "GT",
                    "value": 0
                }]
            }],
            "limit": 0
        }
    }
    return requests.post(url + f"{collection}/documents/count", json=json_doc, headers=headers, verify=True).json()[
        'count']


def compare_two_docs(first_doc, second_doc):
    """
    Checks that all fields and values of the first_doc are included in the second_doc.
    Return True if all fields and their values from first_doc contains in second_doc,
    otherwise return False
    """
    shared_items = {k: first_doc[k] for k in first_doc if k in second_doc and first_doc[k] == second_doc[k]}
    return len(shared_items) == len(first_doc)


def check_searched_document_have_expected_content(expected_content, searched_document):
    assert compare_two_docs(expected_content, searched_document["revisions"][0]["document"]), (
        GlobalErrorMessages.WRONG_CONTENT)
