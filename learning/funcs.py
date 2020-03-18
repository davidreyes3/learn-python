# r - read only, is default
# w - write only, cant read contents, WILL DELETE CONTENT WHEN OPENING
# a - append
# r+, read-write
# if you open a file and the file already exists, the old contents will be deleted as soon as the file is opened
file_path = "test.properties"

def dict_practice():
    d = {"id": 1, "name": "name1"}
    print(d["id"])
    print(d["name"])


def chunker(iterable, size):
    # Implement function here
    list = []
    iterable_length = len(iterable)
    i = 0
    for item in iterable:
        list.append(item)
        i += 1
        if len(list) == size or i == iterable_length:
            yield list
            list = []





def chunker2(iterable, size):
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]




def lists():
    s = 'python programming'
    print(s[0])
    print()
    print(s[0:4])



def getting_a_date():
    import datetime
    import os

    timestamp = os.path.getmtime(file_path) # timestamp of last modification
    print(timestamp)

    print(datetime.datetime.fromtimestamp(timestamp)) # human readable date


#getting_a_date()


def iterating_through_files():
    lines = []
    with open(file_path) as file:
        lines = file.readlines()
    print(lines)


# iterating_through_files()


def with_block_file():
    with open(file_path) as file:
        print(file.read())

    print("---")

    with open(file_path) as file:
        # for line in file:  # line includes the new line character
        #   print("'{}'".format(line))
        for line in file:
            print("'{}'".format(line.strip()))  # deletes new line characters


# with_block_file()


def open_read_close_file():
    file = open(file_path)
    print(file.readline())
    print("---")
    print(file.read())
    print("---")
    print(file.read())  # nothing left to read; prints just an empty line
    file.close()

# open_read_close_file()

# colors = ["red", "white", "blue"]
# colors.insert(2, "yellow")
# print(colors)

# def highlight_word(sentence, word):
#     #for x in sentence.split():
#         #if x == word:
#             #print(x.upper())
#             #return x.upper()
#     #return word
#     print(sentence.split())
#     return sentence.replace(word, word.upper())
#
#
# print(highlight_word("Have a nice day", "nice"))
# print(highlight_word("Shhh, don't be so loud!", "loud"))

#
#
#

# def combine_lists(list1, list2):
#     # Generate a new list containing the elements of list2
#     # Followed by the elements of list1 in reverse order
#     list1_ordered = []
#     for elem in list1:
#         list1_ordered.insert(0, elem)
#     print(list1_ordered)
#     list2.extend(list1_ordered)
#     return list2
#
#
# Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
# Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
#
# print(combine_lists(Jamies_list, Drews_list))
