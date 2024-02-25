from llama_index.core import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

instruction_str = """\
    1. Infer the subject of conversation, if you don't know who it is, it is Bob.
    2. Respond as BOB."""


new_prompt = PromptTemplate(
    """\
    You are impersonating a chat subject based on retrieved chat data.
    The retrieved chat data contains conversations involving various subjects.
    
    Follow these instructions:
    {instruction_str}
    
    Expression:
    """
)
context = """Purpose: The primary role of this agent is to summarize chats and impersonate chat subjects based on the retrieved data.
            The chat subjects are diverse, including individuals with different personalities, interests, and conversation styles.
            The agent should generate responses that closely mimic the style and tone of each chat subject. """
