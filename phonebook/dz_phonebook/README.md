# **Телефонный справочник**

**Описание задачи.**  
Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.  
_Под форматами понимаем структуру файлов, например: в файле на одной строке хранится одна часть записи, пустая строка - разделитель._

**Структура приложения (модули)**

1. main (основной модуль) 
2. logger (модуль логирования) 
3. .gitignore (не требует комментариев) 
4. crud (создание, чтение, обновление, удаление) 
5. user_interface (модуль взаимодействия с пользователем) 
6. data_generation (модуль генерации БД) 

**Как запустить проект**

Для запуска необходимо запустить main.py

отдельно есть метод генерации контактов, для этого необходимо раскомментировать все в main.py один раз
запустить и вернуть все назад
   

Для запуска телеграм-бота:
скачать проект в локальный репозиторий;
настроить окружение, введя в консоле поочередно команды:
python3 -m venv .libraries;
pip install pyTelegramBotAPI;
при необходимости обновить библиотеку до последней версии (следуя инструкциям в консоле)
перезапустить консоль;
перед запуском необходимо в файле "bot.py" в строке 8 вместо слова ТОКЕН ввести свой индивидуальный токен телеграмм бота
в консоле ввести команду "python3 bot.py" или "python bot.py" 





