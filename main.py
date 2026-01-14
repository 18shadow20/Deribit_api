from fastapi import FastAPI, Depends
from database import SessionLocal, CryptoPrice
from sqlalchemy.orm import Session

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/alldata")
def all_datas(ticker:str, db: Session = Depends(get_db)):
    datas = db.query(CryptoPrice).filter(CryptoPrice.ticker == ticker.upper()).all()
    return {
        "datas": [
            {
                "ticker": d.ticker,
                "price": float(d.price),
                "timestamp": d.timestamp
            }
            for d in datas
        ]
    }

@app.get("/lastticker")
def last_tickers(ticker:str, db: Session = Depends(get_db)):
    last_data = (db.query(CryptoPrice).filter(CryptoPrice.ticker == ticker.upper())
                                      .order_by(CryptoPrice.timestamp.desc())
                                      .first()
                 )
    return {
        "ticker": last_data.ticker,
        "price": float(last_data.price),
        "timestamp": last_data.timestamp
    }


@app.get("/filterdatas")
def filter_tickers(ticker:str, from_time:int, to_time:int, db: Session = Depends(get_db)):
    filter_datas = (db.query(CryptoPrice).filter(CryptoPrice.ticker == ticker.upper(),
                    CryptoPrice.timestamp >= from_time,
                    CryptoPrice.timestamp <= to_time
                    )
                    .order_by(CryptoPrice.timestamp)
                    .all()
                )
    return {"filter_datas": [
            {
                "ticker": d.ticker,
                "price": float(d.price),
                "timestamp": d.timestamp
            }
            for d in filter_datas
        ]}


