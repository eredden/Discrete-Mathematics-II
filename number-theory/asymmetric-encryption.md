### INTRODUCTION TO PUBLIC KEY CRYPTOGRAPHY

Private key cryptography, while perfectly secure, can be impractical in everyday use. For example, meeting with an online retailer to agree to a private key for your credit card would be unworkable.

**Public key cryptography relies on two keys for each party -- a public key for encrypting messages, and a private key for decrypting messages.** The recipient's public key is used by anyone to encrypt messages that they would like to send to the recipient. Only the recipient knows their private key, which they can use to decrypt these messages that others have encrypted for them. **Public key cryptosystems rely on two premises: the presumed difficulty of the computation required to decrypt the message and the assumption that there exists no more efficient method to decrypt the ciphertext without knowing the key.**

### GENERATING RSA KEYS

The mostly widely used public key cryptosystem is the **RSA (Rivest, Adelman, and Shamir) cryptosystem.** This method of encryption depends on the difficulty of factoring large numbers. RSA public keys are chosen to be very large (hundreds of digits) prime numbers whose product is nearly impossible to factor (due to time to brute force the answer).

Here is how the preparation of public and private keys works in the RSA cryptosystem:
1. Bob selects two large prime numbers, p and q.
2. Bob computes N = pq and φ = (p-1)(q-1). Note the symbol φ is read Phi.
3. Bob finds an integer e such that gcd(e, φ) = 1.
    - Often a guessed prime number.
4. Bob computes the multiplicative inverse of e mod φ: an integer d such that (ed mod φ) = 1.
    - This involves finding a multiplicative inverse mod through the Extended Euclidean Algorithm.
5. Public (encryption) key: N and e.
6. Private (decryption) key: d.

#### EXAMPLE ONE:
1. For two primes, p = 31 and q = 59:
    - N = pq = 31 * 59 = **1829**
    - φ = (p -1)(q - 1) = 31 * 58 = 1740
2. Find an integer e such that gcd(e, φ) = 1, i.e. find a relatively prime integer.
    - Guess e = **859** and check: gcd(859, 1740) = 1
    - If the first guess is not relatively prime to φ, guess again!
3. Using Euclid's algorithm, find A and B such that A * 859 + B * 1740 = 1.
    - **79** * 859 + (-39) * 1740 = 1
    - **79** * 859 mod 1740 = 1
    - d = 49 is the inverse of 859 mode 1740.
4. The public keys are N = 1829 and e = 859. The private key is d = 79.

#### EXAMPLE TWO:
This was done by me, so the notes here are more brief. The steps are the same as before.
```md
p = 509
q = 733

N = 373097
φ = 371856

# Making up a random guess prime here.
e = 859

# Applying Euclid's algorithm here.
gcd(859, 371856) = 1, see below.

# Converting from [y = qx + r] form to [r = y - qx] form.
371856 mod 859 = 768   ->    768 = 371856 - (432 * 859)
   859 mod 768 = 91    ->     91 = 859 - (1 * 768)
   768 mod  91 = 40    ->     40 = 768 - (8 * 91)
    91 mod  40 = 11    ->     11 = 91 - (2 * 40)
    40 mod  11 = 7     ->      7 = 40 - (3 * 11)
    11 mod   7 = 4     ->      4 = 11 - (1 * 7)
     7 mod   4 = 3     ->      3 = 7 - (1 * 4)
     4 mod   3 = 1     ->      1 = 4 - (1 * 3)
     3 mod   1 = 0

# Now we have to use the Extended Euclidean algorithm.
Find s and t such that:
1  =  se + tφ  =  s * 859 + t * 371856

# I just ended up using an online calculator for this 
# as I didn't want to go through substution hell.
s = 102163
t = -236

# Results are in!
Public keys are N = 373097 and e = 859. The private key is d = 102163.
```

### RSA ENCRYPTION AND DECRYPTION

Thankfully, encrypting and decrypting messages with the RSA cryptosystem is far easier than generating the keys used for these operations. Both formulas are found below.

- c = m<sup>e</sup> mod N, encryption.
    - c = encoded message
    - m = plaintext message
    - e = public key #1
    - N = public key #2
- m = c<sup>d</sup> mod N, decryption.
    - c = encoded message
    - m = plaintext message
    - d = private key
    - N = public key #2

Ex. encrypt the ASCII string "NO" given the public keys N = 373097 and e = 459173.
1. NO = 7879 (78 79) in ASCII.
2. c = 7879<sup>459173</sup> mod 373097.
3. c = 329940
