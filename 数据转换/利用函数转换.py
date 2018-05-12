import numpy as np
import pandas as pd
data = pd.DataFrame({"food":["bacon","pulled pork","bacon",
                          "Pastraml","corned beef","Bacon",
                          "pastrami","honey ham","nova lox"],
                  "ounces":[4,3,12,6,7.5,8,3,5,6]})

print(data)
# 编写一个肉类到动物的映射
meat_to_animal = {
    "bacon":"pig",
    "pulled pork":"pig",
    "pastrami":"cow",
    "corned beef":"cow",
    "honey ham":"pig",
    "nova lox":"salmon"
}
data["animal"] = data["food"].map(str.lower).map(meat_to_animal)
print(data)

data["food"].map(lambda x:meat_to_animal[x.lower()])

