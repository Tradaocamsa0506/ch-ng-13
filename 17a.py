def primes(n=100):
    prime_list = []
    num = 2
    while len(prime_list) < n:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(num)
        num += 1
    return prime_list
ket_qua = primes()
print(ket_qua)
