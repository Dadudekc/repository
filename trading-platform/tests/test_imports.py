import importlib


def test_imports():
    for module in ['pandas', 'numpy', 'yfinance']:
        importlib.import_module(module)

