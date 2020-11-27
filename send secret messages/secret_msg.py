""" Send secret messages to Crush
 that her father won't be able to understand.

 Cryptography with Python.

 author: ashraf minhaj
 mail: ashraf_minhaj@yahoo.com
"""

"""
install:
$ pip install caesarcipher
"""

from caesarcipher import CaesarCipher

# what you will do
cipher = CaesarCipher('Baby I Love you', offset=4)
print(cipher.encoded)
# output - "Fefc M Pszi csy"

# what your gf will do
print(cipher.decoded)
# output - "Baby I Love you"