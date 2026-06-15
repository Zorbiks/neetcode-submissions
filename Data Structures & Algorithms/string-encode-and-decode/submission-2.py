class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for word in strs:
            encoded_str += str(len(word)) + '#' + word
        return encoded_str


    def decode(self, s: str) -> List[str]:
        decoded_msg = []

        while s:
            length = ''
            # getting the length
            while s[0] != '#':
                length += s[0]
                s = s[1:]

            # skipping the seperator '#'
            s = s[1:]
            
            length = int(length)
            decoded_msg.append(s[:length])
            s = s[length:]

        return decoded_msg













