# collection mulitple values means ____  (# collecting multiple values in a single variable)

# list {} ordered and changeable duplicate okay !
# set []    unordered and immutable , but add and remove okay !! but no duplicate 
# tuple ()  ordered and un changeable duplicate okay  faster  !

# eg ::

def list():
    fruits=["mango"  ,  "apple"     ,"oraange","banana"]

    # you chnage change a set like ::
    fruits[0]="grape"
    # we can append or add a value to a list 
    fruits.append(" black , white gorok")
    #we can remove somethng from a list using :
    fruits.remove("apple")
    # we can insert a value by using insert on a given value
    fruits.insert(4, "mobile")
    # we can sort item alpabtely by using sort 
    fruits.sort()
    # we can reverse the alpabtely order  by using reverse if used sort 
    # if not they will be reversed by the input of your list

    fruits.reverse()
    for fruit in (fruits):
    
        print(fruit, sep="")
list()







def set():
    fruit={"mango"  ,  "apple"     ,"oraange","banana"}
    # unordered and immutable , but add and remove okay !! but no duplicate 
    # but you can  use : (add) , (len) , (in), (remove) , (clear)
    # eg::
    fruit.add(" grape")
    fruit.pop()
    fruit.remove(" apple")
    # fruit.clear()

    for x in (fruit):
        
            print(x, sep="")
set()





def tuple():
    fruittt=("mango"  ,  "apple"     ,"oraange","banana")
   #ordered and un changeable duplicate okay  faster  !
       #  we only have count and index for typel
    
    print(fruittt.index(" apple"))
    print(fruittt.count(" oraange"))

tuple()