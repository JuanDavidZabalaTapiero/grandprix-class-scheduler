import logging

logger = logging.getLogger(__name__)


def handle_integrity_error(e, unique_fields: dict, context: dict = None):
    error_code = e.orig.args[0]

    # === MYSQL DUPLICATE KEY ===
    if error_code == 1062:

        for field, exception in unique_fields.items():
            logger.warning("Duplicate key | field=%s | context=%s", field, context)
            raise exception() from e

    # === UNKNOWN INTEGRITY ERROR ===
    logger.warning("Unexpected IntegrityError | context=%s", context)
    raise e
