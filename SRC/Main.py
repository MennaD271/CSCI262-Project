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
            filter()     
        
        elif option == 4:
            t1 = time.time()
            avg_similarity = analyzeDataset1(); 
            t2 = time.time()
            print(f"Average Similarity of dataset 1 is: {avg_similarity}")
            print(f"Time taken: {t2-t1} seconds")

        elif option == 5:
            t1 = time.time()
            avg_similarity = analyzeDataset1(); 
            t2 = time.time()
            avg_similarity = analyzeDataset2(); 
            print(f"Average Similarity of dataset 2 is: {avg_similarity}")
            print(f"Time taken: {t2-t1} seconds")

        elif option == 6:
            t1 = time.time()
            avg_similarity = analyzeDataset1(); 
            t2 = time.time()
            avg_similarity = analyzeDataset3(); 
            print(f"Average Similarity of dataset 3 is: {avg_similarity}")
            print(f"Time taken: {t2-t1} seconds")
                  
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
        
def filter() -> None:
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
    similarity = 0.0
    with open("SRC/datasets/beta1.txt", 'r') as w:
        lines = w.readlines()
        for i in range(0, len(lines), 2):
            similarity += bloom.get_similarity(lines[i], lines[i+1])

        similarity /= len(lines)

    return similarity

def analyzeDataset2():
    similarity = 0.0
    with open("SRC/datasets/beta2.txt", 'r') as w:
        lines = w.readlines()
        for i in range(0, len(lines), 2):
            similarity += bloom.get_similarity(lines[i], lines[i+1])

        similarity /= len(lines)

    return similarity

def analyzeDataset3():
    similarity = 0.0
    with open("SRC/datasets/beta3.txt", 'r') as w:
        lines = w.readlines()
        for i in range(0, len(lines), 2):
            similarity += bloom.get_similarity(lines[i], lines[i+1])

        similarity /= len(lines)

    return similarity

        

if __name__ == "__main__":
    main()
            
            
            
    