
class Account:

    def __init__(self, first, last, balance, record_id=None):

        self.first = first

        self.last = last

        self.balance = balance

        self.record_id = record_id

    def get_name(self):

        return f'{self.first} {self.last}'
