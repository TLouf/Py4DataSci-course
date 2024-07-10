#!/usr/bin/env sh
BOOK_DIR="python-school"

python clean.py $BOOK_DIR

# actual stuff...
jupyter-book build $BOOK_DIR
