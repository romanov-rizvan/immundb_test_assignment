from src.config import SERVICE_URL, HEADERS, COLLECTION_NAME
from src.base_methods import *
from src.enums.global_enums import GlobalErrorMessages


def test_put_already_exist_transaction(prepare_collection, prepare_constant_transaction):
    docs = get_constant_payload()
    resp = create_transaction(SERVICE_URL, docs, HEADERS, COLLECTION_NAME)
    assert resp.status_code == 409, GlobalErrorMessages.WRONG_STATUS_CODE.value
