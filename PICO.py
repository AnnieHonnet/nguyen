def extract_sequence_from_fastq(file_path):
    with open(file_path, 'r') as fastq_file:
        lines = fastq_file.readlines()
        
        # Initialize an empty list to store the DNA sequences
        sequences = []
        
        # Iterate through the lines to extract sequences
        for i in range(len(lines)):
            # Check if the line starts with '@' (indicating the start of a sequence)
            if lines[i].startswith('@'):
                # Get the sequence from the line that is two lines below
                if i + 1 < len(lines):
                    sequence = lines[i + 1].strip()
                    sequences.append(sequence)
                
        return sequences
    
def save_sequences_to_file(sequences, output_file_path):
    with open(output_file_path, 'w') as output_file:
        for sequence in sequences:
            output_file.write(sequence + '\n')


# Specify the path to your FASTQ file
file_path = '/home/stu/Desktop/PICO/DATA/MINION.ALL.DATA.fastq'

# Call the function to extract DNA sequences
dna_sequences = extract_sequence_from_fastq(file_path)

# Specify the path for the output file            
output_file_path = '/home/stu/Desktop/PICO/DATA/MINION.extracted.txt'

# Call the function to save sequences to a file
save_sequences_to_file(dna_sequences, output_file_path)

# Print the extracted DNA sequences
print("Extracted DNA Sequences:")
for sequence in dna_sequences:
    print(sequence)

