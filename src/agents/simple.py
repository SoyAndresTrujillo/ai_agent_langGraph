from typing import TypedDict
from langgraph.graph import StateGraph, START, END

# Simple memorie for all agents using pure python
class State(TypedDict):
    """
    A TypedDict representing the state structure for storing customer information.
    
    Attributes:
        customer_name (str): The name of the customer
        my_age (int): The age associated with the state
    """
    customer_name: str
    my_age: int

# Each nodo has access to the shared state
# The principle function of the node id update and return
# the state to update
def node_1(state: State):
  if state.get("customer_name") is None:
    return {
      "customer_name": "Andres Trujillo"
    }
  
  return {
    "my_age": 24
  }

# Creation of the connection with flow of the Graph
builder = StateGraph(State)
# The name of the nodo for best practice should be the name
# of the node function
builder.add_node("node_1", node_1)

builder.add_edge(START, "node_1")
builder.add_edge("node_1", END)

agent = builder.compile()