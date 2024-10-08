from math import sqrt

#### Fonction secondaire
def isprime(p):
    if p < 2:
        return False
    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True
