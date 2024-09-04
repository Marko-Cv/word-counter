# Word Counter Instructions (Jupyter Notebook)

### Preparation
1. Ensure you have the `requests`, `beautifulsoup4`, and `pandas` libraries installed. If not, install them using \
   `!pip install requests beautifulsoup4 pandas`
3. Enter the desired save file destinations in lines 90, 91
4. Run the code in the next cell to define the functions (click on the cell, Shift+Enter)

### Usage options

##### Syntax:

`main(URL(s), phrase(s), want_words=False, want_phrases=False)`\
The funciton is called in the 2nd and 3rd code cells. Run it by clicking on the desired cell and pressing Shift+Enter.

##### Arguments:
- `URL(s)` (mandatory): A string or list of strings `['url1', 'url2', 'url3']` containing the URL(s) to analyze
- `phrase(s)` (optional): A string or list of strings `['phrase1', 'phrase2', 'phrase3']` containing the phrase(s) to count. Default is an empty list.
- `want_words` (optional): A boolean `True` or `False` to save word counts to a CSV file. Default is `False`.
- `want_phrases` (optional): A boolean `True` or `False` to save phrase counts to a CSV file. Default is `False`.

### Notes
- The `main` function will print the count of a phrase only if the single phrase is provided as a string.
- This script will not accept numbers as phrases, only words.
