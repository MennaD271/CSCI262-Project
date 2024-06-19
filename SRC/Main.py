from Bloomfilter import Bloomfilter
import time

bloom = Bloomfilter()

def main():
    while True: 
        print("\n\nWelcome to menu, choose from the follwoing.")
        print("Choose 1 to generate the bloom filter of your given password.")
        print("Choose 2 to check if passwords are similar")
        print("Choose 3 to compare passwords with jaccard coefficient.") 
        print("Choose 4 to analyze dataset 1.") 
        print("Choose 5 to analyze dataset 2.") 
        print("Choose 6 to analyze dataset 3.") 
        print("Choose 0 to exit menu.")
        option = int(input("Enter your choice: ")) 
                                           
        if option == 3:
            nJaccard()
        
        elif option == 2:
            similarity()
        
        elif option == 1: 
            bloomfilter()     
        
        elif option == 4:
            avg_similarity = analyzeDataset1(); 
            print(f"Average Similarity of dataset 1 is: {avg_similarity}")
            

        elif option == 5:
            avg_similarity = analyzeDataset2(); 
            print(f"Average Similarity of dataset 2 is: {avg_similarity}")

        elif option == 6:
            avg_similarity = analyzeDataset3(); 
            print(f"Average Similarity of dataset 3 is: {avg_similarity}")
                  
        elif option == 0: 
            print("Exiting menu")
            break
        
        else:
            print("Insert a valid option")
            
def nJaccard() -> None:
    p = input("Enter password: ")

    new_p = input("Enter another password to compare using Jaccard Coefficient. To exit enter 0: ")
    while (new_p != "0"):
        similarity = bloom.get_similarity(p, new_p)
        print(f"The Jaccard Coefficient is {similarity}")
        new_p = input("Enter another password to compare using Jaccard Coefficient. To exit enter 0: ")
        
def bloomfilter() -> None:
    password = input("Enter password to get bloom filter: ")
    filter = bloom.bigram_hash(password)
    print("Your filter is: ", filter)

def similarity():
    pass1 = input("Enter password from the beta file: ")
    pass2 = input("Enter another password from the beta file: ")
    similarity = bloom.get_similarity(pass1, pass2)
    #Jaccard Threshold
    if similarity > 0.7: 
        print("Passwords are very similar")
    else: 
        print("Passwords are not similar")

def analyzeDataset1():
    t1 = time.time()

    similarity = 0.0
    passwords = open("SRC/datasets/dataset1.txt", "r").readlines()
    passwords = list(filter(lambda password: password != '\n', passwords))
    passwords = list(map(lambda password: password.replace("\n", "").strip() ,passwords))

    bf = Bloomfilter()
    bf.train_filter(passwords)

    t2=time.time()

    inp = input("Enter password to test dataset: ").strip()

    t3=time.time()

    if (bf.test(inp)): 
        print("Password is strong")
    else: 
        print("Password is weak")

    for i in range(0, len(passwords), 2):
        similarity += bloom.get_similarity(passwords[i], passwords[i+1])

    t4=time.time()

    print(f"Time taken: {t4-t3+t2-t1} seconds")
    return similarity/len(passwords)

def analyzeDataset2():
    t1 = time.time()

    similarity = 0.0
    passwords = open("SRC/datasets/dataset2.txt", "r").readlines()
    passwords = list(filter(lambda password: password != '\n', passwords))
    passwords = list(map(lambda password: password.replace("\n", "").strip() ,passwords))

    bf = Bloomfilter()
    bf.train_filter(passwords)

    t2=time.time()

    inp = input("Enter password to test dataset: ").strip()

    t3=time.time()

    if (bf.test(inp)): 
        print("Password is strong")
    else: 
        print("Password is weak")

    for i in range(0, len(passwords), 2):
        similarity += bloom.get_similarity(passwords[i], passwords[i+1])

    t4=time.time()

    print(f"Time taken: {t4-t3+t2-t1} seconds")
    return similarity/len(passwords)

def analyzeDataset3():
    t1 = time.time()

    similarity = 0.0
    passwords = open("SRC/datasets/dataset3.txt", "r").readlines()
    passwords = list(filter(lambda password: password != '\n', passwords))
    passwords = list(map(lambda password: password.replace("\n", "").strip() ,passwords))

    bf = Bloomfilter()
    bf.train_filter(passwords)

    t2=time.time()

    inp = input("Enter password to test dataset: ").strip()

    t3=time.time()

    if (bf.test(inp)): 
        print("Password is strong")
    else: 
        print("Password is weak")

    for i in range(0, len(passwords), 2):
        similarity += bloom.get_similarity(passwords[i], passwords[i+1])

    t4=time.time()

    print(f"Time taken: {t4-t3+t2-t1} seconds")
    return similarity/len(passwords)


        

if __name__ == "__main__":
    main()
            
            
            
    