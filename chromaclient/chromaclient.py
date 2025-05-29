import chromadb
from chromadb.utils import embedding_functions


class Chroma():
    def __init__(self):
        self.chromaClient = chromadb.HttpClient(port=8001)
        self.collection = self.chromaClient.get_or_create_collection(
            name="HSN_Data",
            embedding_function=embedding_functions.DefaultEmbeddingFunction()
        )

    def addDatas(self, code, description):
        batch_size = 5145  # 5146 max size

        for i in range(0, len(code), batch_size):
            batch_code = code[i:i + batch_size]
            batch_description = description[i:i + batch_size]
            batch_metadata = [{f"{i}": batch_description[i]}
                              for i in range(len(batch_description))]
            self.collection.add(
                documents=batch_description,
                ids=batch_code,
                metadatas=batch_metadata
            )

    def getDatas(self, description):
        
        res = self.collection.query(
            query_texts=[description]
        )
        
        response = [{i: j} for i, j in zip(res['ids'][0], res['documents'][0])]
        return response

    def getDatasOnIndex(self, code):
        if len(code)==0:
            return 
        res = self.collection.get(
            ids=code
        )
       
        response = [{i: j} for i, j in zip(res['ids'], res['documents'])]
        return response
