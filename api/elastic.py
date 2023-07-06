from elasticsearch import Elasticsearch

PWD = "l9+CScQb=tuyuNHdgALf"
ID = "elastic"
ADDR = "http://40.66.36.190:9200"
INDEX_NAME = "Cyberbox"

def persist_data(json_arr):
    es = Elasticsearch(hosts=[ADDR], basic_auth=(ID, PWD))
    if es.ping():
        print("Connection to Elasticsearch successful.")
    else:
        print("Failed to connect to Elasticsearch.")
        es.close()
 

    if not es.indices.exists(index=INDEX_NAME):
        es.indices.create(index=INDEX_NAME)
    for doc in data:
        # Index a document in Elasticsearch
        res = es.index(index=INDEX_NAME, document=doc)
        print(res['result'])
    es.close()

##sqkmnjfknkm
doc1 =  {
    'author': 'author_name',
    'text': 'Interensting content...',
}

doc2 =  {
    'author': 'rodrigo',
    'text': 'Interenstfksdflùd content...',
}
data = [doc1, doc2]

#persist_data(data)
