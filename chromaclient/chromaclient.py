import chromadb
from chromadb.utils import embedding_functions

class Chroma():
    def __init__(self):
        self.chromaClient=chromadb.PersistentClient()
        self.collection=self.chromaClient.get_or_create_collection(
            name="HSN_Data",
            embedding_function=embedding_functions.DefaultEmbeddingFunction()
        )
    def addDatas(self,code,description):
        batch_size=5145 #5146 max size
       
        for i in range(0, len(code), batch_size):
            batch_code = code[i:i + batch_size]
            batch_description = description[i:i + batch_size]
            batch_metadata=[ {f"{i}":batch_description[i]} for i in range(len(batch_description))]
            self.collection.add(
                documents=batch_description,
                ids=batch_code,
                metadatas=batch_metadata
            )
        
    def getDatas(self,description):
        print(description)
        res=self.collection.query(
            query_texts=[description]
        )
        response=[{i:j} for i,j in zip(res['ids'],res['documents'])]
        return response
    
    
    def getDatasOnIndex(self,code):
        print(code)
        res=self.collection.get(
            ids=code
        )
        print(res)
        response=[{i:j} for i,j in zip(res['ids'],res['documents'])]
        return response 