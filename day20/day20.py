def get_infinity(step, enhancement):
    if step % 2:
        return int(enhancement[0] == '#')
    return 0


def enhance_pixel(image, enhancement, x, y, step):
    n = 0
    for yy in range(y-1, y+2):
        for xx in range(x-1, x+2):
            if xx < 0 or xx >= len(image[0]) or yy < 0 or yy >= len(image):
                n = n << 1
                n |= get_infinity(step, enhancement)
            else:
                n = n << 1
                n |= int(image[yy][xx] == '#')
    return enhancement[n]


def day20(image_data, enhancement):
    img = image_data
    for step in range(1, 51):
        updated_image = []
        for y in range(-1, len(img) + 1):
            x_data = ''
            for x in range(-1, len(img[0]) + 1):
                x_data += enhance_pixel(img, enhancement, x, y, step)
            updated_image.append(x_data)
        if step == 2:
            yield updated_image.copy(), step
        img = updated_image
        if step == 50:
            yield updated_image.copy(), step


def count_pixels(image): return sum(row.count('#') for row in image)


if __name__ == '__main__':
    with open('day20.txt') as data:
        parts = data.read().split('\n')
        enhancement = parts[0]
        image_data = parts[2:]
        for updated_image, step in day20(image_data, enhancement):
            c = 0
            for line in updated_image:
                c += line.count('#')
            print(f"{step} {c}")
