calls = 0


def count_calls():
    global calls
    calls += 1
    return


def string_info(string):
    global calls
    _str = (len(string), string.upper(), string.lower())
    count_calls()
    return _str


def is_contains(string,list_to_search):
    global calls
    count_calls()
    for i in range(0, len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    if string.lower() in list_to_search[i].lower():
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
