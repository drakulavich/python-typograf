Превращает знаки дюйма (""), дефисы (-) и другие клавиатурные символы в кавычки («»), тире (—). Добавляет неразрывные пробелы.

Использованы наработки проекта [alfred-typograf](https://github.com/voldmar/alfred-typograf) и [«Типограф»](http://www.artlebedev.ru/tools/typograf/) студии Артемия Лебедева.

## Использование

**В Ubuntu**: System Settings... → Keyboard → Shortcuts → Custom Shortcuts. Прописываем исполнение скрипта:
```
python /path/to/typograph.py
```
**В Windows**: Создать ярлык. Для выполнения указываем `pythonw`, чтобы не открывалось консольные окно при запуске.

Назначаем сочетание клавиш. Например, `Ctrl+Win+T`.

Скопируйте текст, нажмите горячие клавиши → в буфер попадёт исправленный текст с типографикой.

1. `Ctrl+C`
2. `Ctrl+Win+T`
3. `Ctrl+V`

## Установка

Зависимости для работы с буфером и обработкой HTTP-запросов:
```
pip install pyperclip requests
```

#### Linux

В репозиториях пакет `python-pip` зачастую устаревший. Рекомендуется установить последнюю версию командой:
```
easy_install --user -U pip
```
Для **Python 3** нет обвязки к gtk, в этом случае ставим `xclip`:
```
sudo apt-get install xclip
```

#### Windows

[Скачиваем](https://www.python.org/downloads/) и устанавливаем Python. В поставку, начиная с 2.7.9 и 3.4.2, включен [pip](https://en.wikipedia.org/wiki/Pip_%28package_manager%29).

##### Работа с прокси

Убедитесь, что установлена переменная `http_proxy`. Для Windows и Linux соответственно:
```
set http_proxy=your_proxy:port

export http_proxy=your_proxy:port
```
