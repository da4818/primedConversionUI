

def count(n):
    if n%2 == 0:
        response ="even"
    else:
        response = "odd"
    n=n+1
    return response, n

if __name__ == "__main__":
    t = 0;
    resp, t = count(t)
    print (resp)
