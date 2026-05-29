"""
学生成绩分数计算器
功能：总分、平均分、最高/最低分、排名、及格率、等级分布
"""

students = [
    {"name": "张三", "scores": {"语文": 88, "数学": 92, "英语": 79, "物理": 85, "化学": 90}},
    {"name": "李四", "scores": {"语文": 75, "数学": 68, "英语": 82, "物理": 70, "化学": 65}},
    {"name": "王五", "scores": {"语文": 95, "数学": 97, "英语": 93, "物理": 91, "化学": 96}},
    {"name": "赵六", "scores": {"语文": 60, "数学": 55, "英语": 58, "物理": 62, "化学": 59}},
    {"name": "孙七", "scores": {"语文": 82, "数学": 78, "英语": 85, "物理": 80, "化学": 88}},
    {"name": "周八", "scores": {"语文": 45, "数学": 50, "英语": 42, "物理": 48, "化学": 40}},
]

# 获取所有科目
subjects = list(students[0]["scores"].keys())

# ========== 1. 每人总分 & 平均分 ==========
print("=" * 50)
print("一、每位学生总分与平均分")
print("=" * 50)

for s in students:
    total = sum(s["scores"].values())
    avg = total / len(subjects)
    s["total"] = total
    s["avg"] = avg
    print(f"{s['name']}: 总分={total}, 平均分={avg:.2f}")

# ========== 2. 全班各科统计 ==========
print("\n" + "=" * 50)
print("二、各科目全班统计")
print("=" * 50)

for subj in subjects:
    sco = [s["scores"][subj] for s in students]
    print(f"{subj}: 最高={max(sco)}, 最低={min(sco)}, 平均={sum(sco)/len(sco):.2f}")

# ========== 3. 排名（按总分降序） ==========
print("\n" + "=" * 50)
print("三、总分排名")
print("=" * 50)

ranked = sorted(students, key=lambda s: s["total"], reverse=True)
for i, s in enumerate(ranked, 1):
    print(f"第{i}名: {s['name']} ({s['total']}分)")

# ========== 4. 及格率（>=60分） ==========
print("\n" + "=" * 50)
print("四、各科及格率（>=60分）")
print("=" * 50)

for subj in subjects:
    sco = [s["scores"][subj] for s in students]
    pass_count = sum(1 for x in sco if x >= 60)
    rate = pass_count / len(sco) * 100
    print(f"{subj}: {pass_count}/{len(sco)} = {rate:.1f}%")

# ========== 5. 等级分布 ==========
print("\n" + "=" * 50)
print("五、总分等级分布")
print("=" * 50)

levels = {"优秀(>=450)": 0, "良好(400-449)": 0, "中等(350-399)": 0, "及格(300-349)": 0, "不及格(<300)": 0}
for s in students:
    t = s["total"]
    if t >= 450:      levels["优秀(>=450)"] += 1
    elif t >= 400:    levels["良好(400-449)"] += 1
    elif t >= 350:    levels["中等(350-399)"] += 1
    elif t >= 300:    levels["及格(300-349)"] += 1
    else:             levels["不及格(<300)"] += 1

for label, count in levels.items():
    print(f"{label}: {count}人")
