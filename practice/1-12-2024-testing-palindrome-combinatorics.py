def is_pal(str):
    i = 0
    while i < len(str) // 2:
        if str[i] != str[len(str) - i - 1]:
            return False
        i += 1
    return True


def pal_tester(length, letters):
    pals = set()
    not_pals = set()

    def pal_generator(length, letters, curr_str=""):
        if len(curr_str) == length:
            if is_pal(curr_str) is True:
                pals.add(curr_str)
            else:
                not_pals.add(curr_str)
            return
        else:
            for letter in letters:
                pal_generator(length, letters, curr_str + letter)

    pal_generator(length, letters)
    return {
        "total": len(pals) + len(not_pals),
        "pals": len(pals),
        "not_pals": len(not_pals),
    }


def total_combos_formula(length, letters):
    return len(letters) ** length


def pal_combos_formula(length, letters):
    if length % 2 == 0:
        return (length // 2) ** len(letters)
    else:
        return ((length // 2) ** len(letters)) * len(letters)


length = 6
letters = ["a", "b"]

print(pal_tester(length, letters))
print(total_combos_formula(length, letters))
print(pal_combos_formula(length, letters))

s = ""
