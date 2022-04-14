from sys import exit
from matplotlib.pyplot import subplots, show
import yfinance as yf
yf.pdr_override()


def getTicker():
    ticker = input("Enter your Ticker: ")
    data = yf.Ticker(ticker)
    if not data.options:
        exit("Invalid Ticker")
    return ticker, data


def getDate(dates):
    for date in dates:
        print(date)
    date = input("Enter your Expiration Date: ")
    if date not in dates:
        exit("Invalid Date")
    return date


def main():
    ticker, data = getTicker()
    dates = data.options
    strikeDate = getDate(dates)
    optionData = data.option_chain(strikeDate)
    callsData = optionData.calls
    putsData = optionData.puts

    # plot IV skew via matplotlib
    fig, axs = subplots(2)
    fig.suptitle(f"Volatility Skew for {ticker} {strikeDate}")
    axs[0].plot(callsData["strike"], callsData["impliedVolatility"]*100)
    axs[0].set_title("IV on calls")
    axs[1].plot(putsData["strike"], putsData["impliedVolatility"]*100)
    axs[1].set_title("IV on puts")
    show()


if __name__ == '__main__':
    main()
