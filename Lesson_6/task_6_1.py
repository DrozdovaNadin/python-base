# Распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt

from requests import get, utils
file1 = open('nginx_logs.txt', mode="w+", encoding="Utf-8") #открываем файл для записи
response = get('https://gbcdn.mrgcdn.ru/uploads/asset/2729331/attachment/e84f9ad49c706008fba3b58e2a1e5b09.txt')

encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)


file1.write(content) #записываем содержимое в файл
file1.close()

with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
    for line in file_1:
        ip_address, log_line = line.split(' - - ')
        date, log_line = log_line.split('] ')
        req, s = log_line.split('/',1)
        s, b = s.split('HTTP',1)
        # Удаление символа
        req = req.replace('"', '')
        print(([(ip_address, req, s)]))


