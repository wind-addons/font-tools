def update_name_with(font, update_func: callable):
    for name in font["name"].names:
        if name.nameID in (1, 4):
            encoding = "utf-16-be" if name.isUnicode() else "latin-1"
            name.string = update_func(name.string.decode(encoding)).encode(encoding)
