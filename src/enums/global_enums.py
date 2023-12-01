from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status code is not equal to expected."
    WRONG_CONTENT = "Received field content in transaction is not the same as sent"
