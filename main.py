import pandas as pd
from H_index_calculate import getscore 
from dotenv import load_dotenv
import os
from pyairtable import Api
import json

load_dotenv()

api_key = os.getenv("AIRTABLE_API_KEY")
api = Api(api_key)
base_id = "appvtCMw78DSAMOUH"
table_name = "Team1_Preprints"
table = api.table(base_id, table_name)

def style(input):
    output = []
    if input:
        input = input.split(";")
        for ele in input:
            ele = ele.replace(",", "")
            output.append(ele)
    return output

import sys

def process():
    records = table.all()
    num = 0
    for ele in records:
        num += 1
        print(num)
        if "Authors" not in ele["fields"] or ele["fields"]["Authors"] is None:
            # print(json.dumps(ele, indent=2))
            # sys.exit(1)
            ele["total-h-index"] = 0
            continue

        authors = style(ele["fields"]["Authors"])
        score = getscore(authors)
        ele["H-index-score"] = score
        print("到这里了", flush=True)
    return records
        # output.append(score)

# from H_index_calculate import hindex
# records = table.first()
# print(hindex(style(records["fields"]["Authors"])))
# print(style(records["fields"]["Authors"]))
# print(json.dumps(records, indent=2))

# from pprint import pformat
# with open("records_output.json", "w") as f:
#     # f.write(pformat(process()))
#     json.dump(process(), f, indent=2, ensure_ascii=False)


