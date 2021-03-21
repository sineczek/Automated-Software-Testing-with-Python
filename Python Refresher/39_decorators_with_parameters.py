import functools

user = {"username": "jose", "access_level": "guest"}  # guest nie ma dostępu


def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:  # do tego przekaywanego w dekoratorze make_secure
                return func(*args, **kwargs)
            else:
                print(f"No {access_level} permissions for {user['username']}")

        return secure_function

    return decorator


@make_secure("admin")
def get_admin_password():  # dostęp tylko dla admin
    return "admin: 1234"


@make_secure("user")
def get_dashboard_password():  # dstęp tylko dla users
    return "user: user_password"


print(get_admin_password())
print(get_dashboard_password())

user = {"username": "jose", "access_level": "admin"}

print(get_admin_password())
print(get_dashboard_password())
