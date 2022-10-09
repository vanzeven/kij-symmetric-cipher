from Algorithms.Algorithm import Algorithm

# Reference: https://www.geeksforgeeks.org/data-encryption-standard-des-set-1/

class DES(Algorithm):
    def __init__(self):
        self.debugMode = False

        self.ipBox = [ 58, 50, 42, 34, 26, 18, 10, 2,
                      60, 52, 44, 36, 28, 20, 12, 4,
                      62, 54, 46, 38, 30, 22, 14, 6,
                      64, 56, 48, 40, 32, 24, 16, 8,
                      57, 49, 41, 33, 25, 17, 9,  1,
                      59, 51, 43, 35, 27, 19, 11, 3,
                      61, 53, 45, 37, 29, 21, 13, 5,
                      63, 55, 47, 39, 31, 23, 15, 7 ]

        self.fpBox = [ 40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
                        38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
                        36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
                        34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25 ]

        self.sBox = [
            [ 2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9 ],
            [ 14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6 ],
            [ 4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14 ],
            [ 11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]
        ]

        self.pBox = [
            16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
            2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25
        ]

    def encrypt(self, plaintext, key):
        # 64 bit
        # 8 character
        # 8-bit per character

        if len(plaintext) != 8:
            print('Plaintext Must be 64-bit')
            return None

        if len(key) != 8:
            print('Key Must be 64-bit')
            return None
            
        ipText = self.initialPermutation(plaintext)

        processedText = ipText

        for roundNumber in range(1, 16 + 1):
            lpt = processedText[:32]
            rpt = processedText[32:]

            processedText = self.xorSwap(lpt, rpt, key, roundNumber)

        cipherBinary = self.finalPermutation(processedText)
        ciphertext = self.bin2string(cipherBinary)

        # print(self.bin2string(lpt))
        # print(self.bin2string(rpt))

        # keyReduce = self.keyReduction(key)
        # print(keyReduce)

        # keyTransform = self.keyTransformation(keyReduce)
        # print(keyTransform)

        # print('Expansion Permutation:')
        # print(self.expansionPermutation('ABCDEFGHIJKLMNOPQRSTUVWXYZ123456'))
        # print(len(self.expansionPermutation('ABCDEFGHIJKLMNOPQRSTUVWXYZ123456')))

        return ciphertext

    def decrypt(self, ciphertext, key):
        pass

    def initialPermutation(self, plaintext):
        originalText = self.string2bin(plaintext)
        originalArray = list(originalText)
        permutatedArray = list(originalText)

        for i in range(64):
            swapIndex = self.ipBox[i] - 1
            permutatedArray[i] = originalArray[swapIndex]

        permutatedText = ''.join(permutatedArray)

        return permutatedText

    def finalPermutation(self, plaintext):
        originalText = self.string2bin(plaintext)
        originalArray = list(originalText)
        permutatedArray = list(originalText)

        for i in range(64):
            swapIndex = self.fpBox[i] - 1
            permutatedArray[i] = originalArray[swapIndex]

        permutatedText = ''.join(permutatedArray)

        return permutatedText

    def keyReduction(self, key):
        # transform 64-bit key into 56-bit by discarding every 8-th bit of the original key
        bin64BitKey = self.string2bin(key)
        bin56BitKey = ''

        for i in range(0, 64):
            if i % 8 == 0:
                continue
            bin56BitKey += bin64BitKey[i]

        return bin56BitKey

    def keyTransformation(self, key, roundNumber):
        leftKey = key[:28]
        rightKey = key[28:]

        leftKey = self.keyTransformationShift(leftKey, roundNumber)
        rightKey = self.keyTransformationShift(rightKey, roundNumber)

        shiftedKey = leftKey + rightKey

        return shiftedKey

    def keyTransformationShift(self, halfKey, roundNumber):
        numberOfShift = 0
        if roundNumber in [ 1, 2, 9, 16 ]:
            numberOfShift = 1
        else:
            numberOfShift = 2

        shiftedKey = self.stringLeftShift(halfKey, numberOfShift)

        return shiftedKey

    def compressionPermutation(self, shiftedKey):
        # 56-bit key into 48-bit key
        compressedKey = ''

        for i in range(56):
            if (i + 1) in [ 9, 18, 22, 25, 35, 38, 43, 54 ]:
                continue
            compressedKey += shiftedKey[i]

        return compressedKey
    
    def expansionPermutation(self, rpt):
        # 32-bit rpt into 48-bit string
        rptArray = list(rpt)
        expansionArray = list('x' * 48)

        for i in range(8):
            for j in range(4):
                targetIndex = i * 6 + j + 1
                sourceIndex = i * 4 + j

                expansionArray[targetIndex] = rptArray[sourceIndex]

                if j == 0:
                    expansionArray[(targetIndex + 48 - 2) % 48] = rptArray[sourceIndex]
                elif j == 3:
                    expansionArray[(targetIndex + 48 + 2) % 48] = rptArray[sourceIndex]

        expansionText = ''.join(expansionArray)

        return expansionText

    def getSBox(self, sixBitBinary):
        # 6-bit binary to sBox value

        row = sixBitBinary[0] + sixBitBinary[5]
        column = sixBitBinary[1:5]

        rowIndex = int(self.bin2char(row))
        columnIndex = int(self.bin2char(column))

        return self.sBox[rowIndex][columnIndex]

    def sBoxSubtitution(self, xoredRptKey):
        # 48-bit into 32-bit

        result = ''

        for i in range(0, 48, 6):
            sixBitBinary = xoredRptKey[i:i + 6]
            sBoxOutput = self.getSBox(sixBitBinary)

            eightBits = self.int2bin(sBoxOutput)
            truncatedBits = eightBits[4:]

            result += truncatedBits

        return result

    def pBoxPermutation(self, sBoxedBinary):
        resultArray = list('x' * 32)

        for i in range(32):
            sBoxIndex = self.pBox[i] - 1
            resultArray[i] = sBoxedBinary[sBoxIndex]

        result = ''.join(resultArray)

        return result

    def xorSwap(self, lpt, rpt, key, roundNumber):
        self.debug('Round Number: ', roundNumber)

        reducedKey = self.keyReduction(key) # 64-bit to 56-bit
        self.debug('Reduced Key: ', reducedKey)

        transformedKey = self.keyTransformation(reducedKey, roundNumber) # 56-bit shifted
        self.debug('Transformed Key: ', transformedKey)

        compressedKey = self.compressionPermutation(transformedKey) # 56-bit shifted to 48-bit shifted
        self.debug('Compressed Key: ', compressedKey)

        expandedRpt = self.expansionPermutation(rpt) # 32-bit to 48-bit
        self.debug('Expanded RPT: ', expandedRpt)

        outputRpt = self.xorBin(expandedRpt, compressedKey) # 48-bit xored rpt and key
        self.debug('Output RPT: ', outputRpt)

        sBoxedOutputRpt = self.sBoxSubtitution(outputRpt) # 48-bit to 32-bit
        self.debug('S-BOXed Output RPT: ', sBoxedOutputRpt)

        pBoxedOutputRpt = self.pBoxPermutation(sBoxedOutputRpt) # 32-bit permutation
        self.debug('P-BOXed Output RPT: ', pBoxedOutputRpt)

        finalLpt = rpt
        finalRpt = self.xorBin(lpt, pBoxedOutputRpt)

        self.debug('Final LPT: ', finalLpt)
        self.debug('Final RPT: ', finalRpt)

        finalString = finalLpt + finalRpt

        self.debug('Final String: ', finalString)

        self.debug()

        return finalString

    def string2bin(self, string):
        result = ''
        for c in string:
            result += self.char2bin(c)
        return result

    def char2bin(self, char):
        return self.int2bin(ord(char))

    def int2bin(self, integer):
        return bin(integer)[2:].zfill(8)

    def bin2char(self, binaryChar):
        return int(binaryChar, 2)

    def bin2string(self, binaryString):
        result = ''
        for i in range(0, 64, 8):
            binaryChar = binaryString[i:i+8]

            if binaryChar == '':
                continue

            integerChar = self.bin2char(binaryChar)
            char = chr(integerChar)
            result += char
        return result

    def stringLeftShift(self, string, iteration):
        result = string

        for i in range(iteration):
            leftMostChar = result[0]
            result = result[1:]
            result += leftMostChar

        return result

    def xorBin(self, binA, binB):
        minLen = min(len(binA), len(binB))

        result = ''

        for i in range(minLen):
            result += str(int(binA[i]) ^ int(binB[i]))
        
        return result    
        
    def setDebug(self, active):
        self.debugMode = active

    def debug(self, *string):
        if self.debugMode:
            print(string)