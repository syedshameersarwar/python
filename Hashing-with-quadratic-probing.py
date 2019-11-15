from os import system
def hashing(data):
    slot=data%len(hash_table)
    n=0
    temp=slot
    while hash_table[slot] != None:
        n+=1
        slot+=2*n - 1
        if slot >= len(hash_table):
            slot=slot%len(hash_table)
            
    print(slot)
    hash_table[slot]=data
def display():
    for x in hash_table:
        print(x,end="  ")
def main():
    global hash_table
    hash_table=[None for x in range(5)]
    for i in range(5):
        data=int(input("Enter number data: "))
        hashing(data)
        display()
    display()
main()
system("Pause")
