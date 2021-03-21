import functools

user = {"username": "jose", "access_level": "guest"}


def make_secure(func):
    @functools.wraps(
        func)  # dekorator zatrzymuje nazwę i dokumentację, nawet jak później zostaje zmieniona "nazwa funkcji" przez make_secure
    def secure_function():
        if user["access_level"] == "admin":
            return func
        else:
            print(f"No admin permissions for {user['username']}")

    return secure_function


@make_secure
def get_admin_password():
    return "1234"


print(get_admin_password())
print(get_admin_password.__name__)  # dzięki functools.wraper zwraca get_admin_passowrd anie make_secure
