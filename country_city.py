from restaurant import User
from ice_cream import Admin

a1 = Admin('ben', 'lam', 60)


def cityplace(country, city, population = ''):
    if population:
        return(f'{country}, {city}, {population}')
    else:
        return(f'{country}, {city}')


def makeAlbum(artist, song, tracks = ''):
    if tracks:
        cover = {artist:song, 'tracks':tracks}
    else:
        cover = {artist:song}
    return(cover)

# while True:
#     x = input('what is the artist name ')
#     if x == 'q':
#         break
#     y = input('what is the name of the song ')
#     if y == 'q':
#         break
#     z = input('how many tracks? ')
#     if z == 'q':
#         break
    
#     makeAlbum(x,y,z)    

def printWord():
    print('sucessfully imported')





