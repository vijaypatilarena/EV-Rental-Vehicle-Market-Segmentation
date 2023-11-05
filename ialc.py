import pandas as pd
import matplotlib.pyplot as plt

data = {
    "State/UT": ["Andaman and Nicobar Island", "Arunachal Pradesh", "Assam", "Bihar", "Chandigarh", "Chhattisgarh", "Delhi", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Ladakh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Puducherry", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Tripura", "Dadra and Nagar Haveli and Daman and Diu", "Uttarakhand", "Uttar Pradesh", "West Bengal"],
    "Total EVs (08.12.2021)": [157, 20, 43707, 58655, 1791, 11998, 126111, 1315, 13270, 24379, 623, 1334, 11060, 72018, 12109, 6, 52159, 519, 31, 18, 53, 10001, 1393, 8190, 47480, 22, 45368, 7146, 123, 23524, 258105, 43432]
}

df = pd.DataFrame(data)
df = df.sort_values(by="Total EVs (08.12.2021)", ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(df["State/UT"], df["Total EVs (08.12.2021)"])
plt.xlabel("State/UT")
plt.ylabel("Total EVs as of 08.12.2021")
plt.title("Geographic Segmentation of Active Electric Vehicles")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.show()
most_suitable_location = df.iloc[0]["State/UT"]
print("Most Suitable Location for Early Market: ", most_suitable_location)
