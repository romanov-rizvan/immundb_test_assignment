from src.config import SERVICE_URL, HEADERS, COLLECTION_NAME
from src.base_methods import *
from src.schemas.search_document_schema import SEARCH_DOCUMENTS


def test_put_search_and_compare_transaction(prepare_collection):
    doc = get_payload_with_random_an()
    resp = create_transaction(SERVICE_URL, doc, HEADERS, COLLECTION_NAME)
    resp.assert_status_code(200)
    resp = search_transaction_by_account_number(SERVICE_URL, doc, HEADERS, COLLECTION_NAME)
    resp.assert_status_code(200).validate(SEARCH_DOCUMENTS)
    check_searched_document_have_expected_content(doc, resp.response_json)


def test_put_search_and_compare_several_transactions(prepare_collection):
    docs = get_multiple_transaction_payload(110)
    resp = create_multiple_transactions(SERVICE_URL, docs, HEADERS, COLLECTION_NAME)
    resp.assert_status_code(200)
    coll_count = get_collection_count(SERVICE_URL, HEADERS, COLLECTION_NAME)
    for page in range(1, ((coll_count // 100) + 2) if coll_count % 100 != 0 else (coll_count // 100) + 1):
        resp = search_all_transactions_in_page(SERVICE_URL, page, HEADERS, COLLECTION_NAME)
        resp.validate(SEARCH_DOCUMENTS)
    for doc in docs['documents']:
        resp = search_transaction_by_account_number(SERVICE_URL, doc, HEADERS, COLLECTION_NAME)
        check_searched_document_have_expected_content(doc, resp.response_json)

