# 字典模拟登录缓存系统：存储用户令牌，支持登录、验证、登出操作
# 演示字典的增（login）、查（check_login）、删（del）操作

#模拟登录系统
login_cache={}

def login(user_id,token):
    """将用户令牌存入缓存"""
    login_cache[user_id]=token
    print(f"User {user_id} login success,Cache updated")

def check_login(user_id,token):
    """验证用户令牌是否匹配"""
    cache_token=login_cache.get(user_id,None)
    if cache_token==token:
        return True,"Login in OK"
    else:
        return False,"Login in Failed or Token Expired"

#模拟用户登录
login("Tom","0d000721")
print(check_login("Tom","0d000721"))

login("Jerry","0d000722")
print(check_login("Jerry","0d000722") )

#用户登出：从缓存中删除令牌
del login_cache["Tom"]
print(check_login("Tom","0d000722"))
