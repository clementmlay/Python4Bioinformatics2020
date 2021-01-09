def writefile(gen_file, out_file):
   
    with open(out_file, 'w') as outfile:
        outfile.write('\n'.join(gen_file))

def remove_empty(gen_file):
 
    tag = True
    while tag:
        try:
            gen_file.remove('-')
        except ValueError:
            tag = False
    return gen_file

def clean_genes(input_file, out_file):
   
    gen_file = []
    tag = False
    with open(input_file, 'r') as humchrx:
        for line in humchrx:
            if line.startswith('Gene'):
                tag=True
            if line == '\n':
                tag = False
            if tag:
                gen_file.append(line.split()[0])
    #clean the gene list
    gen_file.pop(2)
    gen_file[0] = gen_file[0]+"_"+gen_file[1]
    gen_file.pop(1)
   
    gen_file = remove_empty(gen_file)
   
    # Writing to file
    writefile(gen_file, out_file)
clean_genes('../Data/humchrx.txt', 'gnames.txt')
