from django.shortcuts import render
import numpy as np
import pandas as pd

# Create your views here.
def index(request):
    """View function for home page of site."""

    # # Generate counts of some of the main objects
    # num_books = Book.objects.all().count()
    # num_instances = BookInstance.objects.all().count()
    
    # # Available books (status = 'a')
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # # The 'all()' is implied by default.    
    # num_authors = Author.objects.count()

    context = {

    }
    
    # data = pd.read('bookManager\static\data\bookDataOriginal.csv')
    # for row in data: 
    #     for info in row:
            

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def login(request):
    context = {

    }
    return render(request, 'login.html', context=context)

def search(request):
    context = {}
        
    return render(request, 'search.html', context)

def book(request):
    return render(request, 'books.html')

def viewBook(request):
    info = request.POST['data']
    data = pd.read_csv('bookManager\static\data\\bookDataOriginal.csv')
    matchedBook = {}
    allbooks = {}
    strSearch = "'AccessionNo': "
    startIndex = info.find(strSearch) + len(strSearch)
    endIndex = info.find("}')")
    accessionString = info[startIndex: endIndex]

    accessionNo = int(accessionString)

    for x in range(0,len(data) - 1):
        if(data.loc[x,'Accession No'] == accessionNo):
            matchedBook = data.loc[x]

    allbooks["book"] = matchedBook
    
    context = {'allbooks': allbooks}

    return render(request, 'viewBook.html', context)

def submit(request):
    allbooks = {}
    context = {}
    info=request.POST['info']
    data = pd.read_csv('bookManager\static\data\\bookDataOriginal.csv')
    count = 1

    if(info == ""):
        pass
    else:
        for x in range(0,len(data) - 1):
            if data.loc[x,"Title"].lower().find(info.lower()) != -1:            
                allbooks["book" + str(count)] = {
                    'Title': data.loc[x,"Title"],
                    'AccessionNo': data.loc[x,"Accession No"]
                }
                count += 1   
        if not allbooks:
            allbooks = {'book': {'Title': 'No book found with title: ' + str(info),'Accession No:': 'N/A'}}
        

        context = {'allbooks': allbooks}
    return render(request, "search.html", context)
