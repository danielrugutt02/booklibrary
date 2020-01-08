import numpy as np
import pandas as pd



def search(request):
    context = {}
    html_return = ""
    search_query = request
    data = pd.read_csv('..\static\data\\bookDataOriginal.csv')
    count = 1

    for x in range(0,len(data) - 1):
        if data.loc[x,"Title"] == search_query:
            context["book" + str(count)] = {
                "Title": data.loc[x,"Title"],
                "Accession No": data.loc[x,"Accession No"]
            }
            html_return += "<tr><td style='width:60%;text-align: center'>"
            html_return += str(data.loc[x,'Title'])
            html_return += "</td><td style = 'width:40%; text-align: center'>"
            html_return += str(data.loc[x,'Accession No'])
            html_return += "</td></tr>"
            count += 1
    if html_return == "":
        print("NO RESULT FOUND")
    else:
        print(html_return)
