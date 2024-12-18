from stock import Stock
from yahoo_fin import stock_info
import yfinance as yf
import warnings
warnings.filterwarnings("ignore")

portfolio =[]

def addStock(name,ticker,sector,numOfShares):
    price = round(float(stock_info.get_live_price(ticker)),2)
    newStock = Stock(name,ticker,sector,price,numOfShares)
    portfolio.append(newStock)

def updatePrice():
    for stock in portfolio:
        price = stock_info.get_live_price(stock.ticker)

def viewPortfolio():
    print("{0:20s}{1:10s}{2:35s}{3:14s}{4:6s}{5:10s}".format("Name of Stock","Ticker","Industry","Price","QTY","Gain/Loss"))
    count =1
    for stock in portfolio:
        print(f"{count}. {stock.name:{17}}{stock.ticker:{10}}{stock.sector:{25}}{stock.currentPrice:{8}}{stock.numOfShares:{6}}")
        count+=1

for i in range(5):
    name =input("Enter the Name of the Stock: ")
    ticker = input("Enter the stock ticker name: ")
    tick = yf.Ticker(ticker).info
    sector=tick['industry']
    numOfShares= int(input("Enter number of stock shares to buy: "))
    addStock(name,ticker,sector,numOfShares)
viewPortfolio()