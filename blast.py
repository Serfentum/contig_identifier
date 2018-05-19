from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML


# Load data
fasta = SeqIO.read("test_blast.fasta", format="fasta")

# Search blast
print('Working...')
result_handle = NCBIWWW.qblast('blastn', 'nt', fasta.seq, format_type='Text')

# Write output
with open("blast_result.txt", "w") as out_handle:
    out_handle.write(result_handle.read())

result_handle = NCBIWWW.qblast("blastn", "nt", fasta.seq)

blast_records = NCBIXML.parse(result_handle)

for blast_record in blast_records:
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            print('sequence:', alignment.title)
            print('{} ... '.format(hsp.query[0:50]))
            print('{} ... '.format(hsp.match[0:50]))
            print('{} ... '.format(hsp.sbjct[0:50]))
            input()