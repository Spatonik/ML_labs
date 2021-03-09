from PIL import Image, ImageDraw
from random import randrange


def polygon(draw, coordinate):
    draw.regular_polygon(((coordinate[0] - 110), (coordinate[1] - 110), randrange(30, 130)), randrange(3, 6),
                         rotation=randrange(0, 180),
                         fill=(randrange(100, 255), randrange(100, 255), randrange(100, 255)))


def rectangle(draw, coordinate):
    draw.rectangle((coordinate[0] - randrange(60, 240), coordinate[1] - randrange(60, 240),
                    coordinate[0], coordinate[1]), fill=(randrange(100, 255), randrange(100, 255), randrange(100, 255)))


def circle(draw, coordinate):
    a = randrange(60, 240)
    draw.ellipse((coordinate[0] - a, coordinate[1] - a, coordinate[0], coordinate[1]),
                 fill=(randrange(100, 255), randrange(100, 255), randrange(100, 255)))


def random_images(number):
    figure_selection = [polygon, circle, rectangle]
    fourth = 256
    centre = [fourth, fourth]
    for i in range(number):
        im = Image.new('RGB', (1200, 1200), (0, 0, 0))
        draw = ImageDraw.Draw(im)
        for j in range(16):
            figure_selection[randrange(0, 3)](draw, centre)
            if centre[0] == 1024:
                centre[0] = fourth
                if centre[1] != 1024:
                    centre[1] += fourth
                else:
                    centre[1] += 0
            else:
                centre[0] += fourth
        im.save(f"create/image{i}.jpg")
        centre = [fourth, fourth]
