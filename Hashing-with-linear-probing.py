from os import system
def hashing(data):
    slot=data%len(hash_table)
    print(slot)
    while hash_table[slot] != None: 
        if slot < len(hash_table)-1:
            slot+=1
        else:
            slot=0
    print(slot)
    hash_table[slot]=data
def display():
    for x in hash_table:
        print(x,end="  ")
def main():
    global hash_table
    hash_table=[None for x in range(11)]
    for i in range(5):
        data=int(input("Enter number data: "))
        hashing(data)
    display()
main()
system("Pause")
    

