# Django-приложение с подключенными RabbitMQ и PostgreSQL

Данный пример демонстрирует деплой приложения с использованием Docker либо Kubernetes.

## Требования перед запуском

 * Minikube последней актуальной версии
 * Kubernetes последней актуальной версии
 * Docker последней актуальной версии
 * Docker-compose последней актуальной версии

## Деплой с использованием Docker

Для деплоя необходимо выполнить команду:

```
docker compose up
```

В логах postgersql должна появиться похожая строка:
```
UTC [1] LOG:  database system is ready to accept connections
```

В логах rabbitmq должна появиться похожая строка:
```
[info] <0.9.0> Time to start RabbitMQ: 3750 ms
```

В логах приложения должна появиться похожая строка:
```
Starting development server at http://0.0.0.0:8000/
```

Для проверки работоспособности приложения можно перейти по адресу http://localhost:8000/swagger/. Используя POST запрос, можно создавать новые задачи.
С помощью двух других GET запросов можно получать информацию обо всех существующих задачах и о конкретной задаче по идентификатору.

Для проверки работоспособности RabbitMQ можно перейти по адресу http://localhost:15672/. Username - guest, password - guest.
Здесь можно увидеть задачи, добавленные в очередь.

Для проверки работоспособности PostgreSQL нужно воспользоваться любым клиентом для работы с БД.
Host - localhost, user - postgres, password - postgres, default database - tasks, port - 5432.
Если выполнить запрос
```
select * from tasks_taskmodel;
```
то можно увидеть созданные задачи.

## Деплой с использованием Kubernetes

Для локального запуска с использованием minikube нужно выполнить следующие команды:
```
minikube start --driver=docker
minikube addons enable ingress
```

Затем из директории .kube выполнить
```
kubectl apply -f postgres_manifest/
```
и дождаться, пока statefulset и service станут активными (проверить можно при помощи kubectl get all).
Подключение к БД можно проверить при помощи любого клиента.
Host - результат команды minikube ip, user - postgres, password - postgres, default database - tasks, port - 30000.

После чего выполнить команду
```
kubectl apply -f rabbit_manifest/
```
Для проверки работоспособности RabbitMQ нужно предварительно отредактировать файл /etc/hosts, добавить туда строку вида
```
192.168.49.2	rabbitmq-manager.com
```
где ip адрес это результат команды minikube ip.
Работоспособность RabbitMQ можно проверить по адресу rabbitmq-manager.com. Username - guest, password - guest.

Для запуска приложения нужно выполнить
```
kubectl apply -f app_manifest/
```
Для корректной работы необходимо, чтобы PostgreSQL и RabbitMQ были запущены.

Нужно отредактировать файл /etc/hosts, добавить туда строку вида
```
192.168.49.2	test-deploy-proj.ru
```
где ip адрес это результат команды minikube ip.
Работоспособность приложения можно проверить по адресу test-deploy-proj.ru/swagger.

При помощи POST запроса можно добавлять новые задачи.
С помощью двух других GET запросов можно получать информацию обо всех существующих задачах и о конкретной задаче по идентификатору.
При добавлении задачи создается запись в БД и появляется задача в RabbitMQ.

Если выполнить запрос
```
select * from tasks_taskmodel;
```
то можно увидеть созданные задачи.
По адресу rabbitmq-manager.com можно отслеживать работу RabbitMQ.
