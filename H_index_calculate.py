import requests
from scholarly import scholarly
import json

base_url = "https://api.openalex.org/authors"

def hindex(author_name):
    result = []
    for name in author_name:
        params = {"search": name}
        response = requests.get(base_url, params=params, timeout=10)

        if response.status_code != 200:
            print(f"fail: {response.status_code}")
            return None
        
        data = response.json()
        val = data.get("results", [])

        #not find in openAlex --> search in google sholar
        if not val:
            # print("not found2")
            h_index = check(name)
            # print(h_index)
        else:
            works_count = val[0].get("works_count",0)
            # with open("records_output.json", "w") as f:
            #     json.dump(val[0], f, indent=2, ensure_ascii=False)
            if works_count > 50000:
                h_index = check(name)
            else:
                h_index = val[0]["summary_stats"].get("h_index", None)
        result.append(h_index)
    return result

def check(name):
    search_query = scholarly.search_author(name)
    try:
        #only one return
        author = next(search_query)
        filled_author = scholarly.fill(author, sections=['basics', 'indices'])
        h_index = filled_author.get("hindex")
        #severa returns

    except:
        h_index = 0

    return h_index

def weight(n):
    base = [1 / (i + 1) for i in range(n)]
    total = sum(base)
    weights = [x / total for x in base]
    return weights

def overall(index_list):
    weights = weight(len(index_list))
    score = sum(h*w for h, w in zip(index_list, weights))
    return score

def getscore(input):
    return overall(hindex(input))

# print(hindex(["Owen Patterson"]))