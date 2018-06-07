from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import time


path = 'test_blast.fasta'

# Load data
fasta = SeqIO.parse(path, format='fasta')
results = []

# Search blast
for record in fasta:
    results.append(NCBIWWW.qblast('blastn', 'nt', record.seq, format_type='Text', alignments=1, descriptions=1))
    # Awful additional delay
    time.sleep(10)



# Write title and sequence to fasta file
with open('blast_result', 'w') as out:
    for res, fasta in zip(results, SeqIO.parse(path, format='fasta')):
        rres = filter(None, res.read().split('\n'))
        for line in rres:
            if line.startswith('Sequences producing significant alignments:'):
                a = next(rres)
                out.write(f'>{a}\n{fasta.seq}')


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