import heapq
import os


class binaryTreeNode:
    def __init__(self, value, freq):
        self.freq = freq
        self.value = value
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq


class huffman_Coding:
    def __init__(self, path):
        self.path = path
        self.__heap = []
        self.__code = {}
        self.__reversecode = {}

    @staticmethod
    def __freqCount(text):
        dic = {}
        for char in text:
            if char not in dic:
                dic[char] = 0
            dic[char] += 1
        return dic

    def __heapSort(self, freq_dict):
        for char in freq_dict:
            frequency = freq_dict[char]
            binary_node = binaryTreeNode(char, frequency)
            heapq.heappush(self.__heap, binary_node)

    def __createBinaryTree(self):
        while len(self.__heap) > 1:
            leftNode = heapq.heappop(self.__heap)
            rightNode = heapq.heappop(self.__heap)
            freqValue = leftNode.freq + rightNode.freq
            newNode = binaryTreeNode(None, freqValue)
            newNode.left = leftNode
            newNode.right = rightNode
            heapq.heappush(self.__heap, newNode)
        return

    def __buildCodeHelper(self, root, cur_code):
        if root is None:
            return
        if root.value is not None:
            self.__code[root.value] = cur_code
            self.__reversecode[cur_code] = root.value
            return
        self.__buildCodeHelper(root.left, cur_code + "0")
        self.__buildCodeHelper(root.right, cur_code + "1")

    def __buildCode(self):
        root = heapq.heappop(self.__heap)
        self.__buildCodeHelper(root, "")

    def __encodedTExt(self, text):
        EncodedText = ""
        for char in text:
            EncodedText += self.__code[char]
        return EncodedText

    @staticmethod
    def __paddingEncodedText(encoded_text):
        padding_range = 8 - (len(encoded_text) % 8)
        for i in range(padding_range):
            encoded_text += '0'
        padded_info = "{0:08b}".format(padding_range)
        padded_encoded_text = padded_info + encoded_text
        return padded_encoded_text

    @staticmethod
    def __getBytesArray(padded_encoded_text):
        array = []
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i + 8]
            array.append(int(byte, 2))
        return array

    def compress(self):
        # reading the file path
        file_name, file_extension = os.path.splitext(self.path)
        output_path = file_name + ".bin"
        with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
            # reading the text from the file
            text = file.read()
            text = text.rstrip()
            # counting the frequency in text
            freq_dict = self.__freqCount(text)
            # creating the heap sort from the freq_dict
            self.__heapSort(freq_dict)
            # creating binary tree node from heap sort tree
            self.__createBinaryTree()
            # build the codes for each value in heap
            self.__buildCode()
            # encoding of text
            Encoded_Text = self.__encodedTExt(text)
            # padding encoded text
            padded_encoded_text = self.__paddingEncodedText(Encoded_Text)
            # converting the encoded text into byte code
            bytes_array = self.__getBytesArray(padded_encoded_text)
            finalBytes = bytes(bytes_array)
            output.write(finalBytes)
        print("compressed")
        return output_path

    def __removePadding(self,text):
        padded_info = text[:8]
        extra_padding = int(padded_info,2)
        text = text[8:]
        text_after_padding_removed = text[:-1*extra_padding] # can be done slicing by this aswell len(text)-extra_padding
        return text_after_padding_removed

    def __decodeText(self,text):
        decoded_text = ""
        current_bits = ""
        for bit in text:
            current_bits += bit
            if current_bits in self.__reversecode:
                charcter = self.__reversecode[current_bits]
                decoded_text += charcter
                current_bits = ""
        return decoded_text

    def decompressed(self, initial_path):
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + "_decompressed" + ".txt"
        with open(initial_path, 'rb') as file, open(output_path, 'w') as output:
            bit_string = ""
            byte = file.read(1)
            while byte:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8,'0')
                bit_string += bits
                byte = file.read(1)
            actual_text = self.__removePadding(bit_string)
            decompressed_text = self.__decodeText(actual_text)
            output.write(decompressed_text)
            print("decomprssed")
            return


path = r"C:\Users\papna\Desktop\vivek.txt"
h = huffman_Coding(path)
output_path = h.compress()
print(output_path)
decompressed_path = h.decompressed(output_path)
