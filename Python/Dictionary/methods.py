dic = {
    "Name" : "Aryan",
    "Age" : 19,
    "City" : "Ahmedabad",
    "Branch" : "IT",
    "SPI" : 9.9
}

dic2 = {
    "College" : "VGEC",
    "Cid" : 17,
}

dic.update( {"Age":20} )    # can change existing data from dictionary
print(dic)

dic.update( {"Grade":"AA"} )    # can add new data in dictionary
print(dic)

dic.update(dic2)    # can add an entire dictionary in one dictionary
print(dic)

dic2.clear()    # empties dictionary
print(dic2)

dic.pop("Cid")  # removes desired element from dictionary
print(dic)

dic.popitem()   # removes last element 
print(dic)

del dic      # deletes entire dictionary
