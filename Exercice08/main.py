def log_decorator(wrapped_function: callable) -> callable:
    """
    A decorator that logs messages before and after the execution of a wrapped
    function. The wrapped function must not have any arguments.

    Args:
        wrapped_function: The function to be decorated. It must be callable and
            cannot have any parameters.

    Raises:
        TypeError: If `wrapped_function` is not callable or if it contains any
            parameters.

    Returns:
        callable: A wrapper function that logs messages before and after
            executing the `wrapped_function`.
    """

    if not callable(wrapped_function):
        raise TypeError("The wrapped function must be callable.")

    # checks if wrapped_function has args in is definition, not when it is called
    # signature = inspect.signature(wrapped_function)
    # if len(signature.parameters) > 0:
    #     raise TypeError("The wrapped function must not have any arguments.")

    def wrapper(*args, **kwargs):
        if args or kwargs:
            raise TypeError("The wrapped function must not have any arguments.")
        print("--- Message before wrapped function ---")
        result = wrapped_function()
        print("--- Message after wrapped function ---")
        return result

    return wrapper


if __name__ == "__main__":
    try:
        # @log_decorator
        # def function_test():
        #     print("Cette fonction ne prend pas d'arguments.")

        # function_test()

        @log_decorator
        def function_test(arg: str):
            print(f"Cette fonction prend un argument: {arg}")

        function_test("test")

    except TypeError as error:
        print("An error happened:")
        print(error)
