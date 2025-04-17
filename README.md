# Meet-in-the-Middle Attack on Textbook RSA

This project demonstrates a **Meet-in-the-Middle attack** on textbook RSA encryption, based on Section 5 of the paper:
**"Why Textbook ElGamal and RSA Encryption Are Insecure" by Boneh, Joux, and Nguyen (2000).**

## 🔒 Description
The attack targets short encrypted messages (e.g., session keys) in RSA systems that use no padding.

RSA encrypts a message `M` as:
```
    C = M^e mod N
```

If `M` is small (e.g., 40-bit), it can be factored into two smaller numbers:
```
    M = M1 * M2
```
Using precomputation and a clever lookup method, this attack finds such factors much faster than brute-force.

## 📂 Files
- `rsa_mitm_attack.py`: Python implementation of the attack
- `README.md`: This file

## ▶️ How to Run
Make sure you have Python 3 installed. Then run:
```bash
python rsa_mitm_attack.py
```
You should see output that looks like:
```
[+] Demo of Meet-in-the-Middle RSA Attack
[*] Encrypted message: 123456789...
[*] Generating lookup table for m1 in range 0 to 1048575
[*] Trying all values of m2 from 1 to 1048575
[+] Success! Recovered message: 838102050 = 12345 * 67890
```

## ⚙️ How It Works
1. The original message `M` is a product of two smaller integers `M1` and `M2`.
2. The attacker precomputes a table of `M1^e mod N` for all possible `M1`.
3. For every possible `M2`, it computes:
   ```
   target = C / (M2^e) mod N
   ```
   and checks if that value is in the table.
4. When a match is found, the original message is recovered as `M1 * M2`.

## 📌 Limitations
- Only works on short messages (e.g., up to 40 bits).
- Assumes textbook RSA (no padding like OAEP).
- This is for educational/demo purposes only. Do not use small RSA key sizes in real life.

## 🧠 References
- Boneh, Joux, Nguyen (2000). *Why Textbook ElGamal and RSA Encryption Are Insecure*. [ASIACRYPT 2000]
- [RSA Algorithm - Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

## 🧪 Example Parameters Used in Demo
- `e = 65537` (common RSA exponent)
- `n = p * q` where p and q are small primes (about 21 bits)
- `m1 = 12345`, `m2 = 67890`, `m = m1 * m2`

## ✅ Output
The script will tell you if it successfully recovered the original message and display its factors.

---
Authors: Mereke Daurenbek, Dias Omarov | Implemented in Python 🐍

