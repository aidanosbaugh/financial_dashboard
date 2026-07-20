import csv

def load_portfolio():
    stocks = []

    with open("portfolio.csv", mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader: 
            stock = {
                "Ticker": row["Ticker"],
                "Price":float(row["Price"]),   
                "Original Price":float(row["Original Price"]),
                "Shares":int(row["Shares"])
            }
            stocks.append(stock)
    return stocks

def save_portfolio(stocks):
    fieldnames = ["Ticker", "Price", "Original Price", "Shares"]
    with open("portfolio.csv", mode="w", newline="", encoding="utf-8") as file:
        saver = csv.DictWriter(file, fieldnames=fieldnames)
        saver.writeheader()
        for stock in stocks:
            saver.writerow(stock)

def value_stock(stock):
    current_value = stock["Price"] * stock["Shares"]
    return current_value

def original_value(stock):
    original_value = stock["Original Price"] * stock["Shares"]
    return original_value

def original_total(stocks):
    original_total_value = 0
    for stock in stocks:
        original_total_value += original_value(stock)
    return original_total_value

def total_value(stocks):
    total_value = 0
    for stock in stocks:
        total_value += value_stock(stock)
    return total_value

def total_profit(stocks):
    total_profit = 0
    for stock in stocks:
        total_profit += profit_stock(stock)
    return total_profit

def profit_stock(stock):
    profit = value_stock(stock) - original_value(stock)
    return profit

def percent_gain(stock):
    percent_gain = profit_stock(stock) / (stock["Original Price"] * stock["Shares"]) * 100 
    return percent_gain

stocks = load_portfolio()