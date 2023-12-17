import yfinance as yf
import random

class Market:
    def __init__(self, high_risk_returns: dict, medium_risk_returns: dict, low_risk_returns: dict):
        self.__stocks = {}
        self.__high_risk_returns = high_risk_returns
        self.__medium_risk_returns = medium_risk_returns
        self.__low_risk_returns = low_risk_returns
    
    def __str__(self):
        stocks = ""
        for key in self.__stocks:
            stocks += f"name: {key}, price: {self.__stocks[key]['price']}, 50ma: {self.__stocks[key]['50ma']}, 200ma: {self.__stocks[key]['200ma']}\n"
        return stocks

    
    def fill_market(self, stock_tickers: list):
        for ticker in stock_tickers:
            info = yf.Ticker(ticker).info
            self.__stocks[ticker] = {"name": info["shortName"], "price": info["currentPrice"], "50ma": info["fiftyDayAverage"], "200ma": info["twoHundredDayAverage"]}
    
    def add_risk_level(self, risks: list):
        for tuple in risks:
            key, risk = tuple
            self.__stocks[key]["risk"] = risk
    
    def change_prices(self):
        for key in self.__stocks.keys():
            current_price = self.__stocks[key]["price"]
            fiftyMa = self.__stocks[key]["50ma"]
            twohundredMa = self.__stocks[key]["200ma"]

            if self.support(current_price, fiftyMa, twohundredMa):
                if self.__stocks[key]["risk"] == "high":
                    price_change = self.__high_risk_returns[round(random.random() * 500500)]

                if self.__stocks[key]["risk"] == "medium":
                    price_change = self.__medium_risk_returns[round(random.random() * 125500)]

                if self.__stocks[key]["risk"] == "low":
                    price_change = self.__low_risk_returns[round(random.random() * 20200)]
            elif self.resistance(current_price, fiftyMa, twohundredMa):
                if self.__stocks[key]["risk"] == "high":
                    price_change = self.__high_risk_returns[round(random.random() * (-500500))]

                if self.__stocks[key]["risk"] == "medium":
                    price_change = self.__medium_risk_returns[round(random.random() * (-125500))]

                if self.__stocks[key]["risk"] == "low":
                    price_change = self.__low_risk_returns[round(random.random() * (-20200))]
            else:
                if self.__stocks[key]["risk"] == "high":
                    price_change = self.__high_risk_returns[round(random.random() * 1001000 - 500500)]

                if self.__stocks[key]["risk"] == "medium":
                    price_change = self.__medium_risk_returns[round(random.random() * 251000 - 125500)]

                if self.__stocks[key]["risk"] == "low":
                    price_change = self.__low_risk_returns[round(random.random() * 40400 - 20200)]
            
            self.__stocks[key]["price"] = round(current_price + (current_price / 100 * price_change), 2)

    def support(self, price: float, fiftyMA: float, twohundredMa: float):
        if price >= fiftyMA >= twohundredMa and price <= twohundredMa + twohundredMa / 100 * 5 <= fiftyMA + fiftyMA / 100 * 5:
            return random.random() < 0.9 
        if price >= fiftyMA and price <= fiftyMA + fiftyMA / 100 * 5:
            return random.random() < 0.65
        if price >= twohundredMa and price <= twohundredMa + twohundredMa / 100 * 5:
            return random.random() < 0.75
        return False
    
    def resistance(self, price: float, fiftyMA: float, twohundredMa: float):
        if price <= fiftyMA <= twohundredMa and price >= fiftyMA - fiftyMA / 100 * 5 >= twohundredMa - twohundredMa / 100 * 5:
            return random.random() < 0.9 
        if price <= fiftyMA and price >= fiftyMA - fiftyMA / 100 * 5:
            return random.random() < 0.65
        if price <= twohundredMa and price >= twohundredMa - twohundredMa / 100 * 5:
            return random.random() < 0.75
        return False

    def news_price_change(self, ticker: str, price_change_precentage: str):
        current_price = self.__stocks[ticker]["price"]
        price_change = current_price / 100 * int(price_change_precentage.replace("%", ""))
        self.__stocks[ticker]["price"] = round(current_price + price_change, 2)

    def update_average(self):
        for key in self.__stocks.keys():
            price = self.__stocks[key]["price"]
            fiftyMA = self.__stocks[key]["50ma"]
            twohundredMa = self.__stocks[key]["200ma"]
            self.__stocks[key]["50ma"] = round((fiftyMA * 49 + price) / 50, 2)
            self.__stocks[key]["200ma"] = round((twohundredMa * 199 + price) / 200, 2)
    
    def get_stock_price(self, ticker: str):
        return self.__stocks[ticker]["price"]
    
    
    def get_stock_info(self, ticker: str):
        return (self.__stocks[ticker]["price"], self.__stocks[ticker]["50ma"], self.__stocks[ticker]["200ma"])

    
    def get_stocks(self):
        return self.__stocks