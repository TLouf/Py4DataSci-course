#!/usr/bin/env zsh
BOOK_DIR="python-school"

micromamba activate $BOOK_DIR
python clean.py $BOOK_DIR

# actual stuff...
jupyter-book build $BOOK_DIR
