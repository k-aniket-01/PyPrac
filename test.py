# # from functools import wraps
# # def transactional_session():
# #     db = 'db'
# #     print("transaction sesion")
# # def perform_transaction(func):
# #     @wraps(func)
# #     def wrapper(*args, **kwargs):
# #         db = kwargs.pop('db', None) 
# #         if db is not None:
# #             return func(db, *args, **kwargs)
# #         else:
# #             with transactional_session() as db:
# #                 return func(db, *args, **kwargs)
# #     return wrapper
# # @perform_transaction
# # def greet(*a,**kw):
# #     return {"a":a,"kw":kw}
# # print(greet('aniket', name='ak'))


# # data = [1, 2, 2, 3, 4, 4, 5]

# # uni = []
# # for i in data:
# #     if i not in uni:
# #         uni.append(i)
# # print(uni)


# s = "aabbcdde"
# l = []

# for i in s:
#     if len(l) == 0:
#         l.append(i)
#     elif l[0] == i:
#             l.pop()
#     else:
#         print(l[0])
#         break
            
    
    
# def reverse_str(s:str) -> str:
#     s = list(s)
#     i,j = 0,len(s)-1
#     while i < j:
#         s[i], s[j] = s[j], s[i]
#         i += 1
#         j -= 1
#     s = "".join(s)
#     return s
# print(reverse_str("python"))

from email import message
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
         
        