import collections
from datetime import datetime


class TransactionalPolicy(collections.UserDict):
    """잘못된 상속의 예시"""

    def change_in_policy(self, customer_id, **new_policy_data):
        self[customer_id].update(**new_policy_data)


policy = TransactionalPolicy({
    "client001": {
        "fee": 1000.0,
        "expiration_date": datetime(2020, 1, 3),
    }
})

print(policy["client001"])

policy.change_in_policy("client001", expiration_date=datetime(2020, 1, 4))
print(policy["client001"])

dir(policy)


class TransactionPolicy:
    """컴포지션을 사용한 리팩토링 예제"""

    def __init__(self, policy_data, **extra_data):
        self._data = {**policy_data, **extra_data}

    def change_in_policy(self, customer_id, **new_policy_data):
        self._data[customer_id].update(**new_policy_data)

    def __getitem__(self, customer_id):
        return self._data[customer_id]

    def __len__(self):
        return len(self._data)
