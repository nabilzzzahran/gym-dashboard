import logging


def predict(features: dict) -> float:
    try:
        value = model.predict(features)
    except KeyError as e:
        logger.error(f"Missing feature: {e}")
        raise ValueError(f"Invalid input: {e}")
    except Exception as e:
        logger.error("Unexpected error", exc_info=True)
        raise
    return value