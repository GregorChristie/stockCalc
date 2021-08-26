# Stock Calc
# By Gregor Christie

initalStockValue = float(input("Enter intial share price: "))
depositValue = float(input("Enter buy amount in stocks currency: "))
finalStockValue = float(input("Enter the final share price: "))

print((depositValue/initalStockValue)*finalStockValue)
