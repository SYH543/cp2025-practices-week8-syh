import numpy as np

# 此函数使用标准公式求解二次方程 ax^2 + bx + c = 0
def standard_formula(a, b, c):
    """
    利用标准公式求解二次方程。

    参数:
        a (float): 二次项系数
        b (float): 一次项系数
        c (float): 常数项

    返回:
        tuple: 方程的两个根 (x1, x2)，若无实根则返回 None
    """
    # 计算判别式
    discriminant = b * b - 4 * a * c
    # 若判别式小于 0，说明方程无实根
    if discriminant < 0:
        return None

    # 计算判别式的平方根
    sqrt_discriminant = np.sqrt(discriminant)
    # 计算两个根
    x1 = (-b + sqrt_discriminant) / (2 * a)
    x2 = (-b - sqrt_discriminant) / (2 * a)

    return x1, x2

# 此函数使用替代公式求解二次方程 ax^2 + bx + c = 0
def alternative_formula(a, b, c):
    """
    利用替代公式求解二次方程，此公式通过对标准公式变形得到。

    参数:
        a (float): 二次项系数
        b (float): 一次项系数
        c (float): 常数项

    返回:
        tuple: 方程的两个根 (x1, x2)，若无实根则返回 None
    """
    # 计算判别式
    discriminant = b * b - 4 * a * c
    # 若判别式小于 0，说明方程无实根
    if discriminant < 0:
        return None

    # 计算判别式的平方根
    sqrt_discriminant = np.sqrt(discriminant)
    # 计算两个根
    x1 = (2 * c) / (-b - sqrt_discriminant)
    x2 = (2 * c) / (-b + sqrt_discriminant)

    return x1, x2

# 此函数是稳定的二次方程求根程序，能处理各种特殊情况和数值稳定性问题
def stable_formula(a, b, c):
    """
    稳定的二次方程求根函数，可处理多种特殊情形。

    参数:
        a (float): 二次项系数
        b (float): 一次项系数
        c (float): 常数项

    返回:
        tuple: 方程的两个根 (x1, x2)，若无实根则返回 None
    """
    # 处理 a 近似为 0 的特殊情况
    if abs(a) < 1e-10:
        # 若 a 和 b 都近似为 0
        if abs(b) < 1e-10:
            # 若 c 不为 0，方程无解；若 c 为 0，方程有无穷多解
            return None if abs(c) > 1e-10 else (0, 0)
        # 此时方程为一次方程，返回其解
        return (-c / b, -c / b)

    # 计算判别式
    discriminant = b * b - 4 * a * c
    # 若判别式小于 0，说明方程无实根
    if discriminant < 0:
        return None

    # 计算判别式的平方根
    sqrt_discriminant = np.sqrt(discriminant)
    # 根据 b 的正负选择合适的公式计算根
    if b >= 0:
        x1 = (-b - sqrt_discriminant) / (2 * a)
        x2 = (2 * c) / (-b - sqrt_discriminant)
    else:
        x1 = (-b + sqrt_discriminant) / (2 * a)
        x2 = (2 * c) / (-b + sqrt_discriminant)

    return x1, x2

# 主函数，用于测试不同的二次方程
def main():
    # 定义测试用例
    test_cases = [
        (1, 2, 1),             # 简单情况
        (1, 1e5, 1),           # b 远大于 a 和 c
        (0.001, 1000, 0.001),  # 原测试用例
    ]

    # 遍历每个测试用例
    for a, b, c in test_cases:
        print("\n" + "=" * 50)
        print(f"测试方程：{a}x^2 + {b}x + {c} = 0")

        # 使用标准公式求解
        roots1 = standard_formula(a, b, c)
        print("\n方法1（标准公式）的结果：")
        if roots1:
            print(f"x1 = {roots1[0]:.15f}, x2 = {roots1[1]:.15f}")
        else:
            print("无实根")

        # 使用替代公式求解
        roots2 = alternative_formula(a, b, c)
        print("\n方法2（替代公式）的结果：")
        if roots2:
            print(f"x1 = {roots2[0]:.15f}, x2 = {roots2[1]:.15f}")
        else:
            print("无实根")

        # 使用稳定的求根程序求解
        roots3 = stable_formula(a, b, c)
        print("\n方法3（稳定求根程序）的结果：")
        if roots3:
            print(f"x1 = {roots3[0]:.15f}, x2 = {roots3[1]:.15f}")
        else:
            print("无实根")

if __name__ == "__main__":
    main()
