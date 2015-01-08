Really old piece of code I had left over from a project involving md5 hash
searching.

Uses a rather naive (but quick-feeling) FS approach.

The characters of a hash are broken out and a folder is created for each one,
the next one nested within the first, and at the end is "plaintext.txt" that
contains the plaintext of the hash in question.

Ex: 
  4 -> c -> b -> 9 -> c -> ... -> a -> plaintext.txt -> "changeme"

Very naive in nature and in implementation, and probably takes up way too
much space given a large enough corpus of hashes.

Usage (as best I remember):
$>python filesystem.py
~/home/dydx/documents/wordlist.txt
Done creating filesystem

$>python search.py
Enter an md5 hash to find:
4cb9c8a8048fd02294477fcb1a41191a
changeme
