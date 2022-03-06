import colorsys
import random


def random_hsl_vector():
    hue = random.random()
    saturation = 1
    lightness = 0.8
    return (hue, saturation, lightness)


def random_rgb_vector():
    (hue, saturation, lightness) = random_hsl_vector()
    (red, green, blue) = list(map(
        lambda x: (int)(x * 255),
        colorsys.hls_to_rgb(hue, lightness, saturation),
    ))
    return (red, green, blue)


def random_hsl():
    (hue, saturation, lightness) = random_hsl_vector()
    return f'hsl({hue:.0f},{saturation:.0%},{lightness:.0%})'


def random_rgb():
    (red, green, blue) = random_rgb_vector()
    return f'rgb({red},{green},{blue})'


def random_hex():
    (r, g, b) = random_rgb_vector()
    return f'#{r:02x}{g:02x}{b:02x}'
