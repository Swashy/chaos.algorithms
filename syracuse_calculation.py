import time
outfile = open("calculations", "w")

def syracuse(n):
    #print("\nCalculating", n)
    counter = 0
    number = n
    while n > 1:
        if (n%2 == 0) and (n != 1):
            n = n//2
            counter +=1
        elif n !=1:
            n = 3*n + 1
            counter +=1
        else: break
    global outfile
    toWrite = "Calculated " + str(number) + " with " + str(counter) + " calculations\n"
    outfile.write(toWrite)

def main():
    global outfile
    for i in range(9000):
        syracuse(i+2)
    print("Finished.")
    time.sleep(3)
    outfile.close()
    return

main()
