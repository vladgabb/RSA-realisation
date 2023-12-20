import random


def rabinMiller(n, d):
    a = random.randint(2, (n - 2) - 2)
    x = pow(a, int(d), n) 
    if x == 1 or x == n - 1:
        return True

    while d != n - 1:
        x = pow(x, 2, n)
        d *= 2

        if x == 1:
            return False
        elif x == n - 1:
            return True
    
    return False

def isPrime(n):


    if n < 2:
        return False

    
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1001, 1003]


    if n in lowPrimes:
        return True

    for prime in lowPrimes:
        if n % prime == 0:
            return False
    
    c = n - 1 
    while c % 2 == 0:
        c /= 2 

    
    for i in range(128):
        if not rabinMiller(n, c):
            return False

    return True

def generateKeys(keysize=1024):
    e = d = N = 0


    p = generateLargePrime(keysize)
    q = generateLargePrime(keysize)

    print(f"p: {p}")
    print(f"q: {q}")

    N = p * q 
    phiN = (p - 1) * (q - 1) 


    while True:
        e = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
        if (isCoPrime(e, phiN)):
            break


    d = modularInv(e, phiN)

    return e, d, N

def generateLargePrime(keysize):

    while True:
        num = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
        if (isPrime(num)):
            return num

def isCoPrime(p, q):

    return gcd(p, q) == 1

def gcd(p, q):

    while q:
        p, q = q, p % q
    return p

def egcd(a, b):
    s = 0; old_s = 1
    t = 1; old_t = 0
    r = b; old_r = a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t

def modularInv(a, b):
    gcd, x, y = egcd(a, b)

    if x < 0:
        x += b

    return x

def exponentiation_and_mod(a, b, n):
    b_mas = []
    while b > 0:
        b_mas.append((b % 2))
        b = b // 2
    b_mas.reverse()
    c = a

    for i in range(1, len(b_mas)):
        if (b_mas[i] == 0):
            c = (c ** 2) % n
        else:
            c = (c ** 2) * a % n
    return c

def encrypt(e, N, msg):
    cipher = ""

    for c in msg:
        m = ord(c)
        cipher += str(pow(m, e, N)) + " "

    return cipher

def decrypt(b, N, cipher):
    msg = ""

    parts = cipher.split()
    for part in parts:
        if part:
            c = int(part)
            msg += chr(pow(c, b, N))

    return msg

def main():
    keysize = 32

    e, d, N = generateKeys(keysize)
    with open("rsa_results.txt", "r") as msg_file:
        msg = msg_file.read()
    print(f"m:{msg}")
    
    

    enc = encrypt(e, N, msg)
    dec = decrypt(d, N, enc)


    with open("rsa_results.txt", "w") as file:
        file.write(f"Message: {msg}\n")
        file.write(f"e: {e}\n")
        file.write(f"d: {d}\n")
        file.write(f"N: {N}\n")
        file.write(f"dec: {dec}\n")
        file.write(f"enc: {enc}\n") 
    with open("rsa_results.txt", "r") as file:
        file_contents = file.read()
    print("\nResults from File:\n")
    print(file_contents)


main()
