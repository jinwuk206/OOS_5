def add(a, b):
    """
    加法运算
    :param a: 第一个数
    :param b: 第二个数
    :return: 两数之和
    """
    return a + b

def multiply(a, b):
    """
    乘法运算
    :param a: 第一个数
    :param b: 第二个数
    :return: 两数之积
    """
    return a * b

# 测试代码
if __name__ == "__main__":
    print("加法测试:")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"-1 + 5 = {add(-1, 5)}")
    print(f"0 + 0 = {add(0, 0)}")
    
    print("\n乘法测试:")
    print(f"2 × 3 = {multiply(2, 3)}")
    print(f"-1 × 5 = {multiply(-1, 5)}")
    print(f"0 × 100 = {multiply(0, 100)}")
