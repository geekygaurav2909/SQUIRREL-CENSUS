import pandas as pd

color_data = pd.read_csv("Squirrel_Data.csv")

gray_squirrels = len(color_data[color_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(color_data[color_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(color_data[color_data["Primary Fur Color"] == "Black"])


color_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]
}

color_df = pd.DataFrame(color_dict)
color_df.to_csv("Squirrel_count.csv", index= False)