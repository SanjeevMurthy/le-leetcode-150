"""
Design two functions:
encode(strs) -> string
decode(s) -> list[str]

Where:
Input is a list of strings
encode() converts it into one string
decode() reconstructs the original list exactly

Example
["neet", "code", "love", "you"]

Encoded:
4#neet4#code4#love3#you

Decoded:
["neet", "code", "love", "you"]
"""

def encode(str_list):
    encoded_string = ""
    for ele in str_list:
        encoded_string = encoded_string + ele + '#'
    return encoded_string


def decode(encoded_str):
    sub_str = ""
    decoded_strings = ["*"] * 4 
    ds_index = 0
    for char in encoded_str:
        if char != '#':
            sub_str = sub_str + char
        if char == '#':
            decoded_strings[ds_index] = sub_str
            sub_str = ""
            ds_index += 1
    return decoded_strings


class Codec:

    def encode(self, strs):
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s):
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            res.append(word)
            i = j + 1 + length
        return res
    

str_list = ["neet", "code", "love", "you"]
encoded_string = encode(str_list)
print("Encoded String: {}".format(encoded_string))
print("Decoded list of strings: {}".format(decode(encoded_string)))

codec = Codec()
encoded_string = codec.encode(str_list)
print("Encoded String: {}".format(encoded_string))
print("Decoded list of strings: {}".format(codec.decode(encoded_string)))