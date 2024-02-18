import random, csv
global cross_over_question

'''# Read in the data from the CSV file
items_csv_information = []
with open('PATH', 'r') as itemCsv:
    reader = csv.reader(itemCsv)
    for row in reader:
        items_csv_information.append((row[0], int(row[1]), int(row[2])))'''

objects1 = [(124, 265), (514, 345), (151, 57), (778, 790), (612, 122), (138, 43), (993, 11)]
# for the time when no list or file of object didn't exist
objects2 = None
choice = int(input(" PICK ONE : 1.Using default list    2.Taking the number of profit and white from user : "))
POP_SIZE = int(input("Please enter population size : "))
cross_over_question = int(input("Pick one : 1.crossover One 2.point crossover N point(PUT N AS INPUT) : "))
Mutation_rate_input = float(input("Please enter mutation rate (Recommend 0.8) :"))
choose_epoch_Repeat = int(input("chosse epoch : "))

if choice == 1:
    N = 7
    MAX_WEIGHT_items = 15
else:
    N = int(input("Please enter the number of items : "))  # number of items
    MAX_WEIGHT_items = int(input("Please enter the MAX weight : "))


class ItemKnapsack:
    def __init__(self, PROFITITEM, WEIGHTITEM):
        self.PROFITITEM = PROFITITEM
        self.WEIGHTITEM = WEIGHTITEM

# profit and weight getter function for each item
def ITEM_GETTER_FUNC(n, input_item=None):
    # items empty list :by taking information of user program will append number in this list
    items = []

    if input_item == None:
        # take value from user for each item "if input_items==None"
        for i in range(n):
            print(f"iteam {i + 1}")
            item_profit = int(input(f"Please enter the profit of item {i + 1} : "))
            item_weight = int(input(f"Please enter the weight of item {i + 1} : "))

            # sending items profit and weight to "calss Item" for making an item
            # appending created items to "items=[]"
            items.append(ItemKnapsack(item_profit, item_weight))
        print(f"Getting information about {N} items is finished!")

    # if file or Variable or list of values exist in program
    # send it to calss Items to make items and return it
    else:
        for item in input_item:
            items.append(ItemKnapsack(item[0], item[1]))

    for item in items:
        print(f"item{items.index(item) + 1}:profit:{item.PROFITITEM}   weight:{item.WEIGHTITEM}")
    return items

def INI_POP(n, POPULATIONPOPULATION):
    # making a list of population
    POP_LIST = []
    # in 'population_list ' we have to have p times elements
    for i in range(POPULATIONPOPULATION):
        new_member = [0 for i in range(n)] + [1 for i in range(n)]
        random.shuffle(new_member)
        # Throw away half of the list
        # taking half of the generated list as our population and use it in a new list
        # two NONE is for showing sum profit and weight of each example which we made it
        new_member = new_member[:n] + [None, None]
        # use new_member as population_list
        POP_LIST.append(new_member)
    return POP_LIST

def CROSSOVERKNAPSAKE(POP_LIST, n, POPULATIONPOPULATION):
    # start from 0 ,end till end of population size-2 last index  ,each time select 2 parent
    if cross_over_question == 1:
        # single point
        for i in range(0, POPULATIONPOPULATION, 2):
            n_b2 = n // 2
            child1 = POP_LIST[i][:n_b2] + POP_LIST[i + 1][n_b2:n] + [None, None]
            child2 = POP_LIST[i + 1][:n_b2] + POP_LIST[i][n_b2:n] + [None, None]
            POP_LIST.append(child1)
            POP_LIST.append(child2)
        return POP_LIST
    elif cross_over_question > 1:
        # n point
        for i in range(0, POPULATIONPOPULATION, 2):
            n_point = cross_over_question
            n_npoint = n // n_point
            child1 = POP_LIST[i][:n_npoint] + POP_LIST[i + 1][n_npoint:n] + [None, None]
            child2 = POP_LIST[i + 1][:n_npoint] + POP_LIST[i][n_npoint:n] + [None, None]
            POP_LIST.append(child1)
            POP_LIST.append(child2)
        return POP_LIST

def mutation(POP_LIST, n, POPULATIONPOPULATION, m):
    # just choose specifics child and just do the mutation on them
    choosen_once = [i for i in range(POPULATIONPOPULATION,POPULATIONPOPULATION*2)]
    random.shuffle(choosen_once)
    choosen_once = choosen_once[:int(((POPULATIONPOPULATION*2)-1)*m)]
    # which cell have to change
    for i in choosen_once:
        # putting the effect of mutation on one (or more) of the cell(s) randomly
        cell = random.randint(0,n-1)
        POP_LIST[i][cell] = 1 if POP_LIST[i][cell] == 0 else 0
    return POP_LIST

