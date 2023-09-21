text = input("Ange ett valfritt tal: ")
tal1 = int(text)
text = input("Ange ett till valfritt tal: ")
tal2 = int(text)
text = input("Ange ett sista valfritt tal: ")
tal3 = int(text)
if tal1 < tal2 and tal1 < tal3 and tal2 < tal3:
    print("tal1 tal2 tal3")
elif tal2 < tal1 and tal2 < tal3 and tal1 < tal3:
    print("tal2 tal1 tal3")
elif tal3 < tal1 and tal3 < tal2 and tal1 < tal2:
    print("tal3 tal1 tal2")
    
    

    
    
    
