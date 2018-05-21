from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import time


path = 'test_blast.fasta'

# Load data
fasta = SeqIO.parse(path, format='fasta')
results = []

# Search blast
print('Search')

for record in fasta:
    results.append(NCBIWWW.qblast('blastx', 'nr', record.seq, format_type='Text', alignments=2, descriptions=2))
    time.sleep(5)
# Write output
with open('blast_result', 'w') as out:
    out.write('\n'.join([res.read() for res in results]))

# result_handle = NCBIWWW.qblast("blastn", "nt", fasta.seq)
#
# blast_records = NCBIXML.parse(result_handle)
#
# for blast_record in blast_records:
#     for alignment in blast_record.alignments:
#         for hsp in alignment.hsps:
#             print('sequence:', alignment.title)
#             print('{} ... '.format(hsp.query[0:50]))
#             print('{} ... '.format(hsp.match[0:50]))
#             print('{} ... '.format(hsp.sbjct[0:50]))
#             input()