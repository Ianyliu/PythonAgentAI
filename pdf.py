import os
from llama_index.readers.file import PDFReader
from llama_index.core.storage import StorageContext
from llama_index.core import VectorStoreIndex
from llama_index.core.indices.loading import load_index_from_storage
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader


load_dotenv()

def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        print("building index", index_name)
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )

    return index


pdf_path = os.path.join("data", "Canada.pdf")
canada_pdf = PDFReader().load_data(file=pdf_path)
canada_index = get_index(canada_pdf, "canada")
canada_engine = canada_index.as_query_engine()



# def get_doc_index(data, index_name):
#     index = None
#     if not os.path.exists(index_name):
#         print("building index", index_name)
#         index = VectorStoreIndex.from_documents(data, show_progress=True)
#         index.storage_context.persist(persist_dir=index_name)
#     else:
#         index = load_index_from_storage(
#             StorageContext.from_defaults(persist_dir=index_name)
#         )
    
#     return index

# documents = SimpleDirectoryReader("/workspaces/PythonAgentAI/data").load_data()
# documents_index = get_doc_index(documents, "chat")
# documents_engine = documents_index.as_query_engine()
