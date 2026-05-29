# 字典实现角色权限映射：根据用户角色返回对应的权限列表
# 使用 get() 为未知角色返回空列表，避免 KeyError

#配置多条件映射
#根据用户角色分配用户权限
role_permissions={
    'admin':['read','write','delete','create','manage'],
    'user':['read','write'],
    'viewer':['read']
}

def get_user_permissions(role):
    """根据角色名获取权限列表，未知角色返回空列表"""
    return role_permissions.get(role,[])

# 遍历测试角色
for role in ['admin', 'user', 'viewer', 'unknown']:
    print(f"{role.title()} Permissions", get_user_permissions(role))
