# Word Counter Instructions

## Setup

1. Download *create_virtualenv.py*, *install_packages.py*, *word_count.py*
2. In Terminal, navigate to the directory where these scripts are saved
3. Run *create_virtualenv.py*
``` 
python3 create_virtualenv.py
```
4. When prompted, enter desired name of the virtual environment
5. Run the output text in Terminal, it should look like: `source /,../..`
6. Run *install_packages.py*
```
python3 install_packages.py
```
7. When prompted, enter the previously entered name of the virtual environment
8. To test, run:
```
python3 word_count.py
```
If you're prompted for an input, the setup process was completed successfully

## Usage
1. Run one of the following:\
a. To save a CSV of word counts only:
```
python3 word_count.py --w
```
b. To save a CSV of phrase counts only:
```
python3 word_count.py --p 'phrase1' 'phrase2' 'etc'
```
c. To save both:
```
python3 word_count.py --w --p 'phrase1' 'phrase2' 'etc'
```
3. When prompted, enter path to a single word/pdf file, or to a folder containing such files
4. If folder path is entered: when prompted, specify whether to analyze PDFs (1), word docs (2), or both types (3)
5. When finished using the script, deactivate the virtual environment by running:
```
deactivate
```




