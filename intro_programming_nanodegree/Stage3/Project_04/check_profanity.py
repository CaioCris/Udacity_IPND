from urllib import request, parse

def read_text():
    quotes = open("/home/caio-cris/Projetos/Udacity/intro_programming_nanodegree/Stage3/Project_04/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = request.urlopen("http://www.wdylike.appspot.com/?q="+parse.quote(text_to_check))
    output = connection.read().decode('UTF-8')
    print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")
        
read_text()