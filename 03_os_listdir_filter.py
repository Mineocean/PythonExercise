# os.listdir 结合条件过滤：筛选当前目录下以 's' 开头且以 '.py' 结尾的文件
# 列表推导式 + os.listdir 实现文件名的条件过滤

import os

# 将过滤结果赋值并打印，否则运行无可见输出
result = [filename for filename in os.listdir('.')
          if filename.endswith('.py') and filename.startswith('s')]
print(result)
