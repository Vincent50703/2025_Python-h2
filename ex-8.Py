def greet():
    " " "簡單的問候函數" " "
    print("你好！歡迎學習python!)
    
#   呼叫函數
greet()

def add_numbers(a, b):
    """計算兩個數字的和"""
    result = a + b
    return result
    
# 使用函數
sum_result ＝ add_numbers（５, 3)
print(f"5 + 33 )={sum_result}

import array
a = array.array('i', [1, 2, 3, 4])
print(a)

import array
a = array.array('i', [1, 2, 3, 4])
a = array.array('f', [1, 2, 3, 4])
#a = array.array("c" ,["1", "2", "3", "4"]) # wrong case

print(a)

print(a[0])

for item in a:
    print(item)
