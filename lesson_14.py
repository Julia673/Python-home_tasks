from functools import wraps

# task 1

def logger(func):
    def name_fun(*args, **kwargs):
        
        print (func.__name__+" called with",*args, **kwargs)
        return func(*args, **kwargs)
    return name_fun

@logger

def add(x, y):

    return x + y

@logger

def square_all(*args):

    return [arg ** 2 for arg in args]

add(3, 4)
square_all(1,2,3,4,5)

# task 2

def stop_words(words):
    
    def inner_function(function):
       @wraps(function)
       def wrapper(*args):
        slogan=function(*args).split()
        for ind in range (len(slogan)):
            if (words.count(slogan[ind]) ):
                slogan[ind]='*'
        slogan_2=' '.join(slogan)
        print(slogan_2)
        return function(*args)
       return wrapper
    return inner_function

@stop_words(['pepsi', 'BMW'])
def create_slogan(name):

    return f"{name} drinks pepsi in his brand new BMW !"

create_slogan('Steve') 

# task 3

def arg_rules(type_wor, max_length, contains):
    
     
    def inner_function(function):
       @wraps(function)
       def wrapper(word):
        count=0
        for i in contains:
            if word.find(i)!=-1:
                count+=1
        if len(word)>max_length or type(word)!= type(type_wor(word)) or count!=len(contains):
             print('is False')   
        else:
            print(function(word))
        return function(word)
       return wrapper
    return inner_function


@arg_rules(str,15,['05', '@'])

def create_slogan(name):

    return f"{name} drinks pepsi in his brand new BMW!"

create_slogan('johndoe05@gmail.com') #is False

create_slogan('S@SH05') #'S@SH05 drinks pepsi in his brand new BMW!'