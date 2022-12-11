namespace RSA;

public interface IKeyGenerator
{
    public Keys GenerateKeys(int size, int? prime1 = null, int? prime2 = null);
}
