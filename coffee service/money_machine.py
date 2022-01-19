class MoneyMachine:

    COIN_VALUES = {'quaters: ':0.25,
                   'dimes: ':0.10,
                   'nickles: ':0.05,
                   'pennies: ':0.01}

    SYMBOL = '$'

    def __init__(self):
        self.profit = 0
        self.money_recevied = 0

    def report(self):
        print(f'Money{self.SYMBOL}{self.profit}')

    def process_coins(self):
        '''Returns the total calculated from coins inserted'''
        print('Please insert coins')
        for coin in self.COIN_VALUES:
            self.money_recevied += int(input(f'How many {coin}'))*self.COIN_VALUES[coin]
        
        return self.money_recevied

    def make_payment(self,cost):
        '''Retunr True when payment is accepted, or Flase if insufficient'''
        self.process_coins()
        if self.money_recevied >= cost:
            change = round(self.money_recevied - cost,2)
            print(f'Here is {self.SYMBOL} {change} in change')
            self.profit += cost
            self.money_recevied = 0

            return True
        
        else:
            print("Sorry, that's not enough money. Money refunded.")
            self.money_recevied = 0
            return False

