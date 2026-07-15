import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def setup_logging(app):
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    log_file = (log_dir / "clinic_app.log").resolve()

    for handler in app.logger.handlers:
        if isinstance(handler, RotatingFileHandler):
            existing_file = Path(handler.baseFilename).resolve()

            if existing_file == log_file:
                return

    file_handler = RotatingFileHandler(
        filename=str(log_file),
        maxBytes=1_000_000,
        backupCount=5,
        encoding="utf-8"
    )

    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler.setFormatter(formatter)

    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.propagate = False

    app.logger.info("Clinic Management System logging initialized.")