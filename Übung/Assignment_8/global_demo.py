global_var = 10

def test_func():
    global global_var
    global_var = 11
    print(global_var)

test_func()
print(global_var)