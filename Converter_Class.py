#!/usr/bin/python3
# Script for converting arabic to roman numerals and vice versa

from Valid_Class import Checkforclass

class Romanconverter(object):
    """Contains methods for converting Arabic numbers to Roman numerals and vice versa. The list of Roman Numerals is customisable and can be defined on creation of object in the arguments as a list. i.e. change the letters or add more. Default limit is 1000; can go higher but results in uncertainties."""
    roman_list = ["I","V","X","L","C","D","M"]
    number_list = []

    def __init__(self, rom_list = roman_list):
        super(Romanconverter, self).__init__()
        self.roman_list = rom_list

        self.number_list = []
        n = 1
        for i, r in enumerate(self.roman_list):
            if i % 2 == 0:
                self.number_list.append(n)
                n = n*5
            else:
                self.number_list.append(n)
                n = n*2

    def print_lists(self):
        """Print the list of latters and numbers associated with this object."""
        print(f"{self.roman_list}\n{self.number_list}")

    def rom_to_num(self, rom_Num):
        """Accepts Roman numerals as input, checks that they are in the correct format, otherwise raises an error, and converts them into an Arabic number."""
        int = 0
        f = 0
        while int < len(rom_Num):
            t = self.roman_list.index(rom_Num[int])
            #print(int, rom_Num[int], self.number_list[t])
            v = self.number_list[t]
            if int + 1 < len(rom_Num):
                if t + 1 < len(self.roman_list) and rom_Num[int+1] == self.roman_list[t+1]:
                    v = self.number_list[t+1] - self.number_list[t]
                    #print(v)
                    int += 1
                elif t + 2 < len(self.roman_list) and rom_Num[int+1] == self.roman_list[t+2]:
                    v = self.number_list[t+2] - self.number_list[t]
                    #print(v)
                    int += 1
                elif rom_Num[int] == rom_Num[int+1]:
                    v = 2*self.number_list[t]
                    #print(v)
                    int += 1
                    if int + 1 < len(rom_Num):
                        if rom_Num[int] == rom_Num[int+1]:
                            v = 3*self.number_list[t]
                            #print(v)
                            int += 1
                            if int + 1 < len(rom_Num):
                                if rom_Num[int] == rom_Num[int+1]:
                                    return f"Error: Number format is incorrect. Too many of the same character in a row: {rom_Num[int]}"
                #else
                #    return "Error: Number format is incorrect."
            if v > f and f != 0:
                return "Error: Number format is incorrect. Check the ordering of the letters"
            else:
                f += v
            int += 1
        return f

    def num_to_rom(self, num):
        """Accepts input of an Arabic number and converts it to Roman Numerals."""
        num_string = str(num)
        rom = ""
        i = 0
        while i < len(num_string):
            num_i = int(num_string[i] + "0"*(len(num_string)-1-i))
            #print(num_i)
            k = 0
            if num_i == 0:
                pass
            elif num_i > self.number_list[-1]:
                #Print("Test: 2")
                rom += self.roman_list[-1]*(int(str(num_i - self.number_list[-1]).replace("0", "")) + 1)
                print("Error: Possible overflow of known Roman Numerals")
            else:
                #Print("Test: 3")
                while k < len(self.number_list):
                    if self.number_list[k] == num_i:
                        #Print("Test: 4", self.number_list[k])
                        rom += self.roman_list[k]
                        break
                    elif k + 1 < len(self.number_list) and self.number_list[k] < num_i < self.number_list[k+1]:
                        #Print("Test: 5", self.number_list[k])
                        if k % 2 == 0:
                            #Print("Test: 6", self.number_list[k])
                            if num_i > int("3" + "0"*(len(num_string)-1-i)):
                                #Print("Test: 7", self.number_list[k], 3*(10**(len(num_string)-1-i)))
                                rom += self.roman_list[k] + self.roman_list[k+1]
                                break
                            else:
                                #Print("Test: 8", self.number_list[k], 3*(10**(len(num_string)-1-i)))
                                rom += self.roman_list[k]*(int(str(num_i - self.number_list[k]).replace("0", "")) + 1)
                                break
                        else:
                            #Print("Test: 9", self.number_list[k])
                            if num_i > self.number_list[k] + int("3" + "0"*(len(num_string)-1-i)):
                                #Print("Test: 10", self.number_list[k])
                                rom += self.roman_list[k-1] + self.roman_list[k+1]
                                break
                            else:
                                #Print("Test: 11", self.number_list[k])
                                rom += self.roman_list[k] + self.roman_list[k-1]*int(str(num_i - self.number_list[k]).replace("0", ""))
                                break
                    k += 1
                #print(rom)
            i += 1
        return rom

    def test_full(self):
        """Print a test set of numbers to check the functionality of the class."""
        print()
        for testNum in [i for i in range(0, 1000)]:
            testRom = self.num_to_rom(testNum)
            retNum = self.rom_to_num(testRom)
            print(f"{testNum} == {testRom}:\t{testNum == retNum}\t{testRom} == {retNum}")

    def num_or_rom(self):
        """Checks which converter method to use, then uses it."""
        while True:
            userinput = input(": ").strip()
            if userinput == "q":
                print("\n\tThanks for using Roman Numeral Converter 2.02 revision 9\n\tGoodbye\n")
                quit()
            elif userinput.isdigit():
                print(self.num_to_rom(int(userinput)))
            elif Checkforclass("".join(self.roman_list)).check_all(userinput):
                print(self.rom_to_num(userinput.upper()))

    def convert(self):
        self.print_lists()
        self.num_or_rom()
