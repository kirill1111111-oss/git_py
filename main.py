import logging
logging.basicConfig(level=logging.INFO)

def greet(name: str) -> str:
    logging.info("Вызов функции greet")
    return f"Привет, {name}!"
