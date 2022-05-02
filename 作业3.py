import nmupy as np
import pandas as pd

df = pd.Dataframe(np.array(1,Bulbasaur,Grass,Poison,318,45,49,49,65,65,45,1,False,
2,Ivysaur,Grass,Poison,405,60,62,63,80,80,60,1,False,
3,Venusaur,Grass,Poison,525,80,82,83,100,100,80,1,False,
3,VenusaurMega Venusaur,Grass,Poison,625,80,100,123,122,120,80,1,False,
4,Charmander,Fire,309,39,52,43,60,50,65,1,False).reshape(4,12), index=[1, 2, 3, 4],
                  column=["Name", "Type1", "Type2", "Total", "HP", "Attack", "Defense", "Sp.Akt", "Sp.Def", "Speed",
                          "Generation", "legendary"])
print(df)