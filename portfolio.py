class Portfolio:
    def __init__(self, capital: int):
        self.__capital = capital
        self.__holdings = {}
        self.__holdings_current_prices = {}
    
    def __str__(self):
        holdings = ""
        for holding in self.__holdings:
            amount = self.__holdings[holding]["amount"]
            average = self.__holdings[holding]["average"]
            value = self.__holdings[holding]["value"]
            current_price = self.__holdings_current_prices[holding]
            if amount != 0:
                holdings += f"You own {amount} shares of {holding} with average price of {average} for a value of {value}, profit/loss: {round((current_price - average) * amount, 2)} \n"
        return(holdings if len(holdings) != 0 else "You don't own anything")

    def buy(self, ticker: str, amount: int, price: float):
        if amount * price > self.__capital:
            raise ValueError(f"You don't have enough money! You can buy {self.__capital // price} shares")
        if ticker not in self.__holdings.keys():
            self.__holdings[ticker] = {"amount": amount, "value": amount * price, "average": price}
            self.__capital -= amount * price
        else:
            current_amount = self.__holdings[ticker]["amount"]
            current_average = self.__holdings[ticker]["average"]
            new_average = (current_amount * current_average + amount * price) / (current_amount + amount)
            self.__holdings[ticker]["amount"] = current_amount + amount
            self.__holdings[ticker]["value"] = (current_amount + amount) * new_average
            self.__holdings[ticker]["average"] = new_average
            self.__capital -= amount * price

        

    def sell(self, ticker: str, amount: float, price: float):
        if ticker not in self.__holdings.keys():
            raise ValueError("You don't own any shares of this stock")
            return
        
        if self.__holdings[ticker]["amount"] < amount:
            raise ValueError(f"You can't sell more than you own, you own {self.__holdings[ticker]['amount']} {ticker} shares")
            return
        self.__capital += (amount * price)
        self.__holdings[ticker]["amount"] -= amount
        if self.__holdings[ticker]["amount"] == 0:
                self.__holdings[ticker]["value"] = 0
                self.__holdings[ticker]["average"] = 0

    def update_holding_prices(self, holding_prices: dict):
        self.__holdings_current_prices = {}
        for key in holding_prices.keys():
            self.__holdings_current_prices[key] = holding_prices[key]
    
    def get_holdings(self):
        return self.__holdings
    
    def get_marketvalue(self):
        marketvalue = 0
        for key in self.__holdings_current_prices:
            marketvalue += self.__holdings_current_prices[key] * self.__holdings[key]["amount"]
        return round(marketvalue, 2)
    
    def get_capital(self):
        return round(self.__capital, 2)
