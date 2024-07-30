import yaml
from datetime import datetime, timedelta
from src.data_fetcher import get_stock_data
from src.analysis import calculate_returns, calculate_correlations, calculate_average_returns
from src.visualization import plot_stock_comparison

def load_config():
    with open('config.yaml', 'r') as file:
        return yaml.safe_load(file)

def main():
    config = load_config()
    
    end_date = datetime.now()
    start_date = end_date - timedelta(days=config['days_to_analyze'])

    stock_data = get_stock_data(config['tickers'], start_date, end_date)
    
    returns = calculate_returns(stock_data)
    correlations = calculate_correlations(stock_data)
    avg_returns = calculate_average_returns(returns)

    print("Average Daily Returns:")
    print(avg_returns)
    print("\nStock Price Correlation:")
    print(correlations)

    plot_stock_comparison(stock_data, 'Stock Price Comparison', 'stock_comparison.png')
    
    stock_data.to_csv('stock_data.csv')
    returns.to_csv('returns_data.csv')

    print("Analysis complete. Check the generated CSV files and stock_comparison.png for results.")

if __name__ == "__main__":
    main()