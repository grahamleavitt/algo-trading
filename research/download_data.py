import yfinance as yf
from pathlib import Path


# Configuration
TICKERS = [
    "CRWD", "VOO", "GOOGL",
    "AAPL", "MSFT", "AMZN", "NVDA",
    "JPM", "KO", "XOM", "WMT"
]

START_DATE = "2023-01-01"
END_DATE = None  # None = today

# From working dir algo-trading/
RAW_DATA_DIR = Path("../data/raw")

# Download loop
for ticker in TICKERS:
    print(f"Downloading {ticker}...")
    df = yf.download(
        ticker,
        start=START_DATE,
        end=END_DATE,
        auto_adjust=True,
        progress=False,
    )

    df.to_csv(RAW_DATA_DIR / f"{ticker}.csv")

print("Download complete.")
