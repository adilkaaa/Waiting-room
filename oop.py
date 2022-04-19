class Waiter:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        Waiter.__instance = None

    def __init__(self, name):
        self.name = name

    def service(self):
        print('Обслуживание с ', self.name)

a1 = Waiter('#1')
print(a1.__dict__)
a1.service()
print(id(a1))
print()

a2 = Waiter('#2')
print(a2.__dict__)
a2.service()
print(id(a2))
print()

a3 = Waiter('#3')
print(a3.__dict__)
a3.service()
print(id(a3))
print()

## Checking
## print(a1.__dict__)
## a1.service()

