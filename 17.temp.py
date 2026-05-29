"""
for i in range(1, 11):
    print(("*" * (2*i-1)).center(20))
"""

# 12个月英文
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

# 取前三位首字母缩写
abbrs = [m[:3] for m in months]
print(abbrs)

# 一旦出现 r 就全大写
months_r_upper = [s.upper() if "r" in s else s for s in months]
print(months_r_upper)
