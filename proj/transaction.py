from proj.tasks import transaction
class MyClass:
    queues = [i for i in range(0,2)]
    index = 0

    @classmethod
    def make_transaction(cls):
        print(cls.index)
        i = cls.queues[cls.index]
        transaction.apply_async((i,),queue = f'logic_operation{i}')
        cls.index += 1
        if cls.index >= len(cls.queues):
            cls.index = 0

