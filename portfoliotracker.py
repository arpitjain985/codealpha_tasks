def stock_portfolio_tracker():
    
    stock_prices = {
        "AAPL": 180.50,
        "TSLA": 250.75,
        "MSFT": 300.25,
        "AMZN": 120.40,
        "GOOGL": 135.60
    }
    print(stock_prices)
    portfolio = {}
    total_value = 0.01
    
    print("Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    
    while True:
        print("\n1. Add stock to portfolio")
        print("2. View portfolio")
        print("3. Calculate total investment")
        print("4. Save portfolio to file")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            ticker = input("Enter stock ticker: ").upper()
            if ticker not in stock_prices:
                print("Invalid stock ticker. Available stocks:", ", ".join(stock_prices.keys()))
                continue
                
            try:
                quantity = int(input(f"Enter quantity of {ticker} shares: "))
                if quantity <= 0:
                    print("Quantity must be positive.")
                    continue
                    
                portfolio[ticker] = portfolio.get(ticker, 0) + quantity
                print(f"Added {quantity} shares of {ticker} to portfolio.")
                
            except ValueError:
                print("Please enter a valid number for quantity.")
                
        elif choice == "2":
            if not portfolio:
                print("Portfolio is empty.")
            else:
                print("\nCurrent Portfolio:")
                for ticker, quantity in portfolio.items():
                    print(f"{ticker}: {quantity} shares")
                    
        elif choice == "3":
            total_value = sum(quantity * stock_prices[ticker] 
                           for ticker, quantity in portfolio.items())
            print(f"\nTotal Portfolio Value: ${total_value:.2f}")
            
        elif choice == "4":
            if not portfolio:
                print("Portfolio is empty. Nothing to save.")
                continue
                
            filename = input("Enter filename to save (e.g., portfolio.txt): ")
            try:
                with open(filename, 'w') as f:
                    f.write("Stock Portfolio\n")
                    f.write("===============\n")
                    for ticker, quantity in portfolio.items():
                        value = quantity * stock_prices[ticker]
                        f.write(f"{ticker}: {quantity} shares @ ${stock_prices[ticker]:.2f} = ${value:.2f}\n")
                    f.write(f"\nTotal Value: ${total_value:.2f}")
                print(f"Portfolio saved to {filename}")
            except IOError:
                print("Error saving file.")
                
        elif choice == "5":
            print("Exiting program.")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    stock_portfolio_tracker()
