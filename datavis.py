import matplotlib.pyplot as plt
from watched import getMovieList
dates = '60s or before', '70s','80s','90s','2000s', '2010s', '2020s' 
movieList = getMovieList()
decades = {
    '60s or before':[],
    '70s':[],
    '80s':[],
    '90s':[],
    '2000s':[],
    '2010s':[],
    '2020s':[]
}
for movie in movieList:
    x = int(movie.year)
    if x<1970: decades['60s or before'].append(movie)
    elif x<1980: decades['70s'].append(movie)
    elif x<1990: decades['80s'].append(movie)
    elif x<2000: decades['90s'].append(movie)
    elif x<2010: decades['2000s'].append(movie)
    elif x<2020: decades['2010s'].append(movie)
    elif x<2030: decades['2020s'].append(movie)
fig, ax = plt.subplots()
lenList = [len(decades['60s or before']),len(decades['70s']),len(decades['80s']),len(decades['90s']),len(decades['2000s']),len(decades['2010s']),len(['2020s'])]
ax.pie(lenList,labels=dates)
plt.show()
