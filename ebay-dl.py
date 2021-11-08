import argparse
import requests 
from bs4 import BeautifulSoup
import json
import csv

# python3 -m doctest ebay-dl.py

def parse_itemsold(text):
    '''
    Takes as input a string and returns the number of items sold, as specified in the string

    >>> parse_itemsold('38 sold')
    38
    >>> parse_itemsold('14 watchers')
    0
    >>> parse_itemsold('Almost gone')
    0
    '''
    numbers = ''
    for char in text: 
        if char in '1234567890':
            numbers += char 
    if 'sold' in text:
        return int(numbers) 
    else: 
        return 0 

def parse_price(dollars):
    '''
    Takes as input a string and returns the number of items sold, as specified in the string

    >>> parse_price('$23.60')
    2360
    >>> parse_price('$5.00')
    500
    >>> parse_price('$60.00')
    6000
    >>> parse_price('$60.00 to $70.00')
    6000
    >>> parse_price('Free shipping')
    0
    >>> parse_price('+$13.45 shipping')
    1345
    '''
    
    dollars_text = ''
    dollar_sign_index = dollars.find('$')
    space_index = dollars.find (' ')
    if dollar_sign_index == -1:
        return 0 
    if space_index != -1:
        dollars_text = dollars[dollar_sign_index:space_index]
    else:
        dollars_text = dollars[dollar_sign_index:]

    cents = ''
    for char in dollars_text: 
        if char in '1234567890':
            cents += char 
    return int(cents)


# this if statement says only run the code below when python file is run "normally"
# normally = not in doctest 

if __name__ == '__main__':

# get command line arguments 
    parser = argparse.ArgumentParser(description='Download information from Ebay and convert to JSON.')
    parser.add_argument('search_term') #no dash is required argument 
    parser.add_argument('--num_pages', default=10)
    parser.add_argument('--csv', default=False)
    args = parser.parse_args()
    print('args.search_term=', args.search_term )

    #list of all items found in all ebay webpages 
    items = []

    #loop over the ebay webpages 
    for page_number in range(1,int(args.num_pages)+1): 

        #build the url 
        url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=' 
        url += args.search_term
        url += '&_sacat=0&LH_TitleDesc=0&_pgn='
        url += str(page_number)
        url += '&rt=nc'
        print('url=', url)

    # download the html
        r = requests.get(url)
        status = r.status_code
        print('status=', status)
        html = r.text
        #print('html=', html[:50])

    # process the html

        soup = BeautifulSoup(html, 'html.parser')

        tags_items = soup.select('.s-item')
        for tag_item in tags_items:
            print('tag_item=', tag_item)

            name = None
            tags_name = tag_item.select('.s-item__title')
            for tag in tags_name:
                name = tag.text

            price = None
            tags_name = tag_item.select('.s-item__price')
            for tag in tags_name:
                price = parse_price(tag.text)

            status = False
            tags_name = tag_item.select('.SECONDARY_INFO')
            for tag in tags_name:
                status = tag.text

            shipping = 0
            tags_name = tag_item.select('.s-item__shipping')
            for tag in tags_name:
                shipping = parse_price(tag.text)
            
            freereturns = False
            tags_freereturns = tag_item.select('.s-item__free-returns')
            for tag in tags_freereturns: 
                freereturns = True

            items_sold = 0
            tags_freereturns = tag_item.select('.s-item__hotness, .s-item__additionalItemHotness')
            for tag in tags_freereturns: 
                items_sold = parse_itemsold(tag.text)

            item = {
                'name': name, 
                'price': price,
                'status': status,
                'shipping': shipping,
                'freereturns': freereturns,
                'itemssold': items_sold
            }
            items.append(item)
        print('len(tags_item)=', len(tags_items))
        print('len(items)=', len(items))


    if (args.csv == False):
        # write the json to a file
        filename = args.search_term+'.json'
        with open(filename, 'w', encoding='ascii') as f:
            f.write(json.dumps(items))

    else: # --csv == True
        field_names = ['name', 'price', 'status', 'shipping', 'freereturns', 'itemssold']
        csvfilename = args.search_term+'.csv'
        with open(csvfilename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = field_names)
            writer.writeheader()
            writer.writerows(items)

