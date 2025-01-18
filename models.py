# Defines models for transactions and budgets

class Transaction:
    def __init__(self, user_id, amount, category, date, type):
        self.user_id = user_id
        self.amount = amount
        self.category = category
        self.date = date
        self.type = type

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "type": self.type,
        }
    