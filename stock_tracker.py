import csv

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 175,
    "MSFT": 410
}

def stock_portfolio_tracker():
    print("--- Stock Portfolio Tracker ---")
    print("Available Stocks and Prices ($):", STOCK_PRICES)
    
    portfolio = {}
    total_portfolio_value = 0
    
    while True:
        symbol = input("\nEnter Stock Symbol (ya 'done' type karein finish karne ke liye): ").upper()
        if symbol == 'DONE':
            break
            
        if symbol not in STOCK_PRICES:
            print("Ye stock list mein nahi hai. Available stocks:", list(STOCK_PRICES.keys()))
            continue
            
        try:
            quantity = int(input(f"Enter quantity for {symbol}: "))
            if quantity <= 0:
                print("Quantity 0 se badi honi chahiye.")
                continue
            portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        except ValueError:
            print("Kripya valid number enter karein.")
            
    if not portfolio:
        print("Aapne koi stock add nahi kiya.")
        return

    print("\n--- Portfolio Summary ---")
    summary_data = []
    
    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        total_portfolio_value += value
        summary_data.append([symbol, qty, price, value])
        print(f"{symbol}: Quantity = {qty}, Price = ${price}, Total Value = ${value}")
        
    print(f"\nTotal Portfolio Value: ${total_portfolio_value}")
    
    save_choice = input("\nKya aap is summary ko CSV file mein save karna chahte hain? (yes/no): ").lower()
    if save_choice in ['yes', 'y']:
        filename = "portfolio_summary.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Stock Symbol", "Quantity", "Price per Share ($)", "Total Value ($)"])
            writer.writerows(summary_data)
            writer.writerow([])
            writer.writerow(["Total Portfolio Value", "", "", total_portfolio_value])
        print(f"Portfolio details successfully '{filename}' mein save ho gaye hain.")

if __name__ == "__main__":
    stock_portfolio_tracker()