"""
Chapter 1 : Exercise 10 : Film Dictionary

Writing a program that creates a dictionary, the dictionary contains relevant data for films. Ex: Director, Title, etc.
Then printing the dictionary of the film details using loops.

"""

# start of the program

# creating the dictionary with the film details
film_dictionary = {
    'Title':'Taxi Driver', 'Directors':'Park Joon-Woo, Lee-Dan', 'Writers':'Oh Sang-Ho, Lee Ji-Hyun', 
    'Producer':'Studio S, Creative Leaders Group Eight', 'Cast-Member 1':'Lee Jehoon (Kim Do Gi)', 
    'Cast-Member 2':'Kim Eui-Sung (Jang Sung Chul)', 'Cast-Member 3':'Pyo Ye-Jin (Ahn Go Eun)',
    'Cast-Member 4':'Jan Hyuk-Jin (Choi Kyung Goo)', 'Cast-Member 5':'Yoo-Ram Bae (Park Jin Eon)', 
    'Country':'South Korea', 'Genre':'Crime, Thriller, Action, Revenge', 'IMDB Rating':'8.0/10', 
    'Release Date':'Season-1 : 9 April, 2021, Season-2 : 17 February, 2023',
    'Number of Seasons':'2', 'Episodes':'16 (per season)'}

# using for loop to print the key, values in the dictionary, .items() to display all items
for key, value in film_dictionary.items():
    print(f"\n {key} ----- {value}")


# end of the program