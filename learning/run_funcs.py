import importlib

funcs = importlib.import_module("funcs")

def run_dict_practice():
    funcs.dict_practice()


def run_chunker2():
    for chunk in funcs.chunker2('python programming', 5):
        print(list(chunk))


def run_chunker():
    for chunk in funcs.chunker(range(25), 4):
        print(list(chunk))


def run_lists():
    funcs.lists()


def main():
    run_dict_practice()


main()
