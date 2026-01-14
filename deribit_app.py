import os
from dotenv import load_dotenv
import requests
import time
from database import SessionLocal, CryptoPrice

load_dotenv()


deribit_key = os.getenv("DERIBIT_API_KEY")
url = "https://test.deribit.com/api/v2/public/get_index_price"

def get_index_price_btc():
    response_btc = requests.get(url, params={
        "index_name":"btc_usd"
    })
    return response_btc.json()["result"]["index_price"]

def get_index_price_eth():
    response_eth = requests.get(url, params={
        "index_name": "eth_usd"
    })
    return response_eth.json()["result"]["index_price"]


def add_db():
    db = SessionLocal()
    price_btc = CryptoPrice(
        ticker = "BTC_USD",
        price = get_index_price_btc(),
        timestamp = int(time.time())

    )
    price_eth = CryptoPrice(
        ticker = "ETH_USD",
        price = get_index_price_eth(),
        timestamp = int(time.time())
    )

    db.add_all([price_btc, price_eth])
    db.commit()
    db.close()





