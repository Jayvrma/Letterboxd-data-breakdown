import csv 

from dataclasses import dataclass
@dataclass
class Movie:
    date:str
    name:str
    year:int
    url:str

watched = "watched.csv"
rows = []
movies= []

with open(watched, 'r') as csvfile:
    csvReader = csv.reader(csvfile)
    fields = next(csvReader)
    for row in csvReader:
        rows.append(row)
for row in rows:
    movies.append(Movie(row[0],row[1],row[2],row[3]))

def getMovieList():
    return movies

# for movie in movies:
#     print(movie)
