from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader


documents = SimpleDirectoryReader('examples/paul_graham_essay/polygon-zkevm/').load_data()
index = GPTSimpleVectorIndex(documents)


response = index.query("How to setup a local ZKEVM node?")
print(response)
