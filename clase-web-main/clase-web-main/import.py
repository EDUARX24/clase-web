import csv
import os

from sqlalchemy import create_engine,  text
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:DLldnWRGjzqy6b7CD9Ms@containers-us-west-169.railway.app:5968/railway")
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("flights.csv")
    reader = csv.reader(f)
    for origin, destination, duration in reader:
        ist = text("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)")
        
        print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
        db.execute(ist, {"origin": origin, "destination":destination, "durations":duration})
    db.commit()

if __name__ == "__main__":
    main()