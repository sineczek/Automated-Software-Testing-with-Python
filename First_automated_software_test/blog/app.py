blogs = dict()  # new dictionary; Blog_name : Blog_object


def menu():
    # show the user the available blogs
    # Let the user make a choice
    # Do smth with that choice
    # Exit

    print_blogs()


def print_blogs():
    # Print available blogs
    for key, blog in blogs.items():  # lista tupli klucz, wartość
        print('- {}'.format(blog))
