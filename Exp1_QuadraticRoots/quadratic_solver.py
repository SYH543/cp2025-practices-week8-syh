import numpy as np


def quadratic_roots_standard(a, b, c):
    """
    用标准公式求解二次方程 ax^2 + bx + c = 0
    :param a: 二次项系数
    :param b: 一次项系数
    :param c: 常数项
    :return: 方程的两个根组成的元组 (x1, x2)，若无实根则返回 None
    """
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return None
    sqrt_delta = np.sqrt(delta)
    root1 = (-b + sqrt_delta) / (2 * a)
    root2 = (-b - sqrt_delta) / (2 * a)
    return root1, root2


def quadratic_roots_alternative(a, b, c):
    """
    用替代公式求解二次方程 ax^2 + bx + c = 0
    :param a: 二次项系数
    :param b: 一次项系数
    :param c: 常数项
    :return: 方程的两个根组成的元组 (x1, x2)，若无实根则返回 None
    """
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return None
    sqrt_delta = np.sqrt(delta)
    root1 = (2 * c) / (-b - sqrt_delta)
    root2 = (2 * c) / (-b + sqrt_delta)
    return root1, root2


def quadratic_roots_stable(a, b, c):
    """
    稳定的二次方程求根程序，能处理各类特殊情况和数值稳定性问题
    :param a: 二次项系数
    :param b: 一次项系数
    :param c: 常数项
    :return: 方程的两个根组成的元组 (x1, x2)，若无实根则返回 None
    """
    if abs(a) < 1e-10:
        if abs(b) < 1e-10:
            return None if abs(c) > 1e-10 else (0, 0)
        single_root = -c / b
        return single_root, single_root

    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return None

    sqrt_delta = np.sqrt(delta)
    if b >= 0:
        root1 = (-b - sqrt_delta) / (2 * a)
        root2 = (2 * c) / (-b - sqrt_delta)
    else:
        root1 = (-b + sqrt_delta) / (2 * a)
        root2 = (2 * c) / (-b + sqrt_delta)
    return root1, root2


def execute_tests():
    test_equations = [
        (1, 2, 1),
        (1, 1e5, 1),
        (0.001, 1000, 0.001)
    ]

    for coef_a, coef_b, coef_c in test_equations:
        print("\n" + "=" * 50)
        print(f"测试方程：{coef_a}x^2 + {coef_b}x + {coef_c} = 0")

        # 用标准公式求解
        results_standard = quadratic_roots_standard(coef_a, coef_b, coef_c)
        print("\n方法1（标准公式）的结果：")
        if results_standard:
            root1, root2 = results_standard
            print(f"x1 = {root1:.15f}, x2 = {root2:.15f}")
        else:
            print("无实根")

        # 用替代公式求解
        results_alternative = quadratic_roots_alternative(coef_a, coef_b, coef_c)
        print("\n方法2（替代公式）的结果：")
        if results_alternative:
            root1, root2 = results_alternative
            print(f"x1 = {root1:.15f}, x2 = {root2:.15f}")
        else:
            print("无实根")

        # 用稳定公式求解
        results_stable = quadratic_roots_stable(coef_a, coef_b, coef_c)
        print("\n方法3（稳定求根程序）的结果：")
        if results_stable:
            root1, root2 = results_stable
            print(f"x1 = {root1:.15f}, x2 = {root2:.15f}")
        else:
            print("无实根")


if __name__ == "__main__":
    execute_tests()
