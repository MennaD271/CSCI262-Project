from Bloomfilter import Bloomfilter
import os

def read_dataset(filepath):
    with open(filepath, 'r') as file:
        return file.read().splitlines()

def generate_beta(filepath, output_filename) -> float:
    bloomfilter = Bloomfilter()
    passwords = read_dataset(filepath)
    with open(output_filename, 'w') as outfile:
        for password in passwords:
            beta = bloomfilter.bigram_hash(password)
            outfile.write(f"{password} {beta}\n")

    

src_folder = 'SRC'

dataset1_filepath = os.path.join(src_folder, 'datasets', 'dataset1.txt')
beta1_output_filename = 'SRC/datasets/beta1.txt'
generate_beta(dataset1_filepath, beta1_output_filename)

dataset2_filepath = os.path.join(src_folder, 'datasets', 'dataset2.txt')
beta2_output_filename = 'SRC/datasets/beta2.txt'
generate_beta(dataset2_filepath, beta2_output_filename)

dataset3_filepath = os.path.join(src_folder, 'datasets', 'dataset3.txt')
beta3_output_filename = 'SRC/datasets/beta3.txt'
generate_beta(dataset3_filepath, beta3_output_filename)