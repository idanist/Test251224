from app import*

def most_expensive(diamonds_ar):
    
    highest_price = 0
    for diamond in diamonds_ar:
        price = float(diamond[6]) 
        if price > highest_price:
            highest_price = price

    print(f"the most expensive diamond costs {highest_price}$.")
        
def avg_price(diamonds_ar):
    sum = 0
    counter = 0
    
    for diamond in diamonds_ar:
        price = float(diamond[7])
        sum += price
        counter += 1
    
    f_avg = sum/counter
        
    print(f"The average price of a diamond is {f_avg}")
    
def count_cut(diamonds_ar, field, target):
    global FIELDS
    counter = 0
    for diamond in diamonds_ar:
        if diamond[FIELDS.cut.value] == target:
            counter += 1
    print(f"There are {counter} diamonds with {target} {field}.")
    
def count_colors(diamonds_ar):
    global FIELDS
    colors = []
    for diamond in diamonds_ar:
        diamond_color = diamond[FIELDS.color.value]
        if diamond_color not in colors:
            colors.append(diamond_color)
    print(f"There are {len(colors)} colors:")
    for color in colors: print(color)

def hetzion_cut_carat(diamonds_ar, cut):
    temp = []
    index_hezion = 0
    for diamond in diamonds_ar:
        if diamond[FIELDS.cut.value] == cut:
            temp.append(diamond[FIELDS.carat.value])
    if len(temp)%2==0: index_hezion = int(len(temp)/2)
    else: index_hezion = int((len(temp)-1)/2)

    print(f"The hezion for carat of {cut} cut is {temp[index_hezion]}.")
        
def avg_carat_for_cut(diamonds_ar):
    sum = float(0)
    counter = float(0)
    cuts = []
    for diamond in diamonds_ar:
        if diamond[FIELDS.cut.value] not in cuts:
            cuts.append(diamond[FIELDS.cut.value])
    for cut in cuts:
        for diamond in diamonds_ar:
            if diamond[FIELDS.cut.value] == cut:
                sum += float(diamond[FIELDS.carat.value])
                counter += float(1)
        print(f"The average carat of {cut} cut diamonds is {sum/counter}.")
        
def avg_price_for_colors(diamonds_ar):
    sum = float(0)
    counter = float(0)
    colors = []
    for diamond in diamonds_ar:
        if diamond[FIELDS.color.value] not in colors:
            colors.append(diamond[FIELDS.color.value])
    for color in colors:
        for diamond in diamonds_ar:
            if diamond[FIELDS.color.value] == color:
                sum += float(diamond[FIELDS.price.value])
                counter += float(1)
        print(f"The average price of {color} color diamonds is {sum/counter}.")
