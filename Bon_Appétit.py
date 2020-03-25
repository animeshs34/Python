from functools import reduce
def bonAppetit(bill, k, b):
    error = ((reduce(lambda x,y:x+y,bill) - bill[k])/2)-b
    print("Bon Appetit" if error == 0 else error)