import SRC.Bloomfilter as Bloomfilter
def main():
    bloom = Bloomfilter() #create object
    listpass = ["password123", "passwords", "Jessica"] #dummy data 
    bloom.train_filter(listpass)
    while True: 
        print("Welcome to menu, choose from the follwoing.")
        print("Choose 1 to set a new password of length 8, 10 or 12 characters.") #doesn't save password anywhere
        print("Choose 2 to chnage your password.") 
        print("Choose 0 to exit menu.")
        option = int(input("Enter your choice: "))
        
        if option == 1:
            password = input("Set a new password: ")
            if len(password) == 8 or 10 or 12:
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
                                           
        elif option == 0: 
            print("Exiting menu")
            break
        
        else:
            print("Insert a valid option")
            
if __name__ == "__main__":
    main()
            
            
            
    