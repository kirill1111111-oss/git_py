import logging
logging.basicConfig(level=logging.DEBUG)

def greet(name: str) -> str:
    logging.info("Вызов функции greet")
    return f"Привет, {name}!"
