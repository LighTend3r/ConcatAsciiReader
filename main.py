import copy
import argparse

def main(sentence, debug):
    find = False
    listeOfAll = [[0, ""]]
    listeOfFail = []
    listeNext = [[0, ""]]
    good = []
    while listeNext != []:
        listeOfAll = copy.deepcopy(listeNext)
        listeNext = []
        for node in listeOfAll:
            if node[0] >= len(sentence):
                find = True
                good.append(node[1])
                continue
            response = next(node[0], sentence, node[1])
            for r in response:
                listeNext.append(r)
        if debug:
            for liste in listeOfAll:
                print(liste[1])

    if not find:
        print("No solution, but I found this :")
    else:
        print("\nI found this :\n")
        for g in good:
            print(g)
            print("-----------------")


def next(i, sentence, char):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-!@#$%^&*()_+[]{};\"':,./<>?`~ \n"
    response = []
    if sentence[i:i+1] != "0":
        if chr(int(sentence[i:i+1])) in alphabet and i + 1 <= len(sentence):
            response.append([i + 1, char + chr(int(sentence[i:i+1]))])

        if chr(int(sentence[i:i+2])) in alphabet and i + 2 <= len(sentence):
            response.append([i + 2, char + chr(int(sentence[i:i+2]))])

        if chr(int(sentence[i:i+3])) in alphabet and i + 3 <=len(sentence):
            response.append([i + 3, char + chr(int(sentence[i:i+3]))])
    return response

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='ConcatAsciiReader',
                    description='Parser of concat ascii')

    parser.add_argument('-d', '--debug', action='store_true', help='seen the debug to see the process')
    parser.add_argument('-t', '--txt', help='The text to decode', required=True)
    args = parser.parse_args()
    for i in args.txt:
        if i not in "0123456789":
            print("Error, only number")
            exit()

    main(args.txt, args.debug)

