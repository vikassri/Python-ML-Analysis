class Account:
    counter = 0

    def __init__(self,  name, balance, credit_limit=1500):
        Account.counter += 1
        self.customer = name
        self.balance = balance
        self.credit_limit = credit_limit

    def __del__(self):
        Account.counter -= 1
        self.customer = "Not Found"
        self.balance = 0

    def withdrawn(self, amount):
        if self.balance - amount < -self.credit_limit :
            print("Insufficient Amount !!!")
            return False
        else :
            self.balance -= amount
            return True

    def deposit(self, amount):
        self.balance += amount
        return True

    def transfer(self, target, amount):
        if self.balance - amount < -self.credit_limit:
            print("Insufficient Amount !!!")
            return False
        else :
            self.balance -= amount
            target.balance += amount
            return True

    def balance(self):
        return self.balance


if __name__ == '__main__':
    vikas = Account("vikas", 100000)
    satish = Account("Satish", 120000)
    print("Vikas's Balance : %i" % (vikas.balance))
    print("Satish's Balance : %i" % (satish.balance))
    print("Vikas Transfer 10000 to Satish : %s" % (vikas.transfer(satish,10000)))
    print("Vikas's Balance : %i" % (vikas.balance))
    print("Satish's Balance : %i" % (satish.balance))
    print("Vikas withdraw 15000 : %s" % (vikas.withdrawn(15000)))
    print("Satish deposit 5000 : %s" % (satish.deposit(5000)))
    print("Vikas's Balance : %i" % (vikas.balance))
    print("Satish's Balance : %i" % (satish.balance))