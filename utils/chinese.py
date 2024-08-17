dots = {
    "sc": "·",
    "tc": "‧",
    "ja": "・",
}


def get_best_chinese_dot(cmap):
    return (
        cmap.get(ord(dots["ja"]))
        or cmap.get(ord(dots["tc"]))
        or cmap.get(ord(dots["sc"]))
    )


def better_chinese_dot(font):
    cmap = font.getBestCmap()

    best_dot = get_best_chinese_dot(cmap)
    if best_dot:
        cmap[ord(dots["sc"])] = best_dot
        cmap[ord(dots["tc"])] = best_dot
    if cmap.get(ord(dots["ja"])) is None:
        cmap[ord(dots["ja"])] = best_dot


def zhu_to_dot(font):
    cmap = font.getBestCmap()
    best_dot = get_best_chinese_dot(cmap)
    if best_dot:
        cmap[ord("丶")] = best_dot


def enforce_corner_brackets(font):
    cmap = font.getBestCmap()
    if ord("「") in cmap:
        cmap[ord("“")] = cmap.get(ord("「"))
    if ord("」") in cmap:
        cmap[ord("”")] = cmap.get(ord("」"))
