import hashlib

class Bloomfilter:
    def __init__(self):
        self.size = 1000
        self.filter = [0 for i in range(self.size)]
        self.num_of_hashes = 15
        
    def hash(self, password: str):
        '''
        hashes the password and returns the indices which must be assigned a value of 1 in the bloom filter. 

        input - password
        output - list of 15 indices which should have a value of 1 in the BF
        '''
        hashes = []
        password = password.encode()
        for i in range(self.num_of_hashes):
            g = hashlib.md5()
            h = hashlib.sha256()
            g.update(password)
            h.update(password)
             
            hash = (int(g.hexdigest(), base=16) + i * int(h.hexdigest(), base=16)) % self.size
            hashes.append(hash)
        return hashes
    
    def train_filter(self, file, passwords):
        '''
        Takes a list of passwords and trains the bloom filter. bigram_hash function is used to generate the indices for the BF. It returns an array of indices for which the value must be 1 in the BF. 
        '''
        #file = open('rockyou.txt', 'r')
        #passwords = file.readlines()  
        for password in passwords: 
            for index in self.bigram_hash(password):
                self.filter[index] = 1
            

    def bigram_hash(self, password: str):
        '''
        Takes a password - eg. pass1
        Adds empty space to the start and end - _pass1_
        Splits it into bigrams - [_p, pa, as, ss, s1, 1_]
        for each bigram
            the hash function is called which returns an array of indices for 1s in the BF
        all the arrays of indices are union-ed to give a single array of indices for the entire word
        this array is returned
        '''
        #implemented by menna
        return None

    def get_similarity(self, password1, password2):
        '''
        password1 - array of indices that are 1s in the BF
        password2 - new password

        we first get all the common indices - this serves as the common bits that are 1 in the BF
        Adding the lengths of the two arrays will give us the total number of bits turned 1 in the BF
        Then we can calculate the jaccard coefficient. 
        '''
        new_password = self.bigram_hash(password2)
        intersection = filter(lambda x: x in new_password, password1)
        
        distance = len(intersection) / (len(password1) + len(new_password))
        return distance

    
    def test(self,password):
        '''
        first get an array of indices for the password
        then check if any of those indices are 0 
        if there are any, return false, corresponding to a weak password. 
        if there are no 0s, then its a strong password and returns true
        '''
        for index in self.bigram_hash(password):
            if self.filter[index] == 0:
                return False
            
        return True
    
#Testing
a = Bloomfilter()
b = input("Enter string: ")
print(a.hash(b))