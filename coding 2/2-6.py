for num in range(20,60):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        print(num)

