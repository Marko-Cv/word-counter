# Word Counter Instructions

## Setup

1. Download *create_virtualenv.py*, *install_packages.py*, *word_count.py*
2. In Terminal, navigate to the directory where these scripts are saved
3. Run *create_virtualenv.py*\
`python3 create_virtualenv.py`
5. When prompted, enter desired name of the virtual environment
6. Run the output text in command line, it should look like: `source /,../..`
7. Run *install_packages.py*\
`python3 install_packages.py`
9. When prompted, enter the previously entered name of the virtual environment

## Usage
1. Run one of the following:\
To save a csv of word counts only:\
`python3 word_count.py --w`
To save a csv of phrase counts only:\
`python3 word_count.py --w 'phrase1' 'phrase2' 'etc'`
To save both:\
`python3 word_count.py --w --p 'phrase1' 'phrase2' 'etc'`
2. When prompted, enter path to a single word/pdf file, or to a folder
3. If path to a folder is entered: when prompted, specify whether to analyze PDFs (1), word docs (2), or both types (3)




