# Incomplete app!

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


# You may want to create a function for this code
def add_movies():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    movies.append({
    'title': title,
    'director': director,
    'year': year
    })
#   - listing movies
def list_movies():
    for i in movies:
        print(f'movie name: {i['title']}')
        print(f'director name: {i['director']}')
        print(f'year: {i['year']}')

#   - finding movies
def find_movies():
    title = str(input("Enter a movie title: "))
    for i in movies:
        if i['title'] == title:
            print(i['title'])
        else:
            print('movie not found')

# And another function here for the user menu
def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == "a":
            add_movies()
        elif selection == "l":
            list_movies()
        elif selection == "f":
            find_movies()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)

menu()

# Remember to run the user menu function at the end!
