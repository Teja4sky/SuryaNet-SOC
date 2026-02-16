import numpy as np
from sklearn.ensemble import IsolationForest
from threat_intel import inc

model=IsolationForest(contamination=0.01)

data=[]

def analyze(size):

    data.append([size])

    if len(data)>100:

        model.fit(data)

        pred=model.predict([[size]])

        if pred[0]==-1:

            inc("ai_anomaly")

            print("[SOC ALERT] AI anomaly")
