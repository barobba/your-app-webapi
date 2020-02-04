
from your_app.models.Account import Account


class AccountDirectory:

    def create(self, first, last, balance) -> Account:

        return Account(first, last, balance, record_id=4)

    def read_list(self) -> list:

        return [
            Account('Kim', 'Brown', 9293120.28, record_id=1),
            Account('John', 'Smith', 340579.71, record_id=2),
            Account('...', '...', 0, record_id=3)
        ]

    def read(self, account_id) -> Account:

        return Account('Some', 'Result', 1234567.89, record_id=account_id)

    def update(self, patch_data: dict):

        pass

    def delete(self):

        pass
