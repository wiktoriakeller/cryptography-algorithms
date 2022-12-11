using System.Numerics;

namespace RSA;

public record Keys(BigInteger PublicKey, BigInteger PrivateKey, BigInteger N, BigInteger Prime1, BigInteger Prime2);

public class KeyGenerator : IKeyGenerator
{
    private readonly IPrimesGenerator _primesGenerator;

    public KeyGenerator(IPrimesGenerator generator)
    {
        _primesGenerator = generator;
    }

    public Keys GenerateKeys(int size, int? prime1 = null, int? prime2 = null)
    {
        BigInteger p, q;
        if (prime1 == null || prime2 == null)
        {
            var primes = _primesGenerator.GenerateTwoPrimes(size);
            p = new BigInteger(primes.p);
            q = new BigInteger(primes.q);
        }
        else
        {
            p = new BigInteger((int)prime1);
            q = new BigInteger((int)prime2);
        }

        BigInteger n = p * q;
        BigInteger phi = (p - 1) * (q - 1);

        var publicKey = GenerateCoprimeNumber(phi);
        var privateKey = GeneratePrivateKey(publicKey, phi);
        return new(publicKey, privateKey, n, p, q);
    }

    private BigInteger GenerateCoprimeNumber(BigInteger number)
    {
        BigInteger coprimeNumber = 3;
        var primes = _primesGenerator.GetAllPrimes();
        
        foreach(var prime in primes)
        {
            if(AreCoprime(new BigInteger(prime), number))
            {
                coprimeNumber = prime;
                break;
            }
        }

        return coprimeNumber;
    }

    private bool AreCoprime(BigInteger a, BigInteger b)
    {
        while (a != b)
        {
            if (a > b)
                a -= b;
            else
                b -= a;
        }

        if (a > 1)
            return false;

        return true;
    }

    private BigInteger GeneratePrivateKey(BigInteger e, BigInteger phi)
    {
        var result = GCDExtended(e, phi);
        return phi + result.x;
    }

    private (BigInteger gcd, BigInteger x, BigInteger y) GCDExtended(BigInteger a, BigInteger b)
    {
        if (a == 0)
            return (b, 0, 1);

        var result = GCDExtended(b % a, a);

        var x = result.y - (b / a) * result.x;
        var y = result.x;

        return (result.gcd, x, y);
    }
}
