#Accessing values in the lists
movie_titles = [
	"Eternal Sunshine of the Spotless Mind",
	"Memento",
	"Requiem for a Dream",
	"Time Travel",
	"Godfather",
	"Gorzilla",
	"Up"
]
print(movie_titles)
print("\n movie_titles[0]  " + movie_titles[0] )
print("\n movie_titles[-1]  " + movie_titles[-1] )
print("\n movie_titles[-2] " + movie_titles[-2] )
#print("\n movie_titles[7] " + movie_titles[7] )

#Appending value in the list
names = ["John", "Alice", "Sarah", "George"]
names.append("Simon")
print(names)
names = names + ["Poll"]
print(names[-1] )
print(names)

 #insert method adding middle in the lists
numbers = [1, 2, 4, 5]
print(numbers)
numbers.insert(2, 3)
print(numbers)
numbers.insert(8, 8)
print(numbers)

#Exercises:
#Create a movies list containing a single tuple. 
movies = ["Memento", "Christopher Nolan", 2000, "$50,000,000"]

#The tuple should contain a movie title, the director’s name, the release year of the movie, and the movie’s budget.
new_movie_title = input("Enter your favoutite Movie name?")
print("Movie name: " + new_movie_title)

new_director = input("Enter movie Director name?")
print("Director name: " + new_director)

new_year_release = int(input("Enter release year of the movie: "))
print(new_year_release)

new_budget = input("Enter Budget of that movie: ")
print(new_budget)

#Create a new tuple from the values you gathered using input. Make sure they’re in the same order as the tuple you wrote in the movies list.
new_movie = (new_movie_title,  new_director, new_year_release, new_budget)
print(new_movie)

#Use an f-string to print the movie name and release year by accessing your new movie tuple.
print(f"{new_movie_title} ({new_year_release})")

#Add the new movie tuple to the movies collection using append.
movies.append(new_movie)

#Print both movies in the movies collection
print(movies[0])
print(movies[1])

#Remove the first movie from movies. Use any method you like.
del movies[0]
print(movies)