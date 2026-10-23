import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
logger.info("Model Loaded.")
logger.warning("Some data is missing.")
logger.error("Something went wrong", exc_info=True) #include traceback
