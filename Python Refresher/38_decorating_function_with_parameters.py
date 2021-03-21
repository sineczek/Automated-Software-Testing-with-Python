import functools

user = {"username": "jose", "access_level": "guest"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args,
                        **kwargs):  # dzięki temu będzie można używać make_secure z innymi funkcjami jako dekorator, nie tylko get_password
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            print(f"No admin permissions for {user['username']}")

    return secure_function


@make_secure
def get_password(panel):  # dekorator panel'i
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"


print(get_password("billing"))
print(get_password.__name__)
