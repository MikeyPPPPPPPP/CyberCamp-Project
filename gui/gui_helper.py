class vincipher:
    def __init__(self):
        pass
    def generateKey(self, string, key):
        key = list(key)
        if len(string) == len(key):
            return (key)
        else:
            for i in range(len(string) -
                           len(key)):
                key.append(key[i % len(key)])
        return ("".join(key))

    def cipherText(self, string, key):
        cipher_text = []
        for i in range(len(string)):
            x = (ord(string[i]) +
                 ord(key[i])) % 26
            x += ord('A')
            cipher_text.append(chr(x))
        return ("".join(cipher_text))

    def originalText(self, cipher_text, key):
        orig_text = []
        for i in range(len(cipher_text)):
            x = (ord(cipher_text[i]) -
                 ord(key[i]) + 26) % 26
            x += ord('A')
            orig_text.append(chr(x))

        return ("".join(orig_text))

class rail2:
    def two_rails(self, mes): # 2 rails
        rail1 = []
        rail2 = []
        numset = []
        numset[:0] = mes
        wordlen = len(mes)
        r1 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        for x in range(0, wordlen):
            if x in r1:
                rail1.append(mes[x])
            else:
                rail2.append(mes[x])

        return rail2, rail1

    def evensimsg(self, mes): # 3 rails
        rail1 = []
        rail2 = []
        rail3 = []
        numsret = []
        numsret[:0] = mes
        wordlen = len(mes)
        r1 = [0, 4, 8, 12, 16, 20, 24]
        r2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
        r3 = [2, 6, 10, 14, 18, 22]
        for x in range(0, wordlen):
            if x in r1:
                rail1.append(mes[x])
            elif x in r2:
                rail2.append(mes[x])
            else:
                rail3.append(mes[x])

        return rail1, rail2, rail3

    def the_rail_5(self, mes): # 5 rails
        rail1 = []
        rail2 = []
        rail3 = []
        rail4 = []
        rail5 = []
        numsret = []
        numsret[:0] = mes
        wordlen = len(mes)
        r1 = [0, 8, 16, 24]
        r2 = [1, 7, 9, 15, 17, 23]
        r3 = [2, 6, 10, 14, 18, 22]
        r4 = [3, 5, 11, 13, 19, 21]
        r5 = [4, 12, 20]
        for x in range(0, wordlen):
            if x in r1:
                rail1.append(mes[x])
            elif x in r2:
                rail2.append(mes[x])
            elif x in r3:
                rail3.append(mes[x])
            elif x in r4:
                rail4.append(mes[x])
            else:
                rail5.append(mes[x])

        return rail1, rail2, rail3, rail4, rail5

    def the_rail_4(self, mes): # 4 rails
        rail1 = []
        rail2 = []
        rail3 = []
        rail4 = []
        numsret = []
        numsret[:0] = mes
        wordlen = len(mes)
        r1 = [0, 6, 12, 18, 24]
        r2 = [1, 5, 7, 11, 13, 17, 19, 23]
        r3 = [2, 4, 8, 10, 14, 16, 20, 22]
        r4 = [3, 9, 15, 21]
        for x in range(0, wordlen):
            if x in r1:
                rail1.append(mes[x])
            elif x in r2:
                rail2.append(mes[x])
            elif x in r3:
                rail3.append(mes[x])
            else:
                rail4.append(mes[x])

        return rail1, rail2, rail3, rail4


    def the_rail_help2(self, entry_input, evod): # 3rails
        list1 = []
        list2 = []
        list3 = []
        fulllist = []
        message = entry_input

        for x in evod[0]:
            list1.append(x)

        for x in evod[1]:
            list2.append(x)

        for x in evod[2]:
            list3.append(x)

        for x in list1:
            fulllist.append(x)

        for x in list2:
            fulllist.append(x)

        for x in list3:
            fulllist.append(x)

        str1 = ''.join(str(e) for e in fulllist)
        return(str1)

    def the_rail_help1(self, entry_input, evod):
        list1 = []
        list2 = []
        fulllist = []
        message = entry_input

        for x in evod[0]:
            list1.append(x)

        for x in evod[1]:
            list2.append(x)

        for x in list1:
            fulllist.append(x)

        for x in list2:
            fulllist.append(x)


        str1 = ''.join(str(e) for e in fulllist)
        return (str1)

    def the_rail_help3(self, entry_input, evod):
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        fulllist = []
        message = entry_input

        for x in evod[0]:
            list1.append(x)

        for x in evod[1]:
            list2.append(x)

        for x in evod[2]:
            list3.append(x)

        for x in evod[3]:
            list4.append(x)


        for x in list1:
            fulllist.append(x)

        for x in list2:
            fulllist.append(x)

        for x in list3:
            fulllist.append(x)

        for x in list4:
            fulllist.append(x)


        str1 = ''.join(str(e) for e in fulllist)
        return (str1)

    def the_rail_help4(self, entry_input, evod):
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        fulllist = []
        message = entry_input

        for x in evod[0]:
            list1.append(x)

        for x in evod[1]:
            list2.append(x)

        for x in evod[2]:
            list3.append(x)

        for x in evod[3]:
            list4.append(x)

        for x in evod[4]:
            list4.append(x)


        for x in list1:
            fulllist.append(x)

        for x in list2:
            fulllist.append(x)

        for x in list3:
            fulllist.append(x)

        for x in list4:
            fulllist.append(x)

        for x in list5:
            fulllist.append(x)

        str1 = ''.join(str(e) for e in fulllist)
        return (str1)


    # rout cipher is added here
    """
    message = "michael michael "  # "michael michael micheal p:" 16 works with 16 charectors # 9 works"e te tess"
    """
    def get_process(self, Mes):
        Message = Mes.replace(" ", "x")

        get_len = len(Message)
        if get_len <= 9:
            a = self.route_9(Message)
        elif get_len <= 16:
            a = self.route_16(Message)
        elif get_len <= 26:
            a = self.route_26(Message)

    def route_9(self, mess):
        combined_list = []
        row1 = []
        row2 = []
        row3 = []
        number = []
        number[:0] = mess

        wordlen_route9 = len(mess)
        ro1 = [0, 7, 6]
        ro2 = [1, 8, 5]
        ro3 = [2, 3, 4]
        for x in range(0, 5):  # wordlen_route9):
            if x in ro1:
                if mess[x] == " ":
                    print("row 1", mess[x])  # for debbuging
                    row1.append("x")
                else:
                    # print("row 1", mess[x])  # for debbuging
                    row1.append(mess[x])
            elif x in ro2:
                if mess[x] == " ":
                    print("row 2", mess[x])  # for debbuging
                    row2.append("x")
                else:
                    # print("row 2", mess[x])  # for debbuging
                    row2.append(mess[x])
            else:
                if mess[x] == " ":
                    print("row 3", mess[x])  # for debbuging
                    row3.append("x")
                else:
                    # print("row 3", mess[x])  # for debbuging
                    row3.append(mess[x])

        for x in range(6, 7):
            f = ''
            if mess[x] == 'x':
                row1.append(mess[x])
                row1.append(mess[x + 1])
            else:
                row1.append(mess[x + 1])
                row1.append(mess[x])
        row2.append(mess[8])
        row2.append(mess[5])

        print(row1)
        print(row2)
        print(row3)
        for x in row1:
            combined_list.append(x)

        for x in row2:
            combined_list.append(x)

        for x in row3:
            combined_list.append(x)

        str1 = ''.join(str(e) for e in combined_list)
        #print(str1)
        return str1

    def route_16(self, mess):
        combined_list = []
        row1 = []
        row2 = []
        row3 = []
        row4 = []
        numsret = []
        numsret[:0] = mess

        wordlen_route16 = len(mess)
        ro1 = [0, 11, 10, 9]
        ro2 = [1, 12, 15, 8]
        ro3 = [2, 13, 14, 7]
        ro4 = [3, 4, 5, 6]

        for x in range(0, 7):  # wordlen_route16):
            if x in ro1:
                if mess[x] == " ":
                    print("row 1", mess[x])  # for debbuging
                    row1.append("x")
                else:
                    row1.append(mess[x])
            elif x in ro2:
                if mess[x] == " ":
                    print("row 2", mess[x])  # for debbuging
                    row2.append("x")
                else:
                    row2.append(mess[x])
            elif x in ro3:
                if mess[x] == " ":
                    print("row 3", mess[x])  # for debbuging
                    row3.append("x")
                else:
                    row3.append(mess[x])
            else:
                if mess[x] == " ":
                    print("row 4", mess[x])  # for debbuging
                    row4.append("x")
                else:
                    row4.append(mess[x])
        row1.append(mess[11])
        row1.append(mess[10])
        row1.append(mess[9])

        row2.append(mess[12])
        row2.append(mess[15])
        row2.append(mess[8])

        row3.append(mess[13])
        row3.append(mess[14])
        row3.append(mess[7])

        print(row1)
        print(row2)
        print(row3)
        print(row4)

        for x in row1:
            combined_list.append(x)

        for x in row2:
            combined_list.append(x)

        for x in row3:
            combined_list.append(x)

        for x in row4:
            combined_list.append(x)

        str1 = ''.join(str(e) for e in combined_list)
        print(str1)
        return str1

    def route_26(self, mess):
        combined_list = []
        row1 = []
        row2 = []
        row3 = []
        row4 = []
        row5 = []
        numsret = []
        numsret[:0] = mess
        wordlen_route26 = len(mess)
        ro1 = [0, 16, 15, 14, 13]
        ro2 = [1, 17, 24, 23, 12]
        ro3 = [2, 18, 25, 22, 11]
        ro4 = [3, 19, 20, 21, 10]
        ro5 = [4, 5, 6, 7, 8, 9]
        for x in range(0, wordlen_route26):
            if x in ro1:
                row1.append(mess[x])
            elif x in ro2:
                row2.append(mess[x])
            elif x in ro3:
                row3.append(mess[x])
            elif x in ro4:
                row4.append(mess[x])
            else:
                row5.append(mess[x])

        for x in row1:
            combined_list.append(x)

        for x in row2:
            combined_list.append(x)

        for x in row3:
            combined_list.append(x)

        for x in row4:
            combined_list.append(x)

        for x in row5:
            combined_list.append(x)

        str1 = ''.join(str(e) for e in combined_list)
        print(str1)
        return str1

        # return row1, row2, row3, row4, row5

#                                                                 print(get_process(message))