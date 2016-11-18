
import math

private_key1 = int(input("Please give first private key: "))
private_key2 = int(input("Please give second private key: "))
encryption_key = int(input("Please give an encryption key: "))


encrypted_message = []


#while math.gcd((private_key1 - 1) * (private_key2 - 1), encryption_key) != 1:
  # encryption_key = input("Invalid input, please give an encryption key: ")


letterDict = {"A": 1,
             "B": 2,
             "C": 3,
             "D": 4,
             "E": 5,
             "F": 6,
             "G": 7,
             "H": 8,
             "I": 9,
             "J": 10,
             "K": 11,
             "L": 12,
             "M": 13,
             "N": 14,
             "O": 15,
             "P": 16,
             "Q": 17,
             "R": 18,
             "S": 19,
             "T": 20,
             "U": 21,
             "V": 22,
             "W": 23,
             "X": 24,
             "Y": 25,
             "Z": 26,
             " ": 27,
             "a": 28,
             "b": 29,
             "c": 30,
             "d": 31,
             "e": 32,
             "f": 33,
             "g": 34,
             "h": 35,
             "i": 36,
             "j": 37,
             "k": 38,
             "l": 39,
             "m": 40,
             "n": 41,
             "o": 42,
             "p": 43,
             "q": 44,
             "r": 45,
             "s": 46,
             "t": 47,
             "u": 48,
             "v": 49,
             "w": 50,
             "x": 51,
             "y": 52,
             "z": 53,
             "0": 54,
             "1": 55,
             "2": 56,
             "3": 57,
             "4": 58,
             "5": 59,
             "6": 60,
             "7": 61,
             "8": 62,
             "9": 63,
             "!": 64,
             "@": 65,
             "#": 66,
             "$": 67,
             "%": 68,
             "^": 69,
             "&": 70,
             "*": 71,
             "(": 72,
             ")": 73}




def number_to_base(n, b):
   if n == 0:
       return [0]
   digits = []
   while n:
       digits.append(int(n % b))
       n /= b
   return digits[::-1]




word_picked = input("Please select a sentence to encrypt: ")


for i in word_picked:
   encrypted_message.append(number_to_base((letterDict[i] ** encryption_key) % (private_key1 * private_key2) + 1, 73))


message = []
for i in encrypted_message:
   for j in i:
       for x in letterDict:
           if letterDict[x] == j:
               message.append(x)
   message.append('~')


for i in message:
   print(i, end='')


