# Конвертер бот  

Написан с помощью библиотеки Aiogram в целях обучения 



## Примеры возможностей

#### конвертер валют 
![image](./description/gifs/currency_var2.gif)

#### Системы счисления 
![image](./description/gifs/scale_of_notation.gif)

#### Конвертер температуры
![image](./description/gifs/temperature.gif)

#### Определение возраста и кол-ва дней до следующего дня рождения
![image](./description/gifs/birthday.gif)

### обычный и инлайн калькулятор 
<code>
<div style="display: flex; justify-content: flex-start; align-items: center;">
    <img style="margin-right: 50px;" height="737" src="./description/gifs/default_calculator.gif">
    <img height="737" src="./description/gifs/inline_calculator.gif">
</div>
</code>

## Установка

1. Создайте локально каталог и перейдите в него

2. Клонируйте в текущую директорию (точка в конце)

> git clone https://github.com/meys313/converter_bot.git .



### 2. Создать виртуальное окружение:

> python -m venv venv

> source venv/bin/activate

> pip install --upgrade pip

### 3. Установите все зависимости 

> pip install -r ./requirements.txt

### 4. Создать файл с переменными окружения ".env" в корне
    внесите данные по шаблону:

    ADMINS= ваш id telegram
    BOT_TOKEN=5181660672#AEqj2xGlfqNEqdss4V6Vib7hmNTMZtUsIp2q # токен вашего бота
    ip=localhost


### 5. Запустите app.py 


