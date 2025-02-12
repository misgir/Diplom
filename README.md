# Diplom
Кинопоиск - сервис для поиска и просмотра фильмов.
В проекте присутствуют:
1. test_api - проверки поиска фильмов через backend с разным параметрам (имя актера, id и т.д)
2. test_ui - проверки поиска фильма через frontend с разными параметрами (актер, символ, цифра)
3.requirements.txt
Перед запуском тестов нужно установить зависимости: pip install -r requirements.txt  
Далее запустить тесты через Allure:  
python -m pytest --alluredir allure-result  
И открыть отчет для просмотра:
allure serve allure-result