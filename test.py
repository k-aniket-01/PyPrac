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

# from email import message
# from fastapi import FastAPI, WebSocket, WebSocketDisconnect

# app = FastAPI()

# class ConnectionManager:
#     def __init__(self):
#         self.active_connections: set[WebSocket] = set()
        
#     async def connect(self, websocket:WebSocket):
#         await websocket.accept()
#         self.active_connections.add(websocket)
#         print(f"connected users: {len(self.active_connections)}")
        
#     async def disconnect(self, websocket:WebSocket):
#         self.active_connections.discard(websocket)
#         print(f"connected users: {len(self.active_connections)}")
        
#     async def brodcast(self, message:str):
#         for connection in list(self.active_connections):
#             await connection.send_text(message)
            
# manager = ConnectionManager()

# @app.websocket('/test/socket')
# async def websocket_endpoint(websocket: WebSocket):
#     await manager.connect(websocket)
#     try:
#         while True:
#             message = await websocket.receive_text()
            
#             await websocket.send_text(message)
            
#     except WebSocketDisconnect:
#         await manager.disconnect(websocket)  
         
        
        
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
# a = ListNode(1)
# b = ListNode(2)
# a.next = b 
# c = ListNode(6)
# b.next = c
# d = ListNode(3)
# c.next = d
# e = ListNode(4)
# d.next = e
# f = ListNode(5)
# e.next = f
# g = ListNode(6)
# f.next = g
# head = a 
# def removeElements(head: ListNode | None, val: int) -> ListNode | None:
#     ll = ListNode()
#     res = ll
#     while head:
#         if head.val == val:
#             head = head.next
#         else:
#             ll.next = head
#             head = head.next
#             ll = ll.next
#     ll.next = None
#     return res.next

# data = removeElements(head, 6)

# while data:
#     print(data.val)
#     data = data.next


def addBinary(a: str, b: str) -> str:
    k, j = len(a)-1, len(b)-1
    print(f"i,j>{k,j}")
    res = ''
    rem = 0 
    end = k if k < j else j
    print(f"end>{end}")
    for i in range(end, -1, -1):
        if a[k]=='0' and b[j]=='0':
            res = str(1) + res if rem else str(0)+res
            rem = 0
        elif a[k]=='1' and b[j]=='1':
            rem = 1
            res = str(0)+res
        else:
            res = str(1)+res if rem else str(0)+res
            rem=0
        k -= 1
        j -= 1
    while k > -1:
        if a[k] == '1':
            if rem:
                res = str(0) + res
                rem = 1
            else:
                res = str(1) + res
        else:
            res = str(1)+res
            rem = 0
        k -= 1
    while j > -1:
        if b[j] == '1':
            if rem:
                res = str(0) + res
                rem = 1
            else:
                res = str(1) + res
        else:
            res = str(1)+res
            rem = 0
        # res = a[i] + res
        j -= 1

    if rem:
        res = str(1)+res
    return res
print(addBinary('100','110010'))
            