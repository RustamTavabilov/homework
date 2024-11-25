calls = 0
def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    count_calls()
    tuple_ = (len(string), string.upper(), string.lower())
    print(tuple_)

def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
        j=0
    while j < len(list_to_search):
        if list_to_search[j] == string:
            c = True
            break
        else:
            j = j + 1
            c = False
    print(c)


string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)