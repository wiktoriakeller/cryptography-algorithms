namespace RSA;

public class PrimesGenerator : IPrimesGenerator
{
    private List<int> _primes = new List<int>();

    public (int p, int q) GenerateTwoPrimes(int size)
    {
        EratostenesSieve(size);
        int p = -1;
        int q = -1;

        for(int i = _primes.Count - 1; i >= 0; i--)
        {
            if(p == - 1)
            {
                p = _primes[i];
            }
            else
            {
                q = _primes[i];
                break;
            }
        }

        return (p, q);
    }

    public List<int> GetAllPrimes()
    {
        return _primes;
    }

    private void EratostenesSieve(int size)
    {
        var table = new bool[size];
        Array.Fill(table, true);
        _primes.Clear();

        for (int i = 2; i <= Math.Sqrt(table.Length); i++)
        {
            if (table[i] == true)
            {
                for (int j = i * i; j < table.Length; j += i)
                {
                    table[j] = false;
                }
            }
        }

        for(int i = 2; i < table.Length; i++)
        {
            if(table[i] == true)
                _primes.Add(i);
        }
    }
}
