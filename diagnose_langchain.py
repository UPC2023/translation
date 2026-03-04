import sys
try:
    import langchain
    print(f"langchain imported: {langchain.__file__}")
    print(f"langchain version: {langchain.__version__}")
    print(f"dir(langchain): {dir(langchain)}")
except ImportError as e:
    print(f"Error importing langchain: {e}")

try:
    import langchain.chains
    print("langchain.chains imported successfully")
except ImportError as e:
    print(f"Error importing langchain.chains: {e}")

try:
    from langchain.chains import RetrievalQA
    print("RetrievalQA imported successfully")
except ImportError as e:
    print(f"Error importing RetrievalQA: {e}")

try:
    import langchain_community
    print(f"langchain_community imported: {langchain_community.__file__}")
except ImportError as e:
    print(f"Error importing langchain_community: {e}")
