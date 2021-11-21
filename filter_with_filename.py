from PIL import Image
import numpy as np


def get_mosaic(image, size, gradation):
    '''
    Принимает изображение и применяет к нему фильтр, который делает черно-белый пиксель-арт
    :param image: исходное изображение
    :param size: размер мозайки
    :param gradation: размер градации
    :return: новое изображение(пиксль-арт)

    '''
    image_arr = np.array(Image.open(image)).astype(int)
    limit = 255 // gradation
    image_len = len(image_arr)
    image_h = len(image_arr[0])
    i = 0
    while i < image_len:
        j = 0
        while j < image_h:
            segment = image_arr[i: i + size, j: j + size]
            sum_c = np.sum(segment)
            avg = int(sum_c // (size ** 2))
            set_color(int(avg // limit) * limit / 3, image_arr, size, i, j)
            j += size
        i += size
    return Image.fromarray(np.uint8(image_arr))


def set_color(new_c, matrix, size, i, j):
    '''
    Принимает размер мозайки и устанавливает новый цвет для пикселя
    :param new_c: новый цвет пикселя
    :param matrix: матрица изображения
    :param size: размер мозайки
    :param i: пиксель по оси x
    :param j: пиксель по оси y
    :return: устанавливает новый цвет пикселя
    '''
    for x in range(i, i + size):
        for y in range(j, j + size):
            for z in range(3):
                matrix[x][y][z] = new_c

get_mosaic('img1.jpg', 10, 50).save('res.jpg')
