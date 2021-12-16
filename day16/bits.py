

class BitStream:
    def __init__(self, binary_data):
        self.binary_data = binary_data
        self.pos = 0

    def read(self, n_bits):
        value = self.peek(n_bits)
        self.pos += n_bits
        return value

    @property
    def empty(self):
        return self.pos >= len(self.binary_data) - 1

    def peek(self, n_bits):
        return self.binary_data[self.pos : self.pos + n_bits]

    def __len__(self):
        return len(self.binary_data) - pos

    def __str__(self):
        return self.binary_data[self.pos:]


class BitsParser:

    def __init__(self, binary_data):
        self.binary_data = BitStream(binary_data)
        self.packets = []

    

class Packet:

    def _bin_str_to_int(self, bin_str):
        return int(bin_str, 2)

    def _read_binary_number(self, bitstream):
        result = ""
        while True:
            number = bitstream.read(5)
            result = result + number[1:]
            if number[0] == "0": 
                return result

    @classmethod
    def parse(cls, bitstream):
        version = cls._bin_str_to_int(cls, bitstream.read(3))
        type_id = cls._bin_str_to_int(cls, bitstream.read(3))
        if type_id == 4:
            return LiteralPacket(bitstream, version)
        else:
            return OperatorPacket(bitstream, version, type_id) 


class LiteralPacket(Packet):

    def __init__(self, data, version):
        self.version = version
        self.value = self._bin_str_to_int(self._read_binary_number(data))

    def version_sum(self):
        return self.version


class OperatorPacket(Packet):

    def __init__(self, data, version, type_id):
        self.version = version
        self.type_id = type_id
        self.subpackets = []
        
        length_type = data.read(1)
        if length_type == "0":
            total_sub_bits = self._bin_str_to_int(data.read(15))
            self._parse_constant_width_subpackets(data, total_sub_bits)
        else:
            n_subpackets = self._bin_str_to_int(data.read(11))
            self._parse_n_subpackets(data, n_subpackets)

    def _parse_constant_width_subpackets(self, bitstream, length):
        subpacket_stream = BitStream(bitstream.read(length))
        while not subpacket_stream.empty:
            self.subpackets.append(Packet.parse(subpacket_stream))

    def _parse_n_subpackets(self, bitstream, n):
        for i in range(n):
            self.subpackets.append(Packet.parse(bitstream))

    def version_sum(self):
        return (sum([packet.version_sum() for packet in self.subpackets])
                + self.version)

    @property
    def value(self):
        if self.type_id == 0:
            return sum([packet.value for packet in self.subpackets])
        elif self.type_id == 1:
            product = 1
            for packet in self.subpackets:
                product *= packet.value
            return product
        elif self.type_id == 2:
            return min([packet.value for packet in self.subpackets])
        elif self.type_id == 3:
            return max([packet.value for packet in self.subpackets])
        elif self.type_id == 5:
            return int(self.subpackets[0].value > self.subpackets[1].value)
        elif self.type_id == 6:
            return int(self.subpackets[0].value < self.subpackets[1].value)
        elif self.type_id == 7:
            return int(self.subpackets[0].value == self.subpackets[1].value)
