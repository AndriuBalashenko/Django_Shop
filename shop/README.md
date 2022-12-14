# Django_Shop
Дипломный проект Django
### Запуск через Docker 
* Ссылка для Windows https://docs.docker.com/desktop/install/windows-install/
* Ссылка для Mac https://docs.docker.com/docker-for-mac/install/
* Ссылка для Linux https://www.docker.com/community-edition
1. Скачиваем ZIP-архив проектра из GitHub
2. Распаковываем архив
3. Данная команда создает новый образ и запустим два контейнера:
```sh
docker-compose up -d --build
```

### Установка в среду разработки:

 1. Установите зависимости:
```sh
pip install -r requirements.txt
```
2. Установка postgresql в среду разработки:
  * В папке с проектом есть папка backup_database там файл shop_lisa.backup
  * Открываем pgAdmin 4 
  * Создаем базу данных с именем shop_lisa
  * Делаем востановление базы данных 

3. Выполните миграции:
```sh
python manage.py migrate
```
4. Создание staticfiles
 ```sh
  python manage.py collectstatic
 ```
5. Запустите тестовый сервер c отладчиком:
  ```sh
 python manage.py runserver 7000 --settings=settings.local
 ```
5.1 Запустите релизный сервер:
  ```sh
 python manage.py runserver --settings=settings.prod
 ```
6. Перейдите по ссылке: (http://127.0.0.1:7000)

#### Тестовый суперпользователь:
:lock: Логин: and@riu.by 
:key: Пароль: Admin2022

<details><summary>Проектное задание</summary> 

Разработать сайт интернет-магазина на Django v4.
Будет реализована клиентская часть сервиса и интерфейс администрирования.

### Описание клиентской части

Просмотр товара и добавление в корзину (рядом с каждым товаром будет кнопка добавления товара в корзину).

* Главная страница со статьями о подборке товаров и перечислением этих товаров.
* Страница категории товара со списком товаров.
* Страница товара с подробным описанием.
* Страница аутификации или регистрацией нового пользователя
  
Меню:

* Ссылка на главную страницу.
* Ссылки на разделы (разделы могут иметь иерархию).
* Ссылка на корзину. Кнопка очистки корзины.
* Кнопка входа/выхода в зависимости от статуса авторизации.

Корзина со списком выбранных товаров, привязанных к пользователю.
Кнопка заказа должна создавать заказ и очищать корзину.

Для входа использовать аутентификацию по адресу электронной почты :email:.
 
### Интерфейс администратора

* Редактирование разделов.
* Редактирование товаров.
* Редактирование статей на главной странице и привязывание к ним товаров,
  которые должны отображаться после нее.
* Просмотр списка заказов пользователей, отсортированных по дате создания,
    с указанием пользователя и количества товаров.
* Страница детализации заказа с просмотром списка заказанных товаров.
</details>
