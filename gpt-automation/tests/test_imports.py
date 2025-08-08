import importlib


def test_imports():
    for module in ['openai', 'langchain']:
        importlib.import_module(module)

