import os
from llama_index.readers.file import PDFReader
from llama_index.core.storage import StorageContext
from llama_index.core import VectorStoreIndex
from llama_index.core.indices.loading import load_index_from_storage
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader
import glob


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


pdf_chats = glob.glob(f"chatdata/**/*.pdf", recursive=True)
chat_pdfs = [PDFReader().load_data(file=i) for i  in pdf_chats]
chats_index = get_index(canada_pdf, "chats")
chats_engine = chats_index.as_query_engine()

pdf_path = os.path.join("chatdata", "bob.pdf")
bob_pdf = PDFReader().load_data(file=pdf_path)
bob_index = get_index(bob_pdf, "bob")
bob_engine = bob_index.as_query_engine()
