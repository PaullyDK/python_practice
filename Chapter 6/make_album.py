def make_album(artist_name, album_title, number_of_songs=None):
    album = {'artist name': artist_name, 'album title': album_title}
    if number_of_songs:
        album['number of songs'] = number_of_songs
    return album

stop = False
while stop == False:
    artist_name = input("What is the name of the artist? ")
    album_title = input("What is the title of the album? ")
    
    choice = input("Would you like to add the number of songs? (yes/no) ")
    if choice.lower() == 'yes':
        number_of_songs = int(input("How many songs? "))

        print(make_album(artist_name, album_title, number_of_songs))
    else:
        print(make_album(artist_name, album_title))

    continue_or_stop = input("Would you like to enter another? (yes/no) ")
    if continue_or_stop.lower() == 'no':
        stop = True