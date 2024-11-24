test = ["//////", "/**//**////**/", "///*/**/", "/////", "//*/", "/*//*/"]


def comments_correct(s: str) -> bool:
    if len(s) % 2 != 0 or len(s) < 2:
        return False

    is_multi_comment = False
    for i in range(0, len(s), 2):
        c = s[i] + s[i + 1]
        if c not in ["//", "/*", "*/"]:
            return False

        if is_multi_comment and c == "/*":
            return False
        elif not is_multi_comment and c == "/*":
            is_multi_comment = True
        elif is_multi_comment and c == "*/":
            is_multi_comment = False
        elif not is_multi_comment and c == "*/":
            return False

    if is_multi_comment:
        return False

    return True


for i in test:
    print(comments_correct(i))
