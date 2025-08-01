import numpy as np
import pandas as pd


def simulate_portfolios(returns: pd.DataFrame, n_simulations=5000, risk_free_rate=0.0):
    n_assets = returns.shape[1]
    mean_returns = returns.mean()
    cov_matrix = returns.cov()
    
    results = {
        'weights': [],
        'return': [],
        'volatility': [],
        'sharpe': []
    }

    for _ in range(n_simulations):
        weights = np.random.random(n_assets)
        weights /= np.sum(weights)

        annual_return = np.sum(mean_returns * weights) * 252
        annual_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix * 252, weights)))
        sharpe_ratio = (annual_return - risk_free_rate) / annual_volatility

        results['weights'].append(weights)
        results['return'].append(annual_return)
        results['volatility'].append(annual_volatility)
        results['sharpe'].append(sharpe_ratio)

    return pd.DataFrame(results)
