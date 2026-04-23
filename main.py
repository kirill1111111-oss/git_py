import logging
logging.basicConfig(level=logging.WARNING)

def greet(name: str) -> str:
    logging.info("Вызов функции greet")
    return f"Привет, {name}!"
