from src.config import SERVICE_URL, HEADERS, COLLECTION_NAME
from src.base_methods import *
from src.enums.global_enums import GlobalErrorMessages


def test_put_transaction(prepare_collection):
    docs = get_payload_with_random_an()
    resp = create_transaction(SERVICE_URL, docs, HEADERS, COLLECTION_NAME)
    assert resp.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value


def test_put_several_transactions(prepare_collection):
    docs = get_multiple_transaction_payload(110)
    resp = create_multiple_transactions(SERVICE_URL, docs, HEADERS, COLLECTION_NAME)
    assert resp.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
