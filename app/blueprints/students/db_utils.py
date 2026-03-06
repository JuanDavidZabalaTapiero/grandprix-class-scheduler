import logging

from .exceptions import (
    StudentDocumentAlreadyExists,
    StudentError,
)

logger = logging.getLogger(__name__)


def handle_student_integrity_error(e, document_id: str):
    error_code = e.orig.args[0]

    # ERROR: DUPLICATE KEY
    if error_code == 1062:
        logger.warning("Duplicate student attempt | document_id=%s", document_id)

        raise StudentDocumentAlreadyExists() from e

    # ERROR: UNKNOWN INTEGRITY ERROR
    logger.exception(
        "Unexpected IntegrityError | document_id=%s",
        document_id,
    )

    raise StudentError() from e
