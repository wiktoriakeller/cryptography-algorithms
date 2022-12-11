using System.Text;
using System.Numerics;

namespace RSA;

public class RSAAlgorithm
{
    public string Cipher { get; private set; } = string.Empty;
    public string PlainText { get; private set; } = string.Empty;
    private readonly IKeyGenerator _keyGenerator;
    private Keys _keys;
    private int _expectedLength;

    public RSAAlgorithm(IKeyGenerator keyGenerator)
    {
        _keyGenerator = keyGenerator;
        _keys = new(1, 1, 1, 1, 1);
    }

    public List<BigInteger> Encipher(string plainText, int size)
    {
        var cipherNumbers = new List<BigInteger>(size);
        var plainTextBytes = Encoding.ASCII.GetBytes(plainText);
        var chunks = 3;
        var addedPadding = chunks - (plainTextBytes.Length % chunks);
        _expectedLength = plainTextBytes.Length;

        if (addedPadding > 0)
        {
            byte[] randomByte = new byte[addedPadding];
            var random = new Random();
            random.NextBytes(randomByte);
            Array.Resize(ref plainTextBytes, plainTextBytes.Length + addedPadding);

            for (int i = _expectedLength; i < plainTextBytes.Length; i++)
                plainTextBytes[i] = randomByte[i - _expectedLength];
        }

        _keys = _keyGenerator.GenerateKeys(size);
        for (int i = 0; i < plainTextBytes.Length; i+= chunks)
        {
            int combined = 0;

            for(int j = (i + chunks) - 1; j >= i; j--)
                combined = combined << 8 | plainTextBytes[j];

            var number = new BigInteger(combined);
            var c = BigInteger.ModPow(number, _keys.PublicKey, _keys.N);
            cipherNumbers.Add(c);
        }
        
        Cipher = string.Join("", cipherNumbers.ToArray());
        return cipherNumbers;
    }
    
    public string Decipher(List<BigInteger> cipher)
    {
        var decipheredText = new StringBuilder();
        for (int i = 0; i < cipher.Count; i++)
        {
            var m = BigInteger.ModPow(cipher[i], _keys.PrivateKey, _keys.N);
            decipheredText.Append(Encoding.ASCII.GetString(m.ToByteArray()));
        }

        PlainText = decipheredText.ToString().Substring(0, _expectedLength);
        return decipheredText.ToString();
    }

    private int Combine(byte b1, byte b2)
    {
        int combined = b1 << 8 | b2;
        return combined;
    }

    private int CombineMultiple(params byte[] bytes)
    {
        int combined = 0;
        foreach(var b in bytes)
            combined = combined << 8 | b;

        return combined;
    }
}
