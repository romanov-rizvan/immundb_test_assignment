import json
import requests
from faker import Faker
from random import sample

fake = Faker()


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
    return requests.put(url=url + f"{collection}", json=json_doc, headers=headers, verify=True)


def delete_collection(url, headers, collection):
    return requests.delete(url=url + f"{collection}", headers=headers, verify=True)


def get_collection(url, headers, collection):
    return requests.get(url=url + f"{collection}", headers=headers, verify=True)


def get_collections(headers):
    url = "https://vault.immudb.io/ics/api/v1/ledger/default/collections"
    return requests.get(url=url, headers=headers, verify=True)


def create_transaction(url, json_doc, headers, collection):
    return requests.put(url + f"{collection}/document", json=json_doc, headers=headers, verify=True)


def create_multiple_transactions(url, json_doc, headers, collection):
    return requests.put(url + f"{collection}/documents", json=json_doc, headers=headers, verify=True)
