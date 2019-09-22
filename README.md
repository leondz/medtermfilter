# medtermfilter
Medical term filtering for twitter capture archives

## Use

Run

```  ./kcl-term-filter.py <input file> <serial>```

where `input file` refers to a file formatted as Twitter JSON with one self-contained JSON record of a Tweet per line; and `serial` is a unique identifier for this run of the program, used to name its output files.

The code relies on Twitter's built-in language identification to strip out non-English tweets.

A series of medications, disorders, and self-harm term categories are searched for, defined by regular expressions. Output is one file of tweet JSON records per category. Input tweets that match more than one category will be presented in every output category. That is, assignment is not hard, and documents that match e.g. terms in both the "self-harm" and "diazepam" categories, will be present in both the self-harm and the medications->diazepam output files.

## Attribution

Code by Leon Derczynski; term specification by Anna Kolliakou. Produced during research supported under the EU [PHEME](https://www.pheme.eu) project. Licensed [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) - you may use and even share this, and attribution is required. You may cite this paper:

**PHEME: Computing Veracity — the Fourth Challenge of Big Social Data**
Leon Derczynski, Kalina Bontcheva, Michal Lukasik, Thierry Declerck, Arno Scharl, Georgi Georgiev, Petya Osenova, Tomas Pariente Lobo, Anna Kolliakou, Robert Stewart, Sara-Jayne Terp, Geraldine Wong, Christian Burger, Arkaitz Zubiaga, Rob Procter, and Maria Liakata.
_Proceedings of the Extended Semantic Web Conference EU Project Networking session (ESCW-PN)_. 2015.

Bibtex:
```
@inproceedings{pheme,
 title={{PHEME: Computing Veracity — the Fourth Challenge of Big Social Data}},
 author={Leon Derczynski and Kalina Bontcheva and Michal Lukasik and Thierry Declerck and Arno Scharl and Georgi Georgiev and Petya Osenova and Tomas Pariente Lobo and Anna Kolliakou and Robert Stewart and Sara-Jayne Terp and Geraldine Wong and Christian Burger and Arkaitz Zubiaga and Rob Procter and Maria Liakata},
 year={2015},
 inproceedings={Proceedings of the Extended Semantic Web Conference EU Project Networking session (ESCW-PN)},
}
```
