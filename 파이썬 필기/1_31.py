def ko_hello(name):
    print(f"안녕하세요, {name}님!")


def en_hello(name):
    print(f"Hello, {name}!")


def add_emoji(name, func):
    func(name)
    print('^~^//')


# add_emoji('동훈', ko_hello)
# ko_hello('동훈')
# en_hello('동훈')

###################################################

def emoji_decorator(func):
    def wrapper(name):
        func(name)
        print('^~^//')

    return wrapper

# new_func = emoji_decorator(ko_hello)
# new_func('동훈')
emoji_decorator(ko_hello)('동훈')
emoji_decorator(en_hello)('donghoon')

@emoji_decorator
def ko_hello(name):
    print(f"안녕하세요, {name}님!")

ko_hello('동훈')


class MyClass:

    def method(self):
        return 'instance method', self

    @classmethod
    def classmethod(cls):
        return 'class method', cls
    
    @staticmethod
    def staticmethod():
        return 'static method'

my_class = MyClass()
print(my_class.method())
# print(my_class.)