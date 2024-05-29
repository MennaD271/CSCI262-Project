class Bloomfilter:
    def __init__(self):
        self.size = [5000]
        self.num_of_hashes = 15
        
    def hash_functions(self, password):
        return password
    
    def train_filter(self,file):
        file = open('rockyou.txt', 'r')
        passwords = file.readlines()  
    
    def test(self,newpassword):
        return True
    