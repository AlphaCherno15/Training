import time
number = 0
target = 155500
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            # print(num % i)
            return False
    else:
        # print(num)
        return True

def calc():
    global target, number
    prime_list = ["", "", "", "", ""]
    while target > 0:
        prime = is_prime(number)
        if prime is True:
            prime_list.append(number)
            prime_list.remove(prime_list[0])
        number += 1
        target -= 1
    return prime_list
start = time.time()
print(calc())
end = time.time()
print(f"For loop time: {end - start:.4f} seconds")