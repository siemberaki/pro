class donation:
    def __init__(self, amount):
        self.amount = amount

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        if amount < 10:
            self.__amount = 10
        elif amount > 1000000:
            self.__amount = 1000000
        else:
            self.__amount = amount


charity = donation(5)
charity.amount