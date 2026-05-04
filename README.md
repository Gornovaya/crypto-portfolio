# crypto-portfolio
Cryptography portfolio: GCD/LCM, extended Euclidean, primality sieves, Fermat factorization, Euler's totient, modular inverse, CRT, primitive roots, Legendre/Jacobi symbols, group decomposition (Z/mZ, Z/mZ*), polynomials over GF(p), elliptic curves over prime fields, Montgomery multiplication, Pepin's test.

Educational project — implementations of fundamental cryptographic and number-theoretic algorithms.

**Algorithms Implemented:**␣␣  

| Algorithm | Task |
|:--------|:--------:|--------------:|
| 1	LCM (Least Common Multiple) |
| 2	GCD & Extended Euclidean Algorithm (linear decomposition) |
| 3	Prime number generation — Sieve of Eratosthenes & Sundaram |
| 4	Fermat factorization (canonical prime decomposition) |
| 5	Euler's totient function φ(m) |
| 6	Modular inverse in ℤ/mℤ |
| 7	Solving linear congruences (prime & composite modulus) |
| 8	Chinese Remainder Theorem (CRT) solver |
| 9	Fast modular exponentiation aᵏ mod m (Fermat's little theorem for prime m, CRT for composite m) |
| 10	Primitive root (generator) + reduced residue system |
| 11	Solving exponential congruences |
| 12	Legendre & Jacobi symbols |
| 13	Orders of all elements in ℤ/mℤ (additive & multiplicative groups) |
| 14	Group decomposition into subgroups + cosets (for both ℤ/mℤ and (ℤ/mℤ)×) |
| 15	Polynomials over GF(p) — GCD & linear decomposition |
| 16	Finite field GF(2ⁿ) construction — Cayley tables for addition & multiplication |
| 17	Elliptic curves over prime fields: order of curve, order of a point, formulas for 𝔽(pʳ) |
| 18	Pseudorandom sequence generator (with parameter justification for maximal period) |
| 19	Montgomery multiplication & exponentiation |
| 20	Pépin's test (Fermat primality test) |

**Requirements:**␣␣
Python 3.8+.
No external dependencies are strictly required for most algorithms.
Optional (for symbolic polynomial operations in tasks 16–17, but the repository contains pure Python fallbacks where possible):
```bash
pip install sympy
```

**RUN:**␣␣ 
1. Clone the repository

```bash
git clone https://github.com/Gornovaya/cryptography-portfolio.git
cd cryptography-portfolio
```

3. Run any script directly
```bash
python 01_lcm_gcd.py   # example
```

5. Follow the console prompts — each script asks for necessary inputs (numbers, modulus, etc.) and prints intermediate steps.


**Project Structure:**␣␣  
cryptography-portfolio/␣␣  
├── labs␣␣  
├── docx␣␣  
├── README.md␣␣  
└── LICENSE␣␣  
