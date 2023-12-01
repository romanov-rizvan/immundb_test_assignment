from src.config import SERVICE_URL, HEADERS, COLLECTION_NAME
from src.base_methods import *
from src.enums.global_enums import GlobalErrorMessages


def test_put_already_exist_transaction(prepare_collection, prepare_constant_transaction):
    doc = get_constant_payload()
    resp = create_transaction(SERVICE_URL, doc, HEADERS, COLLECTION_NAME)
    assert resp.status_code == 409, GlobalErrorMessages.WRONG_STATUS_CODE.value
    resp = search_transaction_by_account_number(SERVICE_URL, doc["account_number"], HEADERS, COLLECTION_NAME)
    assert doc["account_number"] == resp.json()["revisions"][0]["document"]["account_number"], (
        GlobalErrorMessages.WRONG_CONTENT)

