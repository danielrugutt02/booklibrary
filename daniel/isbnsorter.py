import isbnlib as isbn
from isbnlib import meta
import isbntools
import pyisbn
import pandas as pd
import urllib.request
import time
from isbnlib.registry import bibformatters
import remoteftp as ftp

def update_catalog():
    file = 'updatedlibrarycatalog.csv'
    catalog = pd.read_csv(file)
    regFormat = bibformatters['default']
    provider = 'loc'
    prevMillis = int(round(time.time() * 1000))

    print(catalog.shape)
    print()

    n = 0
    t = 0
    f = 0
    
    
    for isbnNumber in catalog['ISBN']:
        try:
            finalISBN = str(int(isbnNumber))
            cleanISBN = isbn.clean(finalISBN)
            FINAL_ISBN = cleanISBN
            try:
                try:
                    isbnInfo = meta(cleanISBN, service=provider)
                    regFormat(isbnInfo)
                except:
                    print('Library of Congress Service Does Not Work')
                    try:
                        provider = 'goob'
                        isbnInfo = meta(cleanISBN, service=provider)
                        regFormat(isbnInfo)
                    except:
                        print('Google Service Does Not Work')
                        try:
                            provider = 'openl'
                            isbnInfo = meta(cleanISBN, service=provider)
                            regFormat(isbnInfo)
                        except:
                            print('OpenL Service Does Not Work')
                            raise ValueError()
            except:
                print("ISBN13 Num Does Not Work")
                tempValue = catalog.loc[catalog['ISBN'] == isbnNumber]['ISBN_10'].values
                isbn10Num = tempValue[0]
                finalISBN10 = str(int(float(isbn10Num)))
                cleanISBN10 = isbn.clean(finalISBN10)
                FINAL_ISBN = cleanISBN10
                try:
                    provider = 'loc'
                    isbnInfo = meta(cleanISBN10, service=provider)
                    regFormat(isbnInfo)
                except:
                    print('Library of Congress Service Does Not Work')
                    try:
                        provider = 'goob'
                        isbnInfo = meta(cleanISBN10, service=provider)
                        regFormat(isbnInfo)
                    except:
                        print('Google Service Does Not Work')
                        try:
                            isbnInfo = meta(cleanISBN10, service='openl')
                            regFormat(isbnInfo)
                        except:
                            print('OpenL Service Does Not Work')
                            websiteURL = "https://isbnsearch.org/search?s=" + cleanISBN
                            website = urllib.request.urlopen(websiteURL)
                            mybytes = website.read()
                            dataFromWebsite = mybytes.decode("utf8")
                            website.close()
                            print(dataFromWebsite)
                            raise ValueError()

            print(regFormat(isbnInfo))

            n = n + 1

            catalog.loc[t, 'ISBN'] = isbnNumber

            bookTitle = isbnInfo['Title']
            catalog.loc[t, 'Title'] = bookTitle

            bookLanguage = isbnInfo['Language']
            catalog.loc[t, 'Language'] = bookLanguage

            bookPublisher = isbnInfo['Publisher']
            catalog.loc[t, 'Publisher'] = bookPublisher

            bookYear = isbnInfo['Year']
            catalog.loc[t, 'Year'] = bookYear

            bookAuthor = isbnInfo['Authors'][0]
            catalog.loc[t, 'Authors'] = bookAuthor

            try:
                bookDesc = isbn.desc(FINAL_ISBN)
                catalog.loc[t, 'Description'] = bookDesc
            except:
                print('Could not extract book description')

            try:
                bookCover = isbn.cover(FINAL_ISBN)
                catalog.loc[t, 'Cover'] = bookCover['thumbnail']
            except:
                print('Could not extract book cover link')

        except:
            print("This ISBN Number is NOT Valid")
            f = f + 1
        t = t + 1
        currentMillis = int(round(time.time() * 1000))
        if currentMillis - prevMillis >= 60000:
            print("Saving File to Local and Remove Server")
            catalog.to_csv('updatedlibrarycatalog.csv')
            ftp.push_file_to_server()
            prevMillis = int(round(time.time() * 1000))
            print("File has Successfully Saved")
        print("\n")

    print('Total Number of Books: ' + str(t))
    print('Successful Books: ' + str(n))
    print('Unsuccessful Books: ' + str(f))
