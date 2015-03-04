def dna(filein, fileout):
    process(filein, fileout)

def process(filein, fileout):
    returnlist = []
    flin = open(filein)
    sequences = flin.readlines()
    for x in range(0, (len(sequences) - 1)):
        sequence = sequences[x]
        if(isValid(sequence)):
            returnlist.append("Region Name: " + sequences[x-1])
            returnlist.append("Nucleotides: " + sequence.upper())
            returnlist.append("Nuc. Counts: " + str(nuc_count(sequence)) + "\n")
            returnlist.append("Total Mass%: " + mass(sequence) + "\n")
            returnlist.append("Codons List: " + str(codons(sequence)) + "\n")
            returnlist.append("Is Protein?: " + protein(sequence) + "\n")
            returnlist.append("\n")
            returnlist.append("\n")
    out = open(fileout, 'w')
    out.writelines(returnlist)


def isValid(dna):
    return True if len([x for x in dna if x.lower() in 'qweryuiopsdfhjklzxvbnm']) == 0 else False

def nuc_count(sequence):
    return [sequence.lower().count('a'), sequence.lower().count('c'), sequence.lower().count('g'), sequence.lower().count('t')]

def mass(sequence):
    mass_a = sequence.lower().count('a') * 135.128
    mass_t = sequence.lower().count('t') * 125.107
    mass_g = sequence.lower().count('g') * 151.128
    mass_c = sequence.lower().count('c') * 111.103
    mass_total = mass_a + mass_c + mass_g + mass_t + (sequence.lower().count('-') * 100)
    return str([round((mass_a / mass_total),4), round((mass_c / mass_total),4), round((mass_g / mass_total),4), round((mass_t / mass_total),4)]) + ' of ' + str(mass_total)

def codons(sequence):
    codon_seq = [x for x in sequence if x != '-']
    return [str(codon_seq[x]).upper() + str(codon_seq[x+1]).upper() + str(codon_seq[x+2]).upper() for x in range(0,len(codon_seq) - (len(codon_seq)%3),3)]

def protein(sequence):
    if(codons(sequence)[0] == 'ATG' and (codons(sequence)[len(codons(sequence)) -1] == 'TAA' or codons(sequence)[len(codons(sequence)) -1] == 'TAG' or codons(sequence)[len(codons(sequence))-1] == 'TGA')):
        if(len(codons(sequence)) > 4):
            if(mass(sequence)[1] + mass(sequence)[2] >=30):
                return 'YES' 
    return 'NO'

def get_input():
    start = raw_input('Enter starting file name: ')
    end = raw_input('Enter destination file name: ')
    dna(start, end)