#!/usr/bin/env python
"""
Pythonic wrapper for Nucleosome position prediction tool called NuPoP. 
It can handle multiple sequence in a FASTA file. More details: http://nucleosome.stats.northwestern.edu/

# Written (W) 2010-2014 Vipin T Sreedharan
    Friedrich Miescher Laboratory of the Max Planck Society, Tuebingen Germany.
    Memorial Sloan Kettering Cancer Center, New York City, USA.
"""

import os
import re
import sys
import time
import struct
from Bio import SeqIO

def __main__():

	stime = time.asctime( time.localtime(time.time()) )

	print '----------------------------------------'
	print 'NuPoP started on %s' % stime  
	print '----------------------------------------'

	print'\nStep:1 Checking input parameters\n' 

	try:
		fasta_file = sys.argv[1]
		linker_len = sys.argv[2]
		order_mm = sys.argv[3]
		linker_up = sys.argv[4]
		organism = sys.argv[5]
		res_format = sys.argv[6]
		pred_file = sys.argv[7]
		pred_file_path = sys.argv[8]
	except:
		sys.stderr.write("Check input parameters:\n\t
            1. A valid FASTA file\n\t
            2. Linker DNA length (100-500)\n\t
            3. Order of HMM (1 or 4)\n\t
            4. Linker length distribution (0-5)\n\t
            5. Species (1 : Homo sapiens, 2 : Mus musculus, 
                3 : Rattus norvegicus, 4 : Danio rerio, 
                5 : Drosophila melanogaster, 6 : Caenorhabditis elegans, 
                7 : Saccharomyces cerevisiae, 8 : Candida albicans, 
                9 : Schizosaccharomyces pombe, 10 : Arabidopsis thaliana, 
                11 : Zea mays)\n\t
            6. Result format (wig or text)\n\t
            7. Prediction result file name\n\t
            8. Temp path\n")
		sys.exit(-1)

	## species available for NuPoP program	
	species = {'1' : "Homo sapiens", 
        '2' : "Mus musculus", 
        '3' : "Rattus norvegicus", 
        '4' : "Danio rerio", 
        '5' : "Drosophila melanogaster", 
        '6' : "Caenorhabditis elegans", 
        '7' : "Saccharomyces cerevisiae", 
        '8' : "Candida albicans", 
        '9' : "Schizosaccharomyces pombe", 
        '10' : "Arabidopsis thaliana", 
        '11' : "Zea mays"}

	os.system("mkdir -p %s" % pred_file_path)

	## log message 	
	print "Reading FASTA file                      : %s" % fasta_file
	print "Maximum length of linker DNA            : %s" % linker_len 
	print "Order of Markov Model                   : %s" % order_mm
	print "Linker length distribution update times : %s" % linker_up
	print "Species selected                        : %s\n" % species[organism] 

	pred_file_handle = open(pred_file, "w+")

	if res_format == 'wig': 
        pred_file_handle.write("track type=wiggle_0 
            name=\"Nucleosome_Position_Prediction\" 
            description=\"Genome source %s\"\n" % species[organism] )

	print 'Step:2 Processing FASTA file\n'
	fasta_handle = open(fasta_file, "rU")

    # binary files are another form of result format 

	for record in SeqIO.parse(fasta_handle, "fasta"):

		print 'Sequence identifier: %s' % record.id 
		print 'Sequence length: %d' % len(record.seq)

		fasta_in = "%s/%s.fa" % (pred_file_path, record.id)
		fasta_outhand = open(fasta_in, "w+")
		fasta_outhand.write(record.format("fasta"))
		fasta_outhand.close()

		# Npred result file 
		npred_out = "%s/%s" % (pred_file_path, record.id) 

		# Compiling NuPoP for chromosome/contig: %s' % record.id

		# run NuPoP os.popen pipe the result TODO 
        
		# clean up the contig based fasta and npred result file 
	fasta_handle.close()	
    pred_file_handle.close()

	etime = time.asctime( time.localtime(time.time()) )
	print '----------------------------------------'
	print 'NuPoP finished on %s' % etime  
	print '----------------------------------------'

if __name__=='__main__':
    __main__()
