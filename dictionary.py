def creat_dictionary():
    x = {"day": "when the sun is out", 
         "night": "when the moon is out",
         "noon": "iN THE MIDDLE"}
    return x

def add_to_dictionary(in_dictionary, new_word, new_definition):
    in_dictionary[new_word] = new_definition


def output_dictionary(in_dictionary):
    print(in_dictionary)
    print(in_dictionary["night"])
    add_to_dictionary(in_dictionary, "lunch", "mid day meal")
    print(get_dictionary(in_dictionary, "lunch"))
    #print(in_dictionary.key())
    #print(in_dictionary.value())
    

def get_dictionary(in_dictionary, word):
    #another = in_dictionary.get(word)
    definition = in_dictionary[word]
    return definition


if __name__ == "__main__":
    my_dictionary = creat_dictionary()
    output_dictionary(my_dictionary)