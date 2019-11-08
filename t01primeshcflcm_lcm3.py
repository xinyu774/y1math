# Find the LCM of two numbers
def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1

    return lcm

def get_lcm_for(your_list):
    return reduce(lambda x, y: lcm(x, y), your_list)

ans = get_lcm_for([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(ans)
