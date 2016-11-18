import math


from decimal import Decimal


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

def decrypt(dKey, pKey, m):
    x = bin(dKey)
    xList = []
    counter = 0

    for i in x[::-1]:
        if(i == 'b'):
            break
        elif(counter != 0):
            m = (m ** 2) % pKey
        if(i == '1'):
            xList.append(m)
        counter += 1

    y = 1
    for i in xList:
        y *= i
        y = y % pKey
    return y


def decrypt_message(encrypt_message, e, p, q):
   public_key = p * q
   pq = (p - 1) * (q - 1)
   pq1 = pq + 1
   flag = True
   decrypted_message = []


   while flag:
       if pq1 % e == 0:
           d = int(pq1 / e)
           flag = False
       else:
           pq1 += pq


   current_value = []
   compress = []


   for letters in encrypt_message:
       counter = 0


       if letters != '~':
           current_value.append(letters)
       else:
           counter_base = len(current_value) - 1
           for x in current_value:
               counter += letterDict[x] * (73 ** counter_base)
               counter_base -= 1
           compress.append(counter - 1)
           current_value = []
   for nums in compress:
       decrypted_message.append(decrypt(d,public_key,nums))
   message = []
   for i in decrypted_message:
       for x in letterDict:
           if i == letterDict[x]:
               message.append(x)


   for i in message:
       print(i, end='')








decrypt_message("g3rIP~aYzJ8~ABmCtl~ABmCtl~gLcei~cVUIu~yMr&Z~gLcei~AA&ZZn~ABmCtl~IoOZ1~!eQM8~", 39581, 9833, 238801)







