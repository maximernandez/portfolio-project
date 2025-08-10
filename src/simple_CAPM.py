import pandas as pd
import numpy as np
import yfinance as yf

def get_price_data(tickers, start, end):
    """Télécharge les prix ajustés depuis Yahoo Finance."""
    data = yf.download(tickers, start=start, end=end, auto_adjust=False)["Adj Close"]
    return data.dropna()

def compute_daily_returns(prices):
    """Calcule les rendements journaliers."""
    returns = prices.pct_change().dropna()
    return returns

def compute_betas_by_covariance(returns, benchmark_returns):
    #Calcule les betas par la formule covariance / variance
    betas = {}
    for ticker in returns.columns:
        cov = np.cov(returns[ticker], benchmark_returns)[0, 1]
        var = np.var(benchmark_returns)
        betas[ticker] = cov / var
    return betas

def compute_expected_returns_CAPM(betas, expected_market_return, risk_free_rate):
    #Applique la formule du CAPM pour chaque actif
    expected_returns = {}
    for ticker, beta in betas.items():
        expected_returns[ticker] = risk_free_rate + beta * (expected_market_return - risk_free_rate)
    return expected_returns

def run_capm_pipeline(tickers, benchmark="^GSPC", start="2023-01-01", end="2024-01-01",
                      expected_market_return=0.08, risk_free_rate=0.02):
    #Pipeline complet CAPM sans régression
    all_tickers = tickers + [benchmark]
    prices = get_price_data(all_tickers, start, end)
    returns = compute_daily_returns(prices)

    benchmark_returns = returns[benchmark]
    asset_returns = returns.drop(columns=[benchmark])

    betas = compute_betas_by_covariance(asset_returns, benchmark_returns)
    expected_returns = compute_expected_returns_CAPM(betas, expected_market_return, risk_free_rate)
    expected_returns = pd.Series(expected_returns)
    cov = asset_returns.cov()
    return betas, expected_returns, cov
