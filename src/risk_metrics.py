import numpy as np
import pandas as pd

#Calcule les rendements log (ou simples) à partir des prix.
def compute_returns(prices: pd.DataFrame, log=True) -> pd.DataFrame:
    if log:
        return np.log(prices / prices.shift(1)).dropna()
    else:
        return prices.pct_change().dropna()

#Volatilité journalière (écart-type) pour chaque actif.
def compute_volatility(returns: pd.DataFrame) -> pd.Series:
    return returns.std()


#Sharpe Ratio annualisé à partir de rendements journaliers
def compute_sharpe_ratio(returns: pd.DataFrame, risk_free_rate=0.0) -> pd.Series:
    rf_daily = risk_free_rate / 252
    excess_return = returns - rf_daily
    sharpe = excess_return.mean() / excess_return.std()
    return sharpe * np.sqrt(252)