def W_diffrence(knapsack, n ,max_weight_input, items_exist_in_list):
    totalWeightBag = 0
    for i in range (n):
        if knapsack[i]:
            totalWeightBag += items_exist_in_list[i].WEIGHTITEM

    # Useless solution, which give weight more than our maximum weight, so we use Very big number for Useless solution
    # Calculate distance, just for useful solution
    return abs(max_weight_input-totalWeightBag) if totalWeightBag<=max_weight_input else 1000

def profit(knapsack ,n ,items_list):
    total_profit = 0
    for i in range(n):
        if knapsack[i]:
            total_profit += items_list[i].PROFITITEM
    return total_profit

def fitness(POP_LIST, n, POPULATIONPOPULATION,items_list, max_weight_input):
    for i in range (POPULATIONPOPULATION*2):# check all elements in populaion with "for"
        # calling two function related to weight and profile
        # related to index-1 which point weight # it has not to be more than 15 #DISTANCE TILL 15 (MAX) IS MATTER
        POP_LIST[i][n] = W_diffrence( POP_LIST[i] ,n ,max_weight_input,items_list)
        POP_LIST[i][n+1] =profit(POP_LIST [i],n ,items_list) # related to index which point profit # we have no MAX here !
    return POP_LIST

def SORTERLASTINDEXFUNC(population_list, index1, index2):
    sorted_list = sorted(population_list, key=lambda x:(x[index1], -x[index2]))
    return sorted_list

# main
if __name__ == "__main__":
    print("MAX WEIGHT is ",MAX_WEIGHT_items)
    # taking items from user with get_items function
    if choice == 1:
        items = ITEM_GETTER_FUNC(N, input_item=objects1)
    else:
        items = ITEM_GETTER_FUNC(N, input_item=objects2)

    def without_epoch():
        # fill knapsack with different item
        # making initial population
        C_POP = INI_POP(N, POP_SIZE)
        print("PARETNS : ")
        for i in C_POP[:4]:
                print(i)

        # We need n for figure out what is the 2 last index element and we new need population_size to recognize where is the parents
        C_POP = CROSSOVERKNAPSAKE(C_POP, N, POP_SIZE)
        print("CHILDS : ")
        for i in C_POP[4:]:
            print(i)

        C_POP = mutation(C_POP, N, POP_SIZE, Mutation_rate_input)
        print("AFTER MUTATION :  ")
        for i in C_POP[4:]:
            print(i)

        C_POP = fitness(C_POP, N, POP_SIZE, items, MAX_WEIGHT_items)
        print("TOTAL WEIGHT AND PROFIT :  ")
        for i in C_POP[4:]:
            print(i)

        C_POP = SORTERLASTINDEXFUNC(C_POP, N, N + 1)
        print("SORTED :  ")
        for i in C_POP[4:]:
            print(i)

        # eleminating : picking half of the population and distroying another half
        C_POP = C_POP[:POP_SIZE]
        C_POP = sorted(C_POP, key=lambda x: -x[N + 1])
        print("AFTER ELEMINATING :  ")
        for i in C_POP:
            print(i)
        print("BEST SOLUTION IS :", C_POP[0])
    def withepoch():
        howManyEPOCH = int(input("EPOCH : "))
        while howManyEPOCH :
            # fill knapsack with different item
            # making initial population
            C_POP = INI_POP(N, POP_SIZE)
            print("PARETNS : ")
            for i in C_POP[:4]:
                print(i)

            # We need n for figure out what is the 2 last index element and we new need population_size to recognize where is the parents
            C_POP = CROSSOVERKNAPSAKE(C_POP, N, POP_SIZE)
            print("CHILDS : ")
            for i in C_POP[4:]:
                print(i)

            C_POP = mutation(C_POP, N, POP_SIZE, Mutation_rate_input)
            print("AFTER MUTATION :  ")
            for i in C_POP[4:]:
                print(i)

            C_POP =fitness(C_POP,N, POP_SIZE, items, MAX_WEIGHT_items)
            print("TOTAL WEIGHT AND PROFIT :  ")
            for i in C_POP[4:]:
                print(i)

            C_POP = SORTERLASTINDEXFUNC(C_POP, N, N+1)
            print("SORTED :  ")
            for i in C_POP[4:]:
                print(i)

            # eleminating : picking half of the population and distroying another half
            C_POP = C_POP[:POP_SIZE]
            C_POP =sorted(C_POP, key=lambda x: -x[N+1])
            print("AFTER ELEMINATING :  ")
            for i in C_POP:
                print(i)
            howManyEPOCH -= 1
        else:
            print("BEST SOLUTION IS :",C_POP[0])
    if choose_epoch_Repeat == 0:
        without_epoch()
    elif choose_epoch_Repeat == 1:
        withepoch()