import logging

logger = logging.getLogger(__name__)


def handle_integrity_error(
    e, unique_fields: dict = None, fk_fields: dict = None, context: dict = None
):
    error_code = e.orig.args[0]

    # === DUPLICATE KEY (UNIQUE) ===
    if error_code == 1062:
        for field, exception in unique_fields.items():
            logger.warning("Duplicate key | field=%s | context=%s", field, context)
            raise exception() from e

    # === FOREIGN KEY (DELETE / UPDATE RESTRICT) ===
    if error_code in (1451, 1452) and fk_fields:
        for field, exception in fk_fields.items():
            logger.warning("FK constraint | field=%s | context=%s", field, context)
            raise exception() from e

    # === UNKNOWN INTEGRITY ERROR ===
    logger.warning("Unexpected IntegrityError | context=%s", context)
    raise e
