1. Запустить wget https://github.com/alexbel75/apprepo/archive/refs/tags/v1.3.tar.gz в домашнем коталоге пользователя
2. Выполнить команду tar -xvf v1.3.tar.gz
3. Перейти в кталог cd apprepo-1.3/backend
4. Выполнить команду time docker build -t pywebd:v1 .
5. Перейти в каталог apprepo-1.3 
6. Запустить docker compose up -d
Запустить curl http://localhost должен появится ответ Hello from Effective Mobile!
При запуске команды curl http://localhost nginx проксирует на сервис pywebd который вополняет комманду python app.py, 
тем самым запускается приложение и выводится ответ "Hello from Effective Mobile!"
