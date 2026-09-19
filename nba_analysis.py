import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 自动创建charts文件夹
if not os.path.exists("charts"):
    os.mkdir("charts")

# 球员数据
data = {
    "球员":["库里","詹姆斯","杜兰特","字母哥","东契奇","塔图姆","巴特勒"],
    "位置":["PG","SF","SF","PF","PG","SF","SF"],
    "得分":[29,27,28,29,30,26,22],
    "篮板":[5,8,7,11,9,8,5],
    "助攻":[6,7,5,5,9,4,6]
}
df = pd.DataFrame(data)

print("====球员数据====")
print(df)

# 得分柱状图
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.figure(figsize=(10,5))
sns.barplot(x="球员",y="得分",data=df)
plt.title("NBA球员得分对比")
plt.tight_layout()
plt.savefig("charts/score_bar.png")
plt.show()

# 按位置求平均得分
pos_avg = df.groupby("位置")["得分"].mean()
print("\n====各位置平均得分====")
print(pos_avg)
