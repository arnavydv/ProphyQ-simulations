import os
import sys
import unittest
import numpy as np

# Make the "Probability simulators" directory importable
MODULE_DIR = os.path.dirname(__file__)
if MODULE_DIR not in sys.path:
    sys.path.insert(0, MODULE_DIR)

import monte_carlo_option_pricing as m


class TestMonteCarloOptionPricing(unittest.TestCase):
    def setUp(self):
        np.random.seed(12345)

    def test_monte_carlo_option_price_sanity(self):
        price = m.monte_carlo_option_price(S0=100, K=105, T=1, r=0.05, sigma=0.2, num_simulations=20000)
        self.assertTrue(np.isfinite(price), "Price should be finite")
        self.assertGreaterEqual(price, 0.0, "Call option price should be non-negative")

    def test_simulate_portfolio_returns_shape(self):
        # 2 assets, 100 observations
        returns = np.random.normal(0, 0.01, size=(2, 100))
        weights = np.array([0.6, 0.4])

        num_simulations = 5000
        simulated = m.simulate_portfolio_returns(returns, weights, num_simulations=num_simulations)
        self.assertEqual(simulated.shape, (num_simulations,))

    def test_monte_carlo_vs_black_scholes_reasonable_close(self):
        # If SciPy isn't available, black_scholes_price may not work.
        try:
            bs = m.black_scholes_price(S0=100, K=105, T=1, r=0.05, sigma=0.2)
        except Exception:
            self.skipTest("black_scholes_price could not be computed (likely SciPy missing).")

        np.random.seed(999)
        mc = m.monte_carlo_option_price(S0=100, K=105, T=1, r=0.05, sigma=0.2, num_simulations=150000)

        # Monte Carlo is noisy; allow a relative tolerance.
        # Typical error should be within a few percent with 150k paths.
        self.assertAlmostEqual(mc, bs, delta=max(0.5, 0.1 * bs))

    def test_cvar_leq_var_for_losses(self):
        # For losses (more negative is worse), CVaR should be <= VaR
        # since CVaR averages the worst tail (more negative outcomes).
        np.random.seed(42)
        returns = np.random.normal(loc=0.0, scale=0.02, size=200000)
        # Convert to "losses-like" tail by shifting slightly negative mean
        returns = returns - 0.01

        var = m.calculate_var(returns, confidence_level=0.95)
        cvar = m.calculate_cvar(returns, confidence_level=0.95)

        self.assertLessEqual(cvar, var, "CVaR should be <= VaR when using the worst-tail definition")


if __name__ == "__main__":
    unittest.main()
