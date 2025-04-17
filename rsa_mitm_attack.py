import math
from collections import defaultdict

def rsa_encrypt(m, e, n):
    return pow(m, e, n)

def meet_in_the_middle_attack(c, e, n, m_bits=40):
    """
    Perform the Meet-in-the-Middle attack on RSA.
    Assumes m = m1 * m2 where m1 and m2 are m_bits//2-bit integers.
    """
    m1_bits = m2_bits = m_bits // 2
    max_m1 = 2 ** m1_bits
    max_m2 = 2 ** m2_bits

    print(f"[*] Generating lookup table for m1 in range 0 to {max_m1 - 1}")
    table = defaultdict(list)
    for m1 in range(1, max_m1):
        val = pow(m1, e, n)
        table[val].append(m1)

    print(f"[*] Trying all values of m2 from 1 to {max_m2 - 1}")
    for m2 in range(1, max_m2):
        try:
            m2e = pow(m2, e, n)
            m2e_inv = pow(m2e, -1, n)  
            target = (c * m2e_inv) % n

            if target in table:
                for m1 in table[target]:
                    recovered = m1 * m2
                    if rsa_encrypt(recovered, e, n) == c:
                        return recovered, m1, m2
        except ValueError:
            continue  

    return None, None, None

def demo():
    print("[+] Demo of Meet-in-the-Middle RSA Attack")
    p = 1278377
    q = 1299721
    n = p * q
    e = 65537
    m1 = 12345
    m2 = 67890
    m = m1 * m2
    c = rsa_encrypt(m, e, n)

    print(f"[*] Encrypted message: {c}")

    recovered, r1, r2 = meet_in_the_middle_attack(c, e, n, m_bits=40)
    if recovered:
        print(f"[+] Success! Recovered message: {recovered} = {r1} * {r2}")
    else:
        print("[-] Attack failed.")

if __name__ == "__main__":
    demo()
