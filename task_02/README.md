## Для работы необходим сервер postgres
### Конфиг подключения прописывается в файле
> config.py

В файле образа прокинуты два переменных окружения:
> name - для теста имени на базовой странице
> hostip - ip адрес для подключения postgres БД

### Создаем сетку
> docker network create --driver bridge flask-network

### Монтируем образ Postgres
> cd postres/
> docker build --tag=postres .

### Монтируем образ фласк
> docker build --tag=flask-simple .

### Запускаем контейнер Postres (обязательно первым)
> docker run -dit --name postgres --network flask-network postgres

### Запускаем контейнер Flask
docker run --name flask-simple -p 80:5000 --network flask-network flask-simple


Для форвардинга портов в Unix системе из bridge сети:
> sysctl net.ipv4.conf.all.forwarding=1
> sudo iptables -P FORWARD ACCEPT
