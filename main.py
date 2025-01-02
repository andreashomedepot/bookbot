def main():
    count_alphabet = {
            "a":0,"b":0,
            "c":0,"d":0,
            "e":0,"f":0,
            "g":0,"h":0,
            "i":0,"j":0,
            "k":0,"l":0,
            "m":0,"n":0,
            "o":0,"p":0,
            "q":0,"r":0,
            "s":0,"t":0,
            "u":0,"v":0,
            "w":0,"x":0,
            "y":0,"z":0,}
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    lowered_string = file_contents.lower()
    count_words = len(file_contents.split())

    for words in lowered_string.split():
        for letter in words:
            if letter in count_alphabet:
                count_alphabet[letter] += 1

    output_string(count_words,count_alphabet)


def output_string(count_words,count_alphabet):
    print("The start of the report")
    print(f"There is {count_words} words in the document")
    print("")
    for letther in count_alphabet:
        print(f"The {letther} character was found {count_alphabet[letther]} timrs")
    print("End of the report")


main()