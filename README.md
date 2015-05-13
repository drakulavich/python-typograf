Превращает знаки дюйма (""), дефисы (-) и другие клавиатурные символы в кавычки («»), тире (—). Добавляет неразрывные пробелы.

Использованы наработки проекта [alfred-typograf](https://github.com/voldmar/alfred-typograf) и [«Типограф»](http://www.artlebedev.ru/tools/typograf/) студии Артемия Лебедева.

## Использование

Скопируйте текст, нажмите горячие клавиши → в буфер попадёт исправленный текст с типографикой.

**В Ubuntu**: System Settings... → Keyboard → Shortcuts → Custom Shortcuts. Прописываем исполнение скрипта:
```
python /path/to/typograph.py
```
**В Windows**: Создать ярлык. Для выполнения указываем `**pythonw**`, чтобы не открывалось консольные окно при запуске.

Назначаем сочетание клавиш. Например, `Ctrl+Win+T`.

Сценарий работы:
* `Ctrl+C` куска текста
* `Ctrl+Win+T` преобразование
* `Ctrl+V` в нужном месте

## Установка

Зависимости для работы с буфером и обработкой HTTP-запросов:
```
pip install pyperclip requests
```

#### pip в Linux

В репозиториях пакет `python-pip` зачастую устаревший. Рекомендуется установить последнюю версию командой:
```
easy_install -U pip
```

#### pip в Windows

[Скачиваем](https://www.python.org/downloads/windows/) и устанавливаем свежий релиз Python 2. В поставку, начиная с 2.7.9, включен `pip`.

#### Работа с прокси

Должна быть установлена переменная `http_proxy`. Для windows и linux соответственно:
```
set http_proxy=your_proxy:port

export http_proxy=your_proxy:port
```