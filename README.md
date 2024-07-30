# Financial Analysis Project

This project performs a basic financial analysis on selected stock tickers, focusing on JPMorgan Chase and its competitors.

## Features
- Fetches historical stock data
- Calculates daily returns and correlations
- Generates visualizations for stock price comparison
- Saves data to CSV files for further analysis

## Installation
1. Clone this repository
2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Adjust the `config.yaml` file if needed
2. Run the analysis:
   ```
   python main.py
   ```
3. Check the console output and generated files

## Project Structure
- `src/`: Contains the main source code
- `tests/`: Contains unit tests (to be implemented)
- `config.yaml`: Configuration file for tickers and analysis period
- `main.py`: Main script to run the analysis
- `requirements.txt`: List of required Python packages

## Future Improvements
- Implement unit tests
- Add more advanced financial metrics
- Create a web interface for the analysis
