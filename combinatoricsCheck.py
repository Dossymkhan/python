def permute(arr, f, l):
    if f == l:
        print(arr)
    else:
        for i in range(f, l + 1):
            arr[f], arr[i] = arr[i], arr[f]
            permute(arr, f + 1, l)
            arr[f], arr[i] = arr[i], arr[f] 
string = "ABC"
n = len(string)
arr = list(string)
permute(arr, 0, n-1)
