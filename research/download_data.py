import yfinance as yf
import pandas as pd
from pathlib import Path

TICKERS = ["AAPL", "AMZN", "CRWD", "GOOGL", "JPM", "KO", "MSFT", "NVDA", "VOO", "WMT", "XOM"]

START_DATE = "2023-01-01" # 3 years of data to exclude COVID

# Assumes working directory is algo-trading/
RAW_DATA_DIR = Path("data/raw")

for ticker in TICKERS:
    print(f"Downloading {ticker}...")
    df = yf.download(
        ticker,
        start=START_DATE,
        multi_level_index=False, # Solves issue of funky index which is bad for TS analysis
        progress=False
    )

    outpath = RAW_DATA_DIR / f"{ticker}.csv"
    df.to_csv(outpath, index=True, index_label="Date")

print(f"All {len(TICKERS)} downloads complete.")
