N = int(input())  # número de operações 

A = 0
B = 0 

interruptor = list(map(int, input().split())) 

for op in interruptor:

    if op == 1:
        A = A ^ 1
                  
    elif op == 2:
        A = A ^ 1
        B = B ^ 1
print(A)
print(B)


#quando A for 0 ela vai virar 1 se for 1 volta a ser 0

# 1 → A = 0 ^ 1 = 1 (acende A)

# 2 → A = 1 ^ 1 = 0, B = 0 ^ 1 = 1

# 2 → A = 0 ^ 1 = 1, B = 1 ^ 1 = 0