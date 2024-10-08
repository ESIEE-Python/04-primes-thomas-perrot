""" Fonction principale Main """ 
from primes import isprime
def main():
    """ Fonction appelée pour calculer un nombre """
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
