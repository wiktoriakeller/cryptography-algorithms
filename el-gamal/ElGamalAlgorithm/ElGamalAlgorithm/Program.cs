using ElGamalAlgorithm;

var algorithm = new ElGamal();

var cipher = algorithm.Encipher("Hello! Have a good day :)");
var plain = algorithm.Decipher(cipher);

Console.WriteLine(plain);
