from Bloomfilter import Bloomfilter
bloom = Bloomfilter()
def main():
     #create object
    listpass = ["password123", "passwords", "Jessica"] #dummy data 
    #bloom.train_filter(listpass)
    while True: 
        print("Welcome to menu, choose from the follwoing.")
        print("Choose 1 to set a new password of length 8, 10 or 12 characters.") #doesn't save password anywhere
        print("Choose 2 to change your password.") 
        print("Choose 3 to compare passwords with jaccard coefficient.") 
        print("Choose 4 to generate the bloom filter of your given password.")
        print("Choose 0 to exit menu.")
        option = int(input("Enter your choice: "))
        
        if option == 1:
            password = input("Set a new password: ")
            if len(password) in [8,10,12]:
                if bloom.test(password):
                    print("Strong")
                else:
                    print("Weak")
            else:
                print("Invalid length")
                
        elif option == 2:
            old_pass = input("Enter your old password: ")
            new_pass = input("Enter your new password: ")
            while True:  #keep looping till user enters a valid length or a password that has less than 0.5 similarity
                if len(password) == 8 or 10 or 12:
                    coefficient = bloom.get_similarity(old_pass, new_pass)
                    if coefficient >= 0.5:
                        print("Password is too similar to your old password. Try again")
                    else:
                        print("Password changed successfully")
                        break
                else:
                    print("Insert password with valid length")    
                                           
        elif option == 3:
            nJaccard()
        
        elif option == 4: 
            filter()     
                  
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


if __name__ == "__main__":
    main()
            
            
            
    