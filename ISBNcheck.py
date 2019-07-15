weightedsum = 0
weights = input("Enter weights in [x,x,x,x,x,x,x,x,x,x,x,x] format:")
weightslst = weights[1:-1].split(",")
isbn = input("The ISBN no. to check is : ")
end = False
while isbn != "q":
    while len(isbn) != 17 or ((isbn[0:3]+isbn[4]+isbn[6:9]+isbn[10:15]+isbn[-1]).isdigit() == False or (isbn[3]+isbn[5]+isbn[9]+isbn[16]) == "----"):
        if isbn == "q":
            end = True
            break
        else:
            print("ISBN input format is incorrect.")
            isbn = input("The ISBN no. to check is : ")

    if end == True:
        break
    
    theisbn = isbn[0:3]+isbn[4]+isbn[6:9]+isbn[10:15]

    for i in range(len(theisbn)):
        weightedsum += int(theisbn[i])* int(weightslst[i])

    remainder = weightedsum % 10
    if remainder == 0:
        check = 0
    else:
        check = 10 - remainder

    print("Weighted sum is: ",weightedsum)
    print("Calculated check digit: ",check)

    if check == int(isbn[-1]):
        print("The ISBN number is correct.")
    else:
        print("The ISBN number is incorrect.")
        
    isbn = input("The ISBN no. to check is : ")

