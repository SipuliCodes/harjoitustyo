from portfolio import Portfolio
from market import Market
from file import News, Leaderboard
from returns import high_risk_returns, medium_risk_returns, low_risk_returns
import os
import time
import random


stock_tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA', 'META', 'NFLX', 'V', 'JPM', 'GS', 'BA', 'DIS', 'IBM', 'CSCO', 'INTC', 'AMD', 'PYPL', 'NVDA', 'WMT', 'MCD']

stock_risks = [("AAPL", "medium"), ("GOOGL", "low"), ("MSFT", "low"), ("AMZN", "medium"), ("TSLA", "high"), ("META", "medium"), ("NFLX", "high"), ("V", "low"), ("JPM", "medium"), ("GS", "high"), ("BA", "high"), ("DIS", "medium"), ("IBM", "medium"), ("CSCO", "low"), ("INTC", "low"), ("AMD", "high"), ("PYPL", "medium"), ("NVDA", "high"), ("WMT", "low"), ("MCD", "low")
]

def clean():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clean")

def update_holdings():
    holdings = {}
    holdings_keys = portfolio.get_holdings().keys()
    for key in holdings_keys:
        holdings[key] = market.get_stock_price(key)
    portfolio.update_holding_prices(holdings)

guide = """
To buy stocks, write: buy "stock_name" "amount"
To sell stocks, write: sell "stock_name" "amount"
To see stocks, prices and MA:s, write: stocks
To see info of one stock, write: "stock_name"
To see your portfolio, write: portfolio
To see leaderboard, write: leaderboard
To simulate one day forward, write: day
To simulate 7 days forward, write: week
To exit, write: x
"""

portfolio = Portfolio(10000)
market = Market(high_risk_returns, medium_risk_returns, low_risk_returns)
stock_news = News("news.txt")
stock_news.read()
leaderboard = Leaderboard("leaderboard.txt")
leaderboard.read()
leaderboard.initialization()
market.fill_market(stock_tickers)
market.add_risk_level(stock_risks)
clean()
username = input("username: ")
clean()
print(f"Welcome {username} to play this trading game! Try your best to not lose all of your money")

while True:
    update_holdings()
    marketvalue = portfolio.get_marketvalue()
    capital = portfolio.get_capital()
    overall_value = round(marketvalue + capital, 2)
    print()
    print(f"current capital: {portfolio.get_capital()}, marketvalue: {marketvalue}, overall: {overall_value}")
    print(guide)
    command = input("Command: ")
    try:
        order, stock_ticker, amount = command.strip().replace('"', '').split()
    except:
        order = command.strip()

    if order.lower() == "buy":
        try:
            portfolio.buy(stock_ticker.upper(), int(amount), market.get_stock_price(stock_ticker.upper()))
            print(f"Bought {amount} of {stock_ticker.upper()}")
            time.sleep(1)
        except Exception as error:
            print(error)
            time.sleep(3)
            
        clean()
        
    elif order.lower() == "sell":
        try:
            portfolio.sell(stock_ticker.upper(), int(amount), market.get_stock_price(stock_ticker.upper()))
            print(f"Sold {amount} of {stock_ticker.upper()}")
            time.sleep(1)
        except Exception as error:
            print(error)
            time.sleep(3)
        clean()

    elif order.lower() == "stocks":
        clean()
        print(market)

    elif order.lower() == "portfolio":
        clean()
        print(portfolio)
    
    elif order.upper() in market.get_stocks().keys():
        clean()
        price, fiftyMA, twohundredMa = market.get_stock_info(order.upper())
        print(f"name: {order.upper()}, price: {price}, 50ma: {fiftyMA}, 200ma: {twohundredMa}")

    elif order.lower() == "day":
        clean()
        market.change_prices()
        market.update_average()
        print("New day, a new chance to get rich")
        if random.random() < 0.3:
            ticker, news, affect = stock_news.get_news(random.randint(1, 200))
            market.news_price_change(ticker, affect)
            print(news.strip(), affect.strip())
        print()

    elif order.lower() == "week":
        clean()
        for _ in range(7):
            market.change_prices()
            market.update_average()
        print("New week, a new chance to get rich")
        news = ""
        affect = ""
        if random.random() < 0.5:
            ticker, news, affect = stock_news.get_news(random.randint(1, 199))
            market.news_price_change(ticker, affect)
        print(news.strip(), affect.strip())
        print()

    elif command.lower() == "x":
        clean()
        leaderboard.add(username, overall_value)
        leaderboard.add_to_file()
        print("leaderboard")
        print(leaderboard)
        end = input("Press enter to end")
        clean()
        break
    elif command.lower() == "leaderboard":
        clean()
        print("leaderboard")
        print(leaderboard)
    else:
        clean()
        print("Command was faulty")
    


        