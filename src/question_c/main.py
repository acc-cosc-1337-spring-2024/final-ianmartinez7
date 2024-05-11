#add import

from question_c import Stock

def main():
    # all the stonk
    stock_aapl = Stock("AAPL", "Apple Inc")
    stock_cat = Stock("CAT", "Caterpillar")
    stock_ek = Stock("EK", "Eastman Kodak")
    stock_goog = Stock("GOOG", "Google")
    stock_msft = Stock("MSFT", "Microsoft")

  # list made
    stocks = [stock_aapl, stock_cat, stock_ek, stock_goog, stock_msft]

 #format for each stonk
    for stock in stocks:
        print(f"Company Symbol: {stock.get_symbol()}")
        print(f"Company Name: {stock.get_company_name()}")
        print("----------------------------")

if __name__ == "__main__":
    main()
