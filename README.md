# scrapy_parser_pep

## Парсер PEP-документов на базе Scrapy.

Проект собирает данные о PEP:
- номер PEP
- название PEP
- статус PEP

Результаты сохраняются в CSV-файлы:
- список всех PEP
- сводка по статусам PEP

### Стек

- Python 3.9
- Scrapy 2.5.1
- pytest
- flake8
- isort
- black

### Структура проекта

```text
scrapy_parser_pep/
├── pep_parse/
│   ├── spiders/
│   │   └── pep.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   └── settings.py
├── results/
├── tests/
├── README.md
├── requirements.txt
└── scrapy.cfg
```
### Как развернуть проект

#### Клонировать репозиторий и перейти в папку проекта:
```
git clone https://github.com/Gevork23/scrapy_parser_pep.git
cd scrapy_parser_pep
```

#### Создать и активировать виртуальное окружение:

Windows (Git Bash)
```
py -3.9 -m venv venv
source venv/Scripts/activate
```

Linux / macOS
```
python3.9 -m venv venv
source venv/bin/activate
```

#### Установить зависимости:
```
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Запуск парсера

#### Запустить паука:
```
python -m scrapy crawl pep
```

После выполнения в папке results/ будут созданы два файла:
pep_YYYY-MM-DDTHH-MM-SS.csv
status_summary_YYYY-MM-DD_HH-MM-SS.csv

Пример содержимого файлов
pep_...csv
number,name,status
1,PEP Purpose and Guidelines,Active
8,Style Guide for Python Code,Active
20,The Zen of Python,Active
status_summary_...csv
Статус,Количество
Active,36
Final,352
Draft,49
Total,718
#### Запуск тестов

Проверка pytest:
```
python -m pytest
```
Проверка flake8:
```
flake8
```
#### Проверка форматирования

Установить black и isort, если они ещё не установлены:
```
python -m pip install black isort
```
Проверить isort:
```
isort . --check-only
```
Проверить black:
```
black . --check
```
Исправить сортировку импортов и форматирование:
```
isort .
black .
```

### Что делает проект

##### Переходит на страницу PEP Index.

##### Находит ссылку на Numerical Index.

##### Собирает ссылки на все PEP.

##### Заходит на страницу каждого PEP.

##### Извлекает:
номер
название
статус

Сохраняет полный список PEP в CSV.

Формирует сводку по статусам и сохраняет её в отдельный CSV.
