def getDataPoint(quote):
    """ Produce all of the needed values to generate a datapoint """
    """ --------------- Update this function ----------- """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price)/2
    return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
    if price_b != 0:
        return price_a / price_b
    else:
        return 0

def main():
    # Example iterations, replace this with your actual data source or loop logic
    iterations = 5  # Number of iterations
    
    # Dictionary to store stock prices
    prices = {}

    # Iterating through the data points and storing them in the prices dictionary
    for _ in range(iterations):
        # Sample quote data (replace this with actual data retrieval logic)
        quote = {'stock': 'XYZ', 'top_bid': {'price': '100'}, 'top_ask': {'price': '110'}}
        
        # Get data point
        stock, _, _, calculated_price = getDataPoint(quote)
        
        # Store data point in the prices dictionary
        prices[stock] = calculated_price

    # Calculating and printing ratios using the stored data points
    for stock, price in prices.items():
        ratio = getRatio(price, prices['XYZ'])  # Assuming 'XYZ' as the reference stock
        print(f'Ratio for {stock}: {ratio}')

if __name__ == "__main__":
    main()
