from src.config import SERVICE_URL, HEADERS, COLLECTION_NAME
from src.base_methods import *
from src.enums.global_enums import GlobalErrorMessages


def test_put_search_and_compare_transaction(prepare_collection):
    doc = get_payload_with_random_an()
    resp = create_transaction(SERVICE_URL, doc, HEADERS, COLLECTION_NAME)
    assert resp.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    resp = search_transaction_by_account_number(SERVICE_URL, doc["account_number"], HEADERS, COLLECTION_NAME)
    assert compare_two_docs(doc, resp.json()["revisions"][0]["document"]), GlobalErrorMessages.WRONG_CONTENT


def test_put_search_and_compare_several_transactions(prepare_collection):
    docs = get_multiple_transaction_payload(110)
    resp = create_multiple_transactions(SERVICE_URL, docs, HEADERS, COLLECTION_NAME)
    assert resp.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    for doc in docs['documents']:
        resp = search_transaction_by_account_number(SERVICE_URL, doc['account_number'], HEADERS, COLLECTION_NAME)
        assert compare_two_docs(doc, resp.json()["revisions"][0]["document"]), GlobalErrorMessages.WRONG_CONTENT

