import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        pos_args = args if args else "none"
        kw_args = kwargs if kwargs else "none"

        result = func(*args, **kwargs)

        log_message = (
            f"function: {func.__name__} | "
            f"positional parameters: {pos_args} | "
            f"keyword parameters: {kw_args} | "
            f"return: {result}"
        )
        logger.info(log_message)

        return result
    return wrapper

@logger_decorator
def say_hello():
    print("Hello, World!")

@logger_decorator
def check_numbers(*args):
    return True

@logger_decorator
def return_logger(**kwargs):
    return logger_decorator

if __name__ == "__main__":
    say_hello()
    check_numbers(10, 20, 30)
    return_logger(a=1, b=2)