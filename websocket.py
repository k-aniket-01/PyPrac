from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: set[WebSocket] = set()
        
    async def connect(self, websocket:WebSocket):
        await websocket.accept()
        self.active_connections.add(websocket)
        print(f"connected users: {len(self.active_connections)}")
        
    async def disconnect(self, websocket:WebSocket):
        self.active_connections.discard(websocket)
        print(f"connected users: {len(self.active_connections)}")
        
    async def brodcast(self, message:str):
        for connection in list(self.active_connections):
            await connection.send_text(message)
            
manager = ConnectionManager()

@app.websocket('/test/socket')
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            message = await websocket.receive_text()
            
            await websocket.send_text(message)
            
    except WebSocketDisconnect:
        await manager.disconnect(websocket)  
         
        