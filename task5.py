"""
Задание 5.
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.
Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess

import chardet

pingWebsite = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]

for ping_element in pingWebsite:
    ping_process = subprocess.Popen(ping_element, stdout=subprocess.PIPE)
    for string in ping_process.stdout:
        result = chardet.detect(string)
        string = string.decode(result['encoding'])
        print(string)
