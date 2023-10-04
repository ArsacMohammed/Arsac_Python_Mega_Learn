import pandas as pd



filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
df = pd.read_csv(filename, sep=",", skiprows=20, parse_dates=["    DATE"])
print(df.head(5))
print(filename)