import rarfile
import zipfile
import os

PATH = 'archives/'

comments = []
count = 0
i = 0
flag = ''

while count < 120:
    try:
        file = rarfile.RarFile('archives/unzipme.{0}'.format(i), 'r')
        c, j = file.comment.strip().split(',')
    except rarfile.BadRarFile:
        file = zipfile.ZipFile('archives/unzipme.{0}'.format(i), 'r')
        c, j = file.comment.decode().strip().split(',')

    flag += c
    i += int(j)
    count += 1
print(flag)
