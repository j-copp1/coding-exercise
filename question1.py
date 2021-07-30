def scramble(arr) :

    #sort to ascending, if already ascending no change
    arr.sort()

    #scramble 1st way
    i = 0
    while i < len(arr) and i + 1 != len(arr):
        
        arr[i], arr[i + 1] = arr[i+1], arr[i]
        i = i + 2


    #scramble 2nd way
    t1, t2 = arr[len(arr) - 2], arr[len(arr) - 1] 
    arr[len(arr) - 2], arr[len(arr) - 1] = arr[0], arr[1]
    arr[0], arr[1] = t1, t2

    return arr

def unscramble(arr) :

    #unscramble 2nd way 
    t1, t2 = arr[len(arr) - 2], arr[len(arr) - 1] 
    arr[len(arr) - 2], arr[len(arr) - 1] = arr[0], arr[1]
    arr[0], arr[1] = t1, t2

    #unscramble 1st way
    i = 0
    while i < len(arr) and i + 1 != len(arr):
        
        arr[i], arr[i + 1] = arr[i+1], arr[i]
        i = i + 2
    return arr

def main():
    e = False
    while e != True :
        print('Enter sorted array to be scrambled (Format: 7 13 13 18 29 33)')
        print('Enter \'e\' to exit program')
        i = input('-> ')

        if i == 'e':
            print('Thanks for using this program!')
            break
        else :
            try :
                arr = [int(val) for val in i.split()]
                arr.sort()
                print('\nOriginal array    :', arr)
                print('Scrambled array   :', scramble(arr))
                print('Unscrambled array :', unscramble(arr),'\n')
            except :
                print('Incorrect format')

if __name__ == "__main__":
    main()