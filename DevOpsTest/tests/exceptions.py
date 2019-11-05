class MyError(Exception):
    # Customise an exception; Inherit Exception

    def __init__(self, age):
        self.age = age

    def __str__(self):
        # __str__ for returning the description
        return f'age cannot be an negative number, your input is {self.age}'


def example():
    age = int(input('Please enter your age:'))
    try:
        if age < 0:
            raise MyError(age)  # raise exception
    except MyError as exp:
        print(f"Found exception: {exp}")


def try_catch():
    try:
        print("May cause exceptions")
    except (IOError, NameError) as e:
        print(f"deal with specific exceptions {e}")
    except Exception as e:
        print(f"deal with exceptions {e}")
    else:
        print("Did not catch exceptions")
    finally:
        print("No matter what, execute this")


if __name__ == '__main__':
    try_catch()
    example()
