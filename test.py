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
            
    
    
def reverse_str(s:str) -> str:
    s = list(s)
    i,j = 0,len(s)-1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    s = "".join(s)
    return s
print(reverse_str("python"))