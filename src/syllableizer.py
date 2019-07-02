#!/usr/bin/python
import inflect
import sys
import os



class Syllableizer:
    def __init__(self, dictPath):
        self.p = inflect.engine()
        self.d = {}
        self.words_list = []

        with open(dictPath) as f:
            for line in f:
                (key, val) = line.split("\t", 1)
                val = val.replace("\n", "")
                self.d[key.lower()] = val

    def isfloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def split_words(self, usr_input):
        print "in syllableizer"
        words = usr_input
        words = words.replace(".", " . ")
        words = words.replace("!", " !")
        words = words.replace("?", " ? ")
        words = words.replace(",", " , ")
        words = words.replace("-", " - ")
        words = words.replace(":", " : ")
        words = words.replace(";", " ; ")
        words = words.replace("\"", " \" ")
        words = words.replace(")", " ) ")
        words = words.replace("(", " ( ")
        words = words.replace("\\", " \\ ")
        words = words.replace("/", " / ")
        words = words.replace("[", " [ ")
        words = words.replace("]", " ] ")
        words = words.split()
        for a in words:
            try:
                if a.isdigit():
                    # print ("true", a)
                    w = self.p.number_to_words(a)
                    # print w
                    self.split_words(w)

                elif self.isfloat(a):
                    (w, dec) = a.split(".", 1)
                    w = self.p.number_to_words(a)
                    # print w
                    self.split_words(w)
                else:
                    # print a
                    self.words_list.append(self.d[a.lower()])
            except:
                path = os.path.dirname(__file__)
                print "Errors, see error.txt"
                f = open( path + "/error.txt", "a+")
                f.write("Failed Word: %s\n" % a)
                f.close()

    def getList(self):
        returnList = self.words_list
        self.words_list = []
        return returnList


def main(args):
    parser = Syllableizer()
    usr_input = "none"
    while (usr_input != "quit"):
        usr_input = raw_input('enter word to break apart\n')
        parser.split_words(usr_input)
        print parser.getList()


if __name__ == '__main__':
    main(sys.argv)
