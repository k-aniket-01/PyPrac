from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect

app = FastAPI()

@app.post('/webhook')
async def webhook(reqeust:Request):
    data = await reqeust.json()
    print("webhook recived")
    print(data)
    return {"message":"webhook recired",
           "data":data}
    
@app.websocket('/ws')
async def websocket_endpoint(websocket:WebSocket):
    await websocket.accept()
    print("client connected")
    try:
        while True:
            message = await websocket.receive_text()
            print("Recived:", message)
            await websocket.send_text(f"server_recived:{message}")
    except WebSocketDisconnect:
        print("websocket disconnected")