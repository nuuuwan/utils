def get_bbox(xy_list):
    max_x, max_y = min_x, min_y = xy_list[0]
    for [x, y] in xy_list[1:]:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    x_span = max_x - min_x
    y_span = max_y - min_y

    return [
        min_x,
        max_x,
        min_y,
        max_y,
        x_span,
        y_span,
    ]


def get_func_transform(WIDTH, HEIGHT, PADDING, xy_list):
    [
        min_x,
        max_x,
        min_y,
        max_y,
        x_span,
        y_span,
    ] = get_bbox(xy_list)

    r = (x_span / HEIGHT) / (y_span / WIDTH)
    if r > 1:
        WIDTH /= r
    else:
        HEIGHT *= r

    def func_transform(xy):
        [x, y] = xy
        px = (x - min_x) / x_span
        py = (y - min_y) / y_span

        x = (px) * (WIDTH - PADDING * 2) + PADDING + WIDTH
        y = (1 - py) * (HEIGHT - PADDING * 2) + PADDING
        return [x, y]

    return func_transform
