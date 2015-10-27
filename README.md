# housekeeping
various bioinformatics scripts for converting file types and other mundane tasks to run in the terminal

SCRIPTS AND THEIR USAGE
---

fastaToPhylip converts fasta format to "pseudo" phylip (doesn't follow name conventions or name 10 spaces sequence rules). Works fine for most programs.
If there are more than two numbers on the first line of output (number of sequences and sequence lengths), some of the sequences of the infile differ in length, which is a problem you should fix.

From terminal:
```bash
python fastaToPhylip.py <your.fasta>
```
countSeq returns a table of sequence lengths

From terminal:
```bash
python counSeq.py <your.fasta>
```
