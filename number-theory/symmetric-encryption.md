### INTRODUCTION TO CRYPTOGRAPHY

 At its most basic level cryptography, or "codes," are messages whose text has been substituted for symbols, other text, or numbers. In modern day cryptographic systems messages are converted to integer values. **Integer m represents the message.**

To ensure accurate sending and receiving of messages, the encryption-decryption process must be one-to- one. That is, for each input there is one and only one output and vice versa. **One-to- one functions map directly to their inverses. Thus, the encryption is a function whose domain (input value) is the characters possible in the message (m), and range (output value) is the set of all ciphertexts, c. Because this function is one-to- one, then the inverse function or decryption function's domain is c and range is m; therefore, mapping the ciphertext back to the correct original plaintext message.**

### ENCRYPTION AND DECRYPTION FUNCTIONS

 **Encrypting a plaintext message requires computing a mathematical function with the integer plaintext m as the input and the ciphertext c as the output.** Decrypting the plaintext therefore is computing the inverse of the encryption process. **Given a ciphertext c, the decryption process must produce the unique plaintext m whose encryption is c.** Suppose that the set of all possible plaintexts comes from a set M, a subset of the integers. Encryption is a function whose domain is M and whose range is C, the set of all ciphertexts.

Consider a simple cryptosystem in which the set of all possible plaintexts come from Z<sub>N</sub> for some integer N, for example N might be 28 if we allow for 26 lower case English characters, a space, and a period. Alice and Bob share a secret number k ∈ Z<sub>N</sub>. The security of their encryption scheme rests on the assumption that no one besides them knows the number k. To encrypt a plaintext m ∈ Z<sub>N</sub>, Alice computes: 

- **c = (m + k) *mod* N, encryption.**
- **m = (c - k) *mod* N, decryption.**

Ex.
1. Alice has a message for Bob!
    1. Alice's message to Bob is **2317**.
    2. The secret key shared by Alice and Bob is 2191.
    3. N (number of possible characters to encode) = 3391. 
2. Alice encrypts the message with her secret key.
    - C = (2317 + 2191) mod 3391 = 1117
3. Bob receives the message and decrypts it.
    - m = (1117 - 2191) mod 3391 = **2317**

This type of encryption scheme is called a symmetric key cryptosystem, as it uses a shared key.

### SYMMETRIC ENCRYPTION SCHEME REQUIREMENTS

If m ≠ m' and m, m' ∈ Z<sub>N</sub> then (m + k) mod N ≠ (m' + k) mod N   (no two distinct plaintexts map to same ciphertext).

If m ∈ Z<sub>N</sub> then (((m + k) mod N)-k) mod N = m   (decryption scheme is inverse of encryption scheme).