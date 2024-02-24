from dotenv import load_dotenv
load_dotenv()

import os
import pandas as pd
from llama_index.core.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, context
from note_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from pdf import canada_engine, chats_engine, bob_engine


# population_path = os.path.join("data", "population.csv")
# population_df = pd.read_csv(population_path)

# population_query_engine = PandasQueryEngine(
#     df=population_df, verbose=True, instruction_str=instruction_str
# )
# population_query_engine.update_prompts({"pandas_prompt": new_prompt})

# tools = [
#     note_engine,
#     QueryEngineTool(
#         query_engine=population_query_engine,
#         metadata=ToolMetadata(
#             name="population_data",
#             description="this gives information at the world population and demographics",
#         ),
#     ),
#     QueryEngineTool(
#         query_engine=canada_engine,
#         metadata=ToolMetadata(
#             name="canada_data",
#             description="this gives detailed information about canada the country",
#         ),
#     ),

#     QueryEngineTool(
#         query_engine=chats_engine,
#         metadata=ToolMetadata(
#             name="chat_data",
#             description="this gives detailed information about Ian's chats",
#         ),
#     ),
# ]
# tools = [
#     note_engine,
#     QueryEngineTool(
#         query_engine=canada_engine,
#         metadata=ToolMetadata(
#             name="canada_data",
#             description="this gives detailed information about canada the country",
#         ),
#     ),

#     QueryEngineTool(
#         query_engine=chats_engine,
#         metadata=ToolMetadata(
#             name="chat_data",
#             description="this gives detailed information about Ian's chats",
#         ),
#     ),

#     QueryEngineTool(
#         query_engine=bob_engine,
#         metadata=ToolMetadata(
#             name="bob_chat_data",
#             description="this gives detailed information about Bob's chat with Ian",
#         ),
#     ),
# ]

tools = [
    note_engine,

    QueryEngineTool(
        query_engine=bob_engine,
        metadata=ToolMetadata(
            name="bob_chat_data",
            description="this gives detailed information about Bob's chat with Ian",
        ),
    ),
]


llm = OpenAI(model="gpt-3.5-turbo")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.query(prompt)
    print(result)
