import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# 데이터 만들기 (테스트용 - 여러개 있어야 학습됨)
data = [
	["2026-04-27","14:00",18,120000],
	["2026-04-27","15:00",19,150000],
	["2026-04-27","16:00",20,170000],
	["2026-04-27","17:00",21,200000],
]

df = pd.DataFrame(data, columns = ["date","hour", "temp", "totGain"])

# 시간 숫자로 변환
df["hour"] = pd.to_datetime(df["hour"], format = "%H:%M")
df["hourNum"] = df["hour"].dt.hour

# 입력 /결과 나누기
X = df[["temp", "hourNum"]]
Y = df["totGain"]


# 모델 생성 및 학습
model = RandomForestRegressor()
model.fit(X, Y)

#예측 (온도 18도 , 오후 6시)
predicData = pd.DataFrame([[18,18]], columns = ["temp", "hourNum"])
pred = model.predict(predicData)
# pred = model.predict([[18, 18]])

print("예측매출 : ", pred[0])
