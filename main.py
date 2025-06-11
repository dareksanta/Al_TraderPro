from strategies.rsi_macd import generate_signal
from data_loader.data_loader import load_data

def main():
    print("Loading data...")
    sample_data = load_data("sample_data.csv")

    print("Generating signal...")
    signal = generate_signal(sample_data)
    print(f"Signal: {signal}")

if __name__ == "__main__":
    main()