import math
def func(x):
    binary_code = list()
    n = int(math.log2(x))
    remainder = x 
    for i in range(n + 1):
        calculation = remainder - 2 ** n
        if calculation >= 0:
            remainder = calculation
            binary_code.append(1)
        else:
            binary_code.append(0)
        n -= 1
    binary_code_str = "".join(map(str, binary_code))
    if binary_code_str.count('1') == 1:
        binary_code_str2 = binary_code_str + '0'
    else:
        binary_code_str2 = binary_code_str.replace('01','10')
    result = 0
    m = 0
    for j in binary_code_str2[::-1]:
        if j == '1':
            result += 2 ** m
        m += 1
    return f"Input: {x} => Output: {result}  ({int(binary_code_str)} => {int(binary_code_str2)})"
print(func(139))
print(func(256))
print(func(764))