class Movie:
    movieID = 0
    def __new__(cls, *args, **kwargs):
        instantObj = object.__new__(cls)
        cls.movieID +=1
        return instantObj

    def __init__(self, movieName, director, movieExpenses, actorSalary, *actors):
        self.movieName = movieName
        self.director = director
        self.movieExpenses = movieExpenses
        self.actorSalary = actorSalary
        self.actorsList = list(actors)

        print(f'The movie id: {self.movieID} and movie name is: {self.movieName}')

    def __str__(self):
        return f'Movie name: {self.movieName}, \nMovie director: {self.director}, \nBudget: {self.movieExpenses}'

movie1 = Movie('Eternals', 'Chloe Zhou', 300000000, 7800000, 'Angelina Jolie', 'Brad Pitt')
print(movie1)


