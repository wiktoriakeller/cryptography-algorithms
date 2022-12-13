using System.Numerics;
using System.Text;

namespace ElGamalAlgorithm
{
    public class ElGamal
    {
        private int _p = 0;
        private int _g = 0;
        private int _x = 0;
        private BigInteger _y = 0;
        private BigInteger _a = 0;

        public ElGamal()
        {
            var random = new Random();
            _p = 9973;
            _g = 11;
            _x = random.Next(2, _p - 1);
            _y = BigInteger.ModPow(_g, _x, _p);
        }

        public List<BigInteger> Encipher(string message)
        {
            var cipherNumbers = new List<BigInteger>();
            var plainTextBytes = Encoding.ASCII.GetBytes(message);

            var random = new Random();
            var k = random.Next(2, _p - 1);
            _a = BigInteger.ModPow(_g, k, _p);

            for (int i = 0; i < plainTextBytes.Length; i++)
            {
                var number = new BigInteger(plainTextBytes[i]);
                var c = ((number % _p) * BigInteger.ModPow(_y, k, _p)) % _p;
                cipherNumbers.Add(c);
            }

            return cipherNumbers;
        }

        public string Decipher(List<BigInteger> cipher)
        {
            var decipheredText = new StringBuilder();
            var tmp = BigInteger.ModPow(_a, _p - 1 - _x, _p);

            for (int i = 0; i < cipher.Count; i++)
            {
                var m = ((cipher[i] % _p) * (tmp % _p)) % _p;
                decipheredText.Append(Encoding.ASCII.GetString(m.ToByteArray()));
            }

            return decipheredText.ToString();
        }
    }
}
