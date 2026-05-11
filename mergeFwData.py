import pandas as pd

# data of original sales
sales = pd.read_csv("sales.csv")

# data of weather sample
weather = pd.DataFrame(
[
{
	"date" : "2026-04-27",
	"time" : "14:00",
	"temp" : 18,
	"humy" : 50,
	"winspd" : 2.1
}
]
)

#merge data
df = pd.merge(weather, sales, on=["date","time"])

print(df)
