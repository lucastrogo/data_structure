"""
    Atividade 2
    Disciplina: Lógica e Programação de Computadores IBMEC
    Nome: Lucas Trogo
    Matrícula: ----------
    Exercícios 1, 3, 4 e 6 da lista 2
"""


def remove_ord(key, list_i):
    """Remotion of an element of the list by a key that was gaved"""
    pos = 0
    searcher = len(list_i) - 1
    while pos <= searcher:
        if key == pos:
            if key == searcher:
                list_i[key] = list_i[key - 1]
                pos += 1
            else:
                list_i[key] = list_i[key + 1]
                pos += 1
        else:
            pos += 1
    return list_i


def include_ord(key, elem, list_i):
    """Inclusion of an element on the list by a key and element provided"""
    pos = 0
    searcher = len(list_i) - 1
    while pos <= searcher:
        if pos == key:
            list_i[pos] = elem
            pos += 1
        else:
            pos += 1
    return list_i


def palind(list_palind):
    """Function to se if the word is a palindrome or not"""
    pos = 0
    vet = 0
    size_palind = len(list_palind) - 1
    while pos <= size_palind:
        for pos in range(size_palind):
            if list_palind[vet] == list_palind[size_palind]:
                vet += 1
                size_palind -= 1
                pos += 1
            else:
                pos += 1
                return "Ins´t an palindrome"
                break
        return "Is an palindrome"
    return list_palind


def pile_to_row(perm, list_perm):
    """Function from pile to row"""
    i = 0
    pos = 1
    for pos in range(perm - 1):
        list_perm[i] = pos
        pos += 1
        i += 1
        print("Included")
    for pos in range(perm // 2):
        list_perm[pos] = list_perm[pos - 1]
        print("Removed")
        pos += 1
    for pos in range(1):
        list_perm[pos] = list_perm[pos + 1]
        print("Included")
    for pos in range(2):
        list_perm[pos] = list_perm[pos - 1]
        print("Removed")


LIST_I = [11, 33, 77, 88, 111]


LIST_PALIND = ["r", "a", "i", "a", "r"]

LIST_PERM = []

remove_ord(3, LIST_I)
include_ord(3, 5, LIST_I)
print("-"*15, "Removing an element", "-"*15, "\n")
print(f"     Removed element: {LIST_I[3]} List: {remove_ord(3, LIST_I)}\n")
print("-"*15, "Including an element", "-"*15, "\n")
print(f"              List:{include_ord(3, 5, LIST_I)}")

palind(LIST_PALIND)
print(palind(LIST_PALIND))
