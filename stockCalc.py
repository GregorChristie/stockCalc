# Stock Calc
# By Gregor Christie

import locale
import yfinance as yf

def main():

    tickerName = input("Enter stock symbol: ")

    ticker = yf.Ticker(tickerName)

    tickerInfo = ticker.info

    if(tickerInfo["financialCurrency"]=="USD"):
        locale.setlocale(locale.LC_ALL, 'en_US')
    elif(tickerInfo["financialCurrency"]=="GBP"):
        locale.setlocale(locale.LC_ALL, 'en_GB')
    else:
        locale.setlocale(locale.LC_ALL, 'en_US')

    initalStockValue = float(input("Enter intial share price: "))
    depositValue = float(input("Enter buy amount in stocks currency: "))
    # finalStockValue = float(input("Enter the final share price: "))
    finalStockValue = ticker.info["currentPrice"]
    print("The current stock value is %s" % (locale.currency(finalStockValue)))
    
    finalBalance = (depositValue/initalStockValue)*finalStockValue
    print(locale.currency(finalBalance))

if __name__ == "__main__":
    main()