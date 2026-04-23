import logging
<<<<<<< HEAD
logging.basicConfig(level=logging.DEBUG)
=======
logging.basicConfig(level=logging.WARNING)
>>>>>>> 07c2be3b4f3b9389eee6da49161b5ea918ffea8c

def greet(name: str) -> str:
    logging.info("Вызов функции greet")
    return f"Привет, {name}!"
