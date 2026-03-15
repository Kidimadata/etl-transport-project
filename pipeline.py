import pandas as pd
from sqlalchemy import create_engine

# 1. Excel-bestand lezen
df = pd.read_excel("transport_dataset.xlsx")

# 2. Eenvoudige opschoning
df = df.dropna(how="all")
df.columns = df.columns.str.strip()

# 3. De eerste onnodige rij verwijderen
df = df.iloc[1:]

# 4. Kolommen hernoemen
df.columns = [
    "transport_id",
    "date",
    "driver_name",
    "vehicle_type",
    "route",
    "distance_km",
    "fare_eur"
]

# 5. Datatypes omzetten
df["transport_id"] = pd.to_numeric(df["transport_id"], errors="coerce")
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["distance_km"] = pd.to_numeric(df["distance_km"], errors="coerce")
df["fare_eur"] = pd.to_numeric(df["fare_eur"], errors="coerce")

# 6. Ongeldige rijen verwijderen
df = df.dropna(subset=["transport_id", "date", "driver_name"])

# 7. Voorbeeld van de data bekijken
print("Data na opschonen:")
print(df.head())

# 8. Verbinding maken met PostgreSQL
engine = create_engine(
    "postgresql+psycopg2://postgres:kidimaTukadi@_12@localhost:5432/transport_db"
)

# 9. Data naar PostgreSQL sturen
df.to_sql("transport_data", engine, if_exists="replace", index=False)

print("Data succesvol naar PostgreSQL verzonden.")
