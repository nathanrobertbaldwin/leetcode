def toHex(num: int) -> str:
    if num == 0:
        return "0"

    negative = False
    if num < 0:
        negative = True
        num = -num - 1

    hex_map = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}

    compliment_map = {
        "0": "f",
        "1": "e",
        "2": "d",
        "3": "c",
        "4": "b",
        "5": "a",
        "6": "9",
        "7": "8",
        "8": "7",
        "9": "6",
        "a": "5",
        "b": "4",
        "c": "3",
        "d": "2",
        "e": "1",
        "f": "0",
    }

    hex_str = ""
    neg_hex_str = ""

    while num > 0:
        remainder = num % 16
        if remainder > 9:
            hex_str = hex_map[remainder] + hex_str
        else:
            hex_str = str(remainder) + hex_str
        num = num // 16

    if negative == False:
        return hex_str
    else:
        fill = 8 - len(hex_str)
        hex_str = ("0" * fill) + hex_str
        for letter in hex_str:
            neg_hex_str += compliment_map[letter]
        return neg_hex_str


print(toHex(-10000))
