import matplotlib.pyplot as plt

def plot_stock_comparison(data, title, filename):
    plt.figure(figsize=(12, 6))
    for column in data.columns:
        plt.plot(data.index, data[column], label=column)
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Stock Price in USD')
    plt.legend()
    plt.savefig(filename)
    plt.close()