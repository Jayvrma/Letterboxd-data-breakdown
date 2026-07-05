import csv 
import io
from dataclasses import dataclass

@dataclass
class Movie:
    date:str
    name:str
    year:int
    url:str

def getMovieList(file):
    movies= []
    content= file.getvalue().decode('utf-8')
    csvReader = csv.reader(io.StringIO(content))
    next(csvReader)
    for row in csvReader:
        movies.append(Movie(row[0],row[1],int(row[2]),row[3]))
    return movies
