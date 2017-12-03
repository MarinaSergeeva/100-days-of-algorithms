import heapq
from functools import total_ordering

@total_ordering
class KeyDict():
    """created to allow using dictionaries as elements in heapq heap"""
    def __init__(self, key, dictionary):
        self.key = key
        self.dictionary = dictionary

    def __lt__(self, other):
        return self.key < other.key

    def __eq__(self, other):
        return self.key == other.key

    def __repr__(self):
        return '{0.__class__.__name__}(key={0.key}, dictionary={0.dictionary})'.format(self)

class HuffmanCodes:
    """created huffman code encoding from dictionary with elements and their frequencies"""
    def __init__(self, frequencies):
        self.encoding_dict = self.get_encodings(frequencies)
        self.decoding_dict = {code:symbol for symbol, code in self.encoding_dict.items()}

    @staticmethod
    def get_encodings(frequencies):
        heap_nodes = [KeyDict(frequency, {symbol: ""}) for symbol, frequency in frequencies.items()]
        heapq.heapify(heap_nodes)
        while len(heap_nodes) > 1:
            node0 = heapq.heappop(heap_nodes)
            node1 = heapq.heappop(heap_nodes)
            for key in node0.dictionary:
                node0.dictionary[key] = "0" + node0.dictionary[key]
            for key in node1.dictionary:
                node1.dictionary[key] = "1" + node1.dictionary[key]
            merged_node = KeyDict(node0.key + node1.key, {**node0.dictionary, **node1.dictionary})
            heapq.heappush(heap_nodes, merged_node)
        return heap_nodes[0].dictionary

    def encode(self, sequence):
        encoded_sequence = []
        for symbol in sequence:
            if symbol in self.encoding_dict:
                encoded_sequence.append(self.encoding_dict[symbol])
            else:
                raise ValueError("Unknown symbol: {0}".format(symbol))
        return "".join(encoded_sequence)

    def decode(self, sequence):
        decoded_sequence = []
        start = 0
        for end in range(1, len(sequence) + 1):
            if sequence[start:end] in self.decoding_dict:
                decoded_sequence.append(self.decoding_dict[sequence[start:end]])
                start = end
        if start != len(sequence):
            raise ValueError("Cannot decode subsequence: {0}".format(sequence[start:]))
        return "".join(decoded_sequence)

    def __repr__(self):
        return '{0.__class__.__name__}(encoding_dict={0.encoding_dict}, decoding_dict={0.decoding_dict})'.format(self)

def test_huffman_codes():
    frequencies0 = {"a": 0.7, "b": 0.07, "c": 0.05, "d": 0.05}
    my_huffman_codes = HuffmanCodes(frequencies0)
    test_sequence = "aaabcdd"
    encoded_test_sequence = my_huffman_codes.encode(test_sequence)
    assert encoded_test_sequence == "11100010011011"
    assert my_huffman_codes.decode(encoded_test_sequence) == test_sequence

if __name__ == "__main__":
    test_huffman_codes()
