# ch1_1.py
# 輸入階層數n,列出階層數的結果

def factorial(n):
    """ 計算n的階乘, n 必須是正整數 """
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))

N = eval(input("請輸入階乘數 : "))
#　eval() 函數用來執行一個字符串表達式，並返回表達式的值
print(N, " 的階乘結果是 = ", factorial(N))





    
