import unittest

# Import test modules
import TestSettings
import TestConnector

# Initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Add tests to the test suite
suite.addTests(loader.loadTestsFromModule(TestSettings))
suite.addTests(loader.loadTestsFromModule(TestConnector))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
