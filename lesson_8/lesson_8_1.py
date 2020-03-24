import hashlib


def line_options(a):
    b = []  # Пришлось оставить массив для сравнения, иначе подсчитывались повторения.
    for n in range(len(a)):
        for i in range(len(a)):
            if (hashlib.sha1(a[n:i + 1].encode('utf-8')).hexdigest() not in b) and \
                    (hashlib.sha1(a[n:i + 1].encode('utf-8')).hexdigest() != hashlib.sha1(
                        ''.encode('utf-8')).hexdigest()) and \
                    hashlib.sha1(a[n:i + 1].encode('utf-8')).hexdigest() != hashlib.sha1(a.encode('utf-8')).hexdigest():
                b.append(hashlib.sha1(a[n:i + 1].encode('utf-8')).hexdigest())
    return len(b)


print(line_options('Скалка!'))

