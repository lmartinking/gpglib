from Crypto.PublicKey import RSA

from gpglib.structures import EncryptedMessage, Key

if __name__ == '__main__':
    data = open('tests/data/key.secret.gpg').read()
    key = Key(passphrase='blahandstuff')
    key.consume(data)
    keys = key.key_dict()
    print keys
    
    data = open('tests/data/data.small.dump.gpg').read()
    message = EncryptedMessage(keys)
    message.decrypt(data)

    print "Message successfully decrypted data.dump::"
    print message.plaintext

    data = open('tests/data/data.big.dump.gpg').read()
    message = EncryptedMessage(keys)
    message.decrypt(data)

    print "Message successfully decrypted data.big.dump::"
    print message.plaintext
