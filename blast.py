from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import time


path = 'test_blast.fasta'
out = 'named_contigs'

# Load data
fasta = SeqIO.parse(path, format='fasta')
results = []

# Search blast and parse its output
for record in fasta:
    res = NCBIWWW.qblast('blastn', 'nt', record.seq, alignments=1, descriptions=1)
    parsed = NCBIXML.parse(res)
    results.append(parsed)
    # Awful additional delay
    time.sleep(10)


# Write title and sequence to fasta file
with open('blast_result2', 'w') as out:
    for res in results:
        for record in res:
            name = record.alignments[0].title
            seq = record.alignments[0].hsps[0].query
            out.write(f'>{name}\n{seq}\n\n')
