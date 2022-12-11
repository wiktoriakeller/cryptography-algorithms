namespace RSA;

public interface IPrimesGenerator
{
    public (int p, int q) GenerateTwoPrimes(int size);
    public List<int> GetAllPrimes();
}
