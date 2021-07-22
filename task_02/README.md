##Для работы необходим сервер postgres
###Конфиг подключения прописывается в файле
> config.py

В файле образа прокинуты два переменных окружения:
> name - для теста имени на базовой странице
> hostip - ip адрес для подключения postgres БД

### Монтируем образ
> docker build --tag=flask-simple .

### Запускаем контейнер
> docker run -p 80:5000 --name=my-flask flask-simple