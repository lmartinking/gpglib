from collections import namedtuple

# Information obtained from an OpenPGP header
Tag = namedtuple('Tag', ('version', 'tag_type', 'body_bit_length'))

class Message(object):
    """
        Class to hold details about a message:
            * keys
            * Bytes of original data
            * Results form decrypt process
    """
    def __init__(self, keys, bytes):
        self.keys = keys
        self.bytes = bytes
    
    @property
    def decryptor(self):
        """Memoized PacketParser"""
        if not hasattr(self, 'decryptor'):
            from packet_parser import PacketParser
            self._decryptor = PacketParser(self.keys)
        return self._decryptor
    
    def decrypt(self, region=None):
        """
            Decrypt a message.
            Bytes can be specified to handle nested packets
            Otherwise, defaults to the byte stream on the Message object itself
        """
        if region is None:
            region = self.bytes
        self.decryptor.consume(self, region)
