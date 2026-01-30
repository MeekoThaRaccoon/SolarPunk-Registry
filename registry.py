from fastapi import FastAPI
import datetime

app = FastAPI()
nodes = {}

@app.post("/register")
def register(node_id: str, url: str):
    nodes[node_id] = {"url": url, "time": datetime.datetime.now().isoformat()}
    return {"status": "registered", "network_size": len(nodes)}

@app.get("/network")
def network():
    return {"nodes": nodes, "total": len(nodes)}

@app.get("/")
def root():
    return {"message": "SolarPunk Registry", "status": "active", "timestamp": datetime.datetime.now().isoformat()}
