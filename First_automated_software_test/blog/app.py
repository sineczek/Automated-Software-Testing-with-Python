MENU_PROMPT = 'Enter:\n"c" to create a blog\n"r" to read a blog\n"p" to create a post\n"q" to quit\n\nI want to: '
#jak zmienna jest dużymi literami cała to nie powinno się jej zmieniać


blogs = dict()  # new dictionary; Blog_name : Blog_object


def menu():
    # show the user the available blogs
    # Let the user make a choice
    # Do smth with that choice
    # Exit

    print_blogs()
    selection = input(MENU_PROMPT)


def print_blogs():
    # Print available blogs
    for key, blog in blogs.items():  # lista tupli klucz, wartość
        print('- {}'.format(blog))
