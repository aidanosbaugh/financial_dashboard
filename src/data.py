import yfinance as yf


def get_history(ticker, selected_period):
    stock = yf.Ticker(ticker)
    return stock.history(period=selected_period)


def get_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        return stock.fast_info["lastPrice"]

    except Exception:
        return None


def update_prices(stocks):

    updated_stocks = []

    for stock in stocks:

        price = get_price(stock["Ticker"])

        if price is None:
            continue

        stock["Price"] = price
        updated_stocks.append(stock)

    return updated_stocks