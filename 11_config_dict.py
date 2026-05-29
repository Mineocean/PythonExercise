# 配置字典：集中管理配置项，通过键读写配置值
# 演示字典作为配置对象的读取和修改

config={
    'input_path':'./data/input',
    'output_path':'./data/output',
    'log_level':'Error',
    'Max_threads':4,
    'timeout':30
}

# 读取配置
print(f'input_path:{config["input_path"]}')

# 修改配置值
config['timeout']=90000
print(f'timeout:{config["timeout"]}')
