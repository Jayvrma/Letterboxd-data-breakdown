import matplotlib.pyplot as plt

def decades(movieList):
    dates = '60s or before', '70s','80s','90s','2000s', '2010s', '2020s' 
    movieList = movieList
    decades = {d: [] for d in dates}
    for movie in movieList:
        x = movie.year
        if x<1970: decades['60s or before'].append(movie)
        elif x<1980: decades['70s'].append(movie)
        elif x<1990: decades['80s'].append(movie)
        elif x<2000: decades['90s'].append(movie)
        elif x<2010: decades['2000s'].append(movie)
        elif x<2020: decades['2010s'].append(movie)
        elif x<2030: decades['2020s'].append(movie)
    fig, ax = plt.subplots()
    lenList = [len(decades[d]) for d in dates]
    ax.pie(lenList,labels=dates)
    return fig