stock_prices={
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "MSFT": 300
}
tot= 0
n=int(input("ENter number of stocks:"))
for i in range(n):
    stock=input("Enter stock name: ").upper()
    quantity=int(input("Enter quantity: "))
    if stock in stock_prices:
        cost= stock_prices[stock]*quantity
        tot=tot+cost
        print("cost of", stock,"=",cost)
    else:
        print("Stock not found")
print("\nTotal Investment Value = ",tot)

file = open("portfolio.txt", "w")
file.write("Total Investment Value = "+str(tot))
file.close()

print("Result saved in portfolio.txt")