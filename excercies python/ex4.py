def find(list_,num_):
    for num in list_:
        if num == num_:
            return [True,list_.index(num)]
    return False        
    
    
    
    '''if num in list_:
        return True
    return False'''

print(find([1,2,3,4,5],4))
