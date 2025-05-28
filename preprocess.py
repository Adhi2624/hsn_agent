from chromaclient.chromaclient import Chroma
import pandas as pd
client=Chroma()

df=pd.read_csv(r"data/HSN_SAC.xlsx - HSN_MSTR.csv")
code=df['HSNCode'].to_list()
description=df['Description'].to_list()

client.addDatas(code=code,description=description)
client.getDatas(description=description[5])