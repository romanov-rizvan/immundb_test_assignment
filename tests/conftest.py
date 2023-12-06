import pytest

from src.config import HEADERS, SERVICE_URL, COLLECTION_NAME, COLLECTION_SCHEMA
from src.base_methods import *
from src.enums.global_enums import GlobalErrorMessages


@pytest.fixture(scope="session")
def prepare_collection():
    if not get_collection(SERVICE_URL, HEADERS, COLLECTION_NAME).response_status == 404:
        delete_collection(SERVICE_URL, HEADERS, COLLECTION_NAME)
    resp = create_collection(COLLECTION_SCHEMA, SERVICE_URL, HEADERS, COLLECTION_NAME)
    resp.assert_status_code(200)
    yield
    resp = delete_collection(SERVICE_URL, HEADERS, COLLECTION_NAME)
    resp.assert_status_code(200)
    get_collection(SERVICE_URL, HEADERS, COLLECTION_NAME).assert_status_code(404)


@pytest.fixture(scope="function")
def prepare_constant_transaction():
    resp = create_transaction(SERVICE_URL, get_constant_payload(), HEADERS, COLLECTION_NAME)
    resp.assert_status_code(200)
