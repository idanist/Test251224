from functions import*
from enum import Enum

DATA_FILE = 'data.csv'

class FIELDS(Enum):
    carat = 0
    cut = 1
    color = 2
    clarity = 3
    depth = 4
    table = 5
    price = 6
    x = 7
    y = 8
    z = 9

DIAMONDS_AR = []

with open(DATA_FILE, 'r') as file:
    header = file.readline()
    for line in file:
        fields = line.strip().split(',')
        DIAMONDS_AR.append(fields)


if __name__=="__main__":
    
    most_expensive(DIAMONDS_AR)
    print("")
    avg_price(DIAMONDS_AR)
    print("")
    count_cut(DIAMONDS_AR, 'cut' ,'Ideal')
    print("")
    count_colors(DIAMONDS_AR)
    print("")
    hetzion_cut_carat(DIAMONDS_AR, 'Premium')
    print("")
    avg_carat_for_cut(DIAMONDS_AR)
    print("")
    avg_price_for_colors(DIAMONDS_AR)
    