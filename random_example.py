import random
import time

def show_random_features():

    #print radom float between 0.0 and 1.0
    print(random.random())

    #generate random integer
    print(random.randint(10,20))

    #random number with step and range
    print(random.randrange(0,100,5))

    #seed the generator for reproductivity
    random.seed(123)
    print([random.random() for _ in range(3)])

    #pick a random elements from a list
    fruits=["Jackfruit", "Banana", "Apple", "date"]
    print(random.choice(fruits))

    #pick a random multiple elements
    print(random.sample(fruits,2))

    #pick a random multiple elements with replacement
    print(random.sample(fruits,k=3))

    #shuffle a list
    cards=["Ace", "6ix", "trum", "nine"]
    random.shuffle(cards)
    print(cards)


    #get an integer with k random bits
    print(random.getrandbits(10))

    #NUMBER FROM DISTRIBUTIONS
    print(random.uniform(1,6))
    print(random.triangular(0,10,7))
    print(random.gauss(0,1))
    print(random.expovariate(1.5))


    #simple time showing random delays
    delay=random.uniform(0.5,1.5)
    start=time.time()
    time.sleep(delay)
    end=time.time()
    print(f"{end-start:.2f}")
show_random_features()
