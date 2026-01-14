 Deribit Crypto Prices API

 Описание

Проект реализует API для получения цен криптовалют (BTC и ETH) с биржи Deribit и их сохранения в базу данных PostgreSQL.  
Данные собираются каждые 60 секунд через фоновую задачу. API позволяет получать:

- все сохранённые данные по указанной валюте
- последнюю цену валюты
- данные с фильтром по времени

---

 Стек технологий

- Python 3.11+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Celery
- requests
- dotenv

---

 Установка и запуск

1. Клонируем репозиторий:
```bash
git clone https://github.com/18shadow20/Deribit_api
cd Deribit_api
```
2 Создаём виртуальное окружение и устанавливаем зависимости:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

pip install -r requirements.txt

```
3. Создаём .env файл:
```bash
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
DERIBIT_API_KEY=<ключ>
```
4. Запуск FastAPI:
```bash
uvicorn main:app --reload
```

5. Фоновая задача через Celery
```bash
celery -A celery_app worker -l info
celery -A celery_app beat -l info
```

Endpoints
1. Получение всех данных
```bash
http://127.0.0.1:8000/alldata?ticker=ETH_USD
http://127.0.0.1:8000/alldata?ticker=BTC_USD
```
2. Получение последней цены
```bash
http://127.0.0.1:8000/lastticker?ticker=ETH_USD
http://127.0.0.1:8000/lastticker?ticker=BTC_USD
```
3. Получение данных по фильтру времени
```bash
http://127.0.0.1:8000/filterdatas?ticker=btc_usd&from_time=1768330752&to_time=1768330760
http://127.0.0.1:8000/filterdatas?ticker=eth_usd&from_time=1768330752&to_time=1768330760
```

Design Decisions

```bash
FastAPI выбран для быстрого создания REST API с современным подходом зависимостей.
SQLAlchemy ORM обеспечивает простую работу с PostgreSQL.
Celery используется для периодического получения данных в фоне.
Все операции с БД выполняются через сессии SQLAlchemy, без глобальных переменных, что предотвращает утечки соединений.
Цена хранится как Numeric(20,8) для точного представления валютных значений.
```








