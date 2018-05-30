#include <stdio.h>
#include <stdlib.h>

typedef unsigned long long uns64;

uns64 modpow(uns64 base, uns64 exp, uns64 modulus) {
  base = base % modulus;
  uns64 result = 1;
  while (exp > 0) {
    if (exp & 1) result = (result * base) % modulus;
    base = (base * base) % modulus;
    exp >>= 1;
  }
  return result;
}

bool is_fermat_pseudoprime(uns64 n) {
    uns64 primes[7] = {2,3,5,7,11,13,17};

    uns64 p;

    for (int i = 0; i < 7; i++) {
        p = primes[i];

        if (n == p) return true;
        if ((n % p) == 0) return false;
        if (modpow(p, n-1, n) != 1) {
            printf("%llu failed for p=%llu\n", n, p);
            return false;
        }
    }

    return true;
}

int main(int argc, char **argv) {
    uns64 top;


    if (argc < 2) {
        top = 50000000;
    } else {
        printf("%llu: %llu\n", atoll(argv[1]), is_fermat_pseudoprime(atoi(argv[1])));
        return 0;

        // top = atoi(argv[1]);
    }

    uns64 v;

    for (uns64 i = 2; i <= top; i++) {
        v = 2*i*i - 1;
        if (is_fermat_pseudoprime(v)) {
            printf("%llu\n",v);
        }
    }

    return 0;
}
