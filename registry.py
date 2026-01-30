```python
from fastapi import FastAPI
import datetime
app = FastAPI()
nodes = {}
@app.post("/register")
def register_node(node_id: str, url: str):
    nodes[node_id] = {"url": url, "time": datetime.datetime.now()}
    return {"status": "ok", "network_size": len(nodes)}
@app.get("/network")
def get_network():
    return {"nodes": nodes, "total": len(nodes)}
