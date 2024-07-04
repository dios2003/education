def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    x = inner_function()
    return


test_function()
inner_function()
