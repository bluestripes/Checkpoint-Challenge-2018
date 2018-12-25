import rarfile
import zipfile
import os

PATH = '/home/gal/Downloads/archives/'

comments = []
count = 0
i = 0
res = ''

while count < 120:
    try:
        file = rarfile.RarFile('/home/gal/Downloads/archives/unzipme.{0}'.format(i), 'r')
        c, j = file.comment.strip().split(',')
    except rarfile.BadRarFile:
        file = zipfile.ZipFile('/home/gal/Downloads/archives/unzipme.{0}'.format(i), 'r')
        c, j = file.comment.decode().strip().split(',')

    res += c
    i += int(j)
    count += 1
print(res)