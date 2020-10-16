seq = input('digite uma sequencia .: ')

arq = open('python-projects\ProgramSimple\savingSeq.fasta', 'w')

arq.write('>seq\n')

arq.write(seq)

arq.close()