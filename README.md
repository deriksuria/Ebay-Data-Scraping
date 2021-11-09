# Ebay-Data-Scraping

[**project instructions** ](https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_03)

## What my program does:
This python program collects the name, price, status, shipping, number sold, and status of specified Ebay items. I used the following packages: 
1. Argparse to generate the command line arguments. 

### How do you run the `ebay-dl.py` file?

I used the following commands to run my file and output JSON files: 

`python3 ebay-dl.py coffee --num_pages=10 --csv=False `

`python3 ebay-dl.py hammer --num_pages=10 --csv=False`

`python3 ebay-dl.py "toy animal" --num_pages=10 --csv=False`

I used the following commands to run my file and output CSV files: 

`python3 ebay-dl.py macbook --num_pages=10 --csv=False `

`python3 ebay-dl.py wallet --num_pages=10 --csv=False`

`python3 ebay-dl.py "water bottle" --num_pages=10 --csv=False`

The general format is `python3 ebay-dl.py search_term num_pages = 10 csv = (True OR False)`. Search terms with more than one word are in quotations so Python searches the entire term rather than only the first word. For example running the code below would result in a unrecognized argument error. 

`python3 ebay-dl.py water bottle --num_pages=10 --csv=False`
