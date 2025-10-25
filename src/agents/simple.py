
from langgraph.graph import MessagesState, StateGraph, START, END
from langchain_core.messages import AIMessage

# Simple memorie for all agents using pure python
class State(MessagesState):
    """
    A TypedDict representing the state structure for storing customer information.
    
    Attributes:
        customer_name (str): The name of the customer
        my_age (int): The age associated with the state
    """
    customer_name: str
    my_age: int
    my_available_jobs: list[{
      "job_title": str,
      "salary": float
    }]


# Each nodo has access to the shared state
# The principle function of the node id update and return
# the state to update
def node_1(state: State):
  if state.get("customer_name") is None:
    return {
      "customer_name": "Andres Trujillo"
    }
  else:
    ai_message = AIMessage(content = "Hello, how can I help you today?")
    return {
      "messages": [ai_message]
    }

# Creation of the connection with flow of the Graph
builder = StateGraph(State)
# The name of the nodo for best practice should be the name
# of the node function
builder.add_node("node_1", node_1)

builder.add_edge(START, "node_1")
builder.add_edge("node_1", END)

agent = builder.compile()