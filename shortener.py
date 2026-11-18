ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encode(num: int) -> str:
    if num == 0:
        return ALPHABET[0]
    chars = []
    while num > 0:
        num, rem = divmod(num, 62)
        chars.append(ALPHABET[rem])
    return "".join(reversed(chars))

if __name__ == "__main__":
    print("12345 ->", encode(12345))
