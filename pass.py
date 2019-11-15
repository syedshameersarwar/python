'''
import getpass
password = getpass.getpass('Password:')
print(password)

'''
import msvcrt


def getPassInput(string="Enter User Pass (Max Length= 30): "):

    print(string)
    char =  msvcrt.getwch()
    i=0
    text = ''
    while (char != '\r'):
  
        if char == '\b':
            if i>0:
                print('\b \b',end = '',flush=True)
                text = text[:-1]
        else:
            print('*',end = '',flush=True)
            text+= char
        i+=1
        char = msvcrt.getwch()
    return text




def validatePass(password):

    for c in password:
        if not(32<=ord(c)<=126):
            return False
    return True
        


if __name__ == '__main__':
    getPassInput()
