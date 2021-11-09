# Ebay-Data-Scraping

[**project instructions** ](https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_03)

## What my program does:
This python program collects the name, price, status, shipping, number sold, and status of specified Ebay items. I used the following packages/steps.
1. *Argparse* to generate the command line arguments. 
2. Added a argument to download the file as a CSV `parser.add_argument('--csv', default=False)`
3. Built the url and looped over the first 10 Ebay pages.
4. *Requests* to download the html file.
5. *bs4 or Beautifulsoup4* to parse through different elements of Ebay listings using CSS selectors and appended them into a dictionary.
6. Used a if/else statement to determine whether to export the file as a JSON or CSV
7. *Json* package to export the file as JSON 
8. *Csv* package to export the file as CSV 

### How do you run the `ebay-dl.py` file?

I used the following commands to run my file and output JSON files: 

`python3 ebay-dl.py coffee --num_pages=10 --csv=False `

`python3 ebay-dl.py hammer --num_pages=10 --csv=False`

`python3 ebay-dl.py "toy animal" --num_pages=10 --csv=False`

I used the following commands to run my file and output CSV files: 

`python3 ebay-dl.py macbook --num_pages=10 --csv=True `

`python3 ebay-dl.py wallet --num_pages=10 --csv=True`

`python3 ebay-dl.py "water bottle" --num_pages=10 --csv=True`

The general format is `python3 ebay-dl.py search_term num_pages = 10 csv = (True OR False)`. Search terms with more than one word are in quotations so Python searches the entire term rather than only the first word. For example running the code below would result in a unrecognized argument error. 

`python3 ebay-dl.py water bottle --num_pages=10 --csv=False`
