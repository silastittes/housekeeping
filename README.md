# housekeeping
various bioinformatics scripts for converting file types and other mundane tasks from the command line. Most scripts print to screen.

SCRIPTS AND THEIR USAGE
---

fastaToPhylip converts fasta format to "pseudo" phylip (doesn't follow name conventions or name 10 spaces sequence rules). Works fine for most programs.
If there are more than two numbers on the first line of output (number of sequences and sequence lengths), some of the sequences of the infile differ in length, which is a problem you should fix.

Terminal usage:
```bash
python fastaToPhylip.py <your.fasta>
```
countSeq returns a table of sequence lengths

Terminal usage:
```bash
python counSeq.py <your.fasta>
```

unwrapFasta returns a fasta file with the sequence for each sample on one line (handy for ``grep -A1 ">header"`` to snag sequences by name)

Terminal usage:
```bash
python unwrapFasta.py <your.fasta>
```

longestSeq returns the name and sequence of the longest sequence in a fasta

Terminal usage:
```bash
python longestSeq.py <your.fasta>
```
