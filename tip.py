
# 输入餐费和小费比例
canfei = float(input("请输入餐费："))
xiaofei_p = float(input("请输入小费比例（例如 15 或 0.15）："))

# 统一小费比例
if xiaofei_p > 1:
    xiaofei_p = xiaofei_p / 100

# 检查输入
if canfei < 0 or xiaofei_p < 0:
    print("餐费和小费比例不能为负数！")
else:
    xiaofei = canfei * xiaofei_p
    total = canfei + xiaofei

    print(f"餐费：{canfei:.2f}")
    print(f"小费：{xiaofei:.2f}")
    print(f"总费用：{total:.2f}")
