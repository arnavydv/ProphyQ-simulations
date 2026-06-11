import numpy as np
import math

def monte_carlo_option_price(S0, K, T, r, sigma, num_simulations=10000):
    """
    Monte Carlo simulation for European call option pricing

    Parameters:
    S0: Initial stock price
    K: Strike price
    T: Time to maturity (in years)
    r: Risk-free interest rate
    sigma: Volatility of the stock
    num_simulations: Number of simulations to run

    Returns:
    Option price
    """
    # Calculate drift and diffusion terms
    drift = (r - 0.5 * sigma**2) * T
    diffusion = sigma * np.sqrt(T)

    # Generate random numbers
    random_numbers = np.random.standard_normal(num_simulations)

    # Calculate stock prices at maturity
    ST = S0 * np.exp(drift + diffusion * random_numbers)

    # Calculate option payoffs
    payoffs = np.maximum(ST - K, 0)

    # Discount payoffs back to present value
    option_price = np.exp(-r * T) * np.mean(payoffs)

    return option_price

def black_scholes_price(S0, K, T, r, sigma):
    """
    Black-Scholes analytical price for European call option
    """
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    price = S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return price

# Import for Black-Scholes calculation
from scipy.stats import norm

def simulate_portfolio_returns(returns, weights, num_simulations=10000):
    """
    Simulate portfolio returns based on historical returns and weights

    Parameters:
    returns: Historical returns matrix (assets x time)
    weights: Portfolio weights for each asset
    num_simulations: Number of simulations

    Returns:
    Simulated portfolio returns
    """
    num_assets = len(weights)
    num_obs = returns.shape[1]

    # Calculate covariance matrix
    cov_matrix = np.cov(returns)

    # Generate correlated random returns
    simulated_returns = np.random.multivariate_normal(
        np.mean(returns, axis=1),
        cov_matrix,
        num_simulations
    )

    # Calculate portfolio returns
    portfolio_returns = np.dot(simulated_returns, weights)

    return portfolio_returns

def calculate_var(returns, confidence_level=0.95):
    """
    Calculate Value at Risk (VaR)

    Parameters:
    returns: Portfolio returns
    confidence_level: Confidence level for VaR

    Returns:
    VaR value
    """
    var = np.percentile(returns, (1 - confidence_level) * 100)
    return var

def calculate_cvar(returns, confidence_level=0.95):
    """
    Calculate Conditional Value at Risk (CVaR/Expected Shortfall)

    Parameters:
    returns: Portfolio returns
    confidence_level: Confidence level for CVaR

    Returns:
    CVaR value
    """
    var = calculate_var(returns, confidence_level)
    cvar = np.mean(returns[returns <= var])
    return cvar
