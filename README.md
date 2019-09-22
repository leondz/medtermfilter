# medtermfilter
Medical term filtering for twitter capture archives

## Use:

Run

```  ./kcl-term-filter.py <input file> <serial>```

where `input file` refers to a file formatted as Twitter JSON with one self-contained JSON record of a Tweet per line; and `serial` is a unique identifier for this run of the program, used to name its output files.

The code relies on Twitter's built-in language identification to strip out non-English tweets.

A series of medications, disorders, and self-harm term categories are searched for, defined by regular expressions. Output is one file of tweet JSON records per category. Input tweets that match more than one category will be presented in every output category. That is, assignment is not hard, and documents that match e.g. terms in both the "self-harm" and "diazepam" categories, will be present in both the self-harm and the medications->diazepam output files.
