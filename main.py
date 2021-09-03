import pandas as pd
import os

if __name__ == '__main__':
    trucks = os.listdir("resources/csv")
    for truck in trucks:
        for truck_data in os.listdir("resources/csv/" + truck):
            data = pd.read_csv("resources/csv/" + truck + "/" + truck_data, ';', decimal=',')
            data.to_json(r"resources/json/" + truck_data.replace(".csv", ".json"))
