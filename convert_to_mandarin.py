trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):
    num = int(us_num)
    if num  in range(11):
        return trans[str(num)]
    elif  num in range(11,20):
        return trans['10']+' '+ trans[str(num%10)]
    else:
        result = trans[str(num//10)]+' '+trans['10']
        if num%10 != 0:
            return result + ' '+trans[str(num%10)]
        else:
            return result
    

print(convert_to_mandarin('75'))
        
