import logging
import os

def setup_logger(name: str, log_file: str = None, level: int = logging.DEBUG) -> logging.Logger:
    """Setup and return a logger with console and optional file handlers."""
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent adding duplicate handlers if already configured.
    if not logger.handlers:
        # Console handler
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    
        # File handler if a log file path is provided
        if log_file:
            os.makedirs(os.path.dirname(log_file), exist_ok=True)
            fh = logging.FileHandler(log_file)
            fh.setFormatter(formatter)
            logger.addHandler(fh)
    
    return logger

# Example usage:
# logger = setup_logger(__name__, log_file='./logs/app.log')
