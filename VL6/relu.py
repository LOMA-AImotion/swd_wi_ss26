# def ReLU 
def relu(x : float) -> float:
    if x < 0:
        return 0
    else: 
        return x
    
for x in range(-10, 11): 
    print(f"x = {x}, ReLU(x) = {relu(x)}")
    
