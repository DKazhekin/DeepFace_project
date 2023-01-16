# Проект по курсу "ООП"

## Тема проекта: "DetFaceBot"
Наша команда реализовала телеграмм бота, основной задачей которого является работа с изображениями. Функционал бота составляет несколько кнопок, при нажатии на которые, пользователь может:
1. Проверить сколько человек есть на фотографии
2. Узнать один и тот же ли человек представлен на двух отправленных фотографиях
3. Выбрать стиль, в котором будет отрисована новая фотография по предоставленной

## Зоны ответственности разработчиков

Армишев К.К. М8О-208Б-21
- Создание на основе машинного обучения кнопки Filter
- Внедрение Filter в tg бот(с возможностью выбора стиля обработки фотографии)
- Внедрение бота на сервер

Кажекин Д.А. М8О-207Б-21
- Организация структуры телеграмм бота
- Реализация функций определения количества человек на фотографии, определения один и тот ли человек изображен на двух фотографиях
- Помощь в интеграции функции фильтра в проект

Желанов Д.В. М8О-210Б-21
- Создание на основе машинного обучения кнопки Filter
- Внедрение Filter в tg бот(с возможностью выбора стиля обработки фотографии)

## Как развернуть приложение:

1. Для запуска нужно поместить всё части проекта в одну папку
2. Активировать виртуальное окружение
```
python -m venv venv
source venv/bin/activate
```
3. Установить Pytorch
```
pip3 install torch torchvision torchaudio —extra-index-url https://download.pytorch.org/whl/cpu
```
4. Установить библиотеки из requirements.txt 
```
pip install -r requirements.txt 
```
5. Установить cmake
```
pip install cmake 
```
6. Установить dlib
```
pip install dlib==19.20 
```
7. Установить ffmpeg
```
sudo apt install ffmpeg
```
8. Установить PyTelegramBotApi
```
pip install pytelegrambotapi
```
9. Установить Face_Recognition
```
pip install face_recognition
```
10. Запустить бота
```
python bot.py
```
11. Перейти в telegram и найти бота ( https://t.me/WheatherIt_bot )
12. Ввести команду "/start"

## Пример работы
### 1. Запуск бота, выбор необходимой функции

![1](https://i.postimg.cc/d0DZFV5p/IMG-4128.jpg)

### 2. Функция, определяющая кол-во людей на фотографии

![2](https://i.postimg.cc/pdnWLMxs/IMG-4129.png)

### 3. Главная функция - Filter, применяющая разные стили к фотографиям
#### 3.1 Стиль Art
![3](https://i.postimg.cc/bvPCsQf4/IMG-4132.png)

#### 3.2 Стиль Arcane-multi

![4](https://i.postimg.cc/fW86pgQy/IMG-4131.png)

#### 3.3 Стиль Sketch-multi

![5](https://i.postimg.cc/0yh6ffyH/IMG-4135.png)

### 4. Функция, определяющая: один ли человек на разных фотографиях

#### 4.1 Пример с одинаковыми людьми
![6](https://i.postimg.cc/1X3g3RHL/IMG-4136.png)

#### 4.2 Пример с разными людьми
![7](https://i.postimg.cc/RZ5GDchq/IMG-4134.png)

<h5 align=center>
<br>
<em>Выполнено в рамках курсового проекта по ООП
<br>
МАИ, 2023</em>
</h5>
