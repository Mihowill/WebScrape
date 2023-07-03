import sys
import re
from bs4 import BeautifulSoup
import os

#   TODO: NAPRAVITI KLASE ZA SVAKU VRSTU HTML-A
#   TODO: SVAKA OD TIH KLASA TREBA IMATI METODU parse() KOJA PRIMA SOUP IZ MAIN-A I VRAĆA ARRAY OBJEKATA (DICTIONARY-a)

#   TODO: SVAKA OD KLASA TREBA DA VRATI LISTU OBJEKATA (DICTIONARY-a) SA ODREĐENOM STRUKTUROM, OVISNO O KOJOJ SE STRANICI RADI

#   ZADATAK 1:
#   http://quotes.toscrape.com/
#   quotes_to_scrape_test.html MORA VRATITI LISTU OBJEKTA (DICTIONARY-a) KOJI SVI IMAJU:
#                                                                        url -> URL NA KOJEM SE MOGU VIDJETI DETALJI AUTORA
#                                                                        author -> IME AUTORA
#                                                                        text -> TEXT QUOTE-A
#                                                                        tags -> ARRAY (LISTA) SA TEXTOM SVIH TAGOVA U QUOTE-U

#   ZADATAK 2
#   https://books.toscrape.com/
#   books_to_scrape_test.html i MORAJA VRATITI LISTU OBJEKTA (DICTIONARY-a) KOJI SVI IMAJU:
#                                                                            url -> URL NA KOJEM SE MOGU VIDJETI DETALJI TE KNJIGE
#                                                                            title -> TITLE TE KNJIGE (PO MOGUĆNOSTI UZETI CIJELI TITLE)
#                                                                            stock -> 0 ILI 1 OVISNO O JELI KNJIGA DOSTUPNA ZA KUPITI (0-NE, 1-DA)
#                                                                            price -> CIJENA KJNIGE (MORA BITI float TIP)
#                                                                            rating -> RATING KNJIGE (OD 0-5, OVISNO KOLIKO ZVIJEZDA IMA KNJIGA)

#   ZADATAK 3
#   https://www.bookdepository.com/category/2638/History-Archaeology
#   books_depository_test.html i MORAJA VRATITI LISTU OBJEKTA (DICTIONARY-a) KOJI SVI IMAJU:
#                                                                            url -> URL NA KOJEM SE MOGU VIDJETI DETALJI TE KNJIGE
#                                                                            title -> TITLE TE KNJIGE (PO MOGUĆNOSTI UZETI CIJELI TITLE)
#                                                                            stock -> 0 ILI 1 OVISNO O JELI KNJIGA DOSTUPNA ZA KUPITI (0-NE, 1-DA)
#                                                                            price -> CIJENA KJNIGE (MORA BITI float TIP)
#                                                                            low_price -> NAJNIŽA CIJENA KJNIGE U 30 DANA (30-day low price), AKO NE POSTOJI MORA BITI ISTI KAO I PRICE (MORA BITI float TIP)
#                                                                            rating -> RATING KNJIGE (OD 0-5, OVISNO KOLIKO ZVIJEZDA IMA KNJIGA)
#                                                                            category -> KATEGORIJA U KOJOJ JE KNJIGA SVRSTANA (New and recent, Bestselling History Titles, ...)


class ClassTemplate():
    def __init__(self, name="ClassTemplate"):
        self.results = []

    def parse(self, soup):
        print("CODE HERE")

        #   PRIMJER LISTE OBJEKATA (ATRIBUTI SU DUMMY PODATCI, SLUŽI SAMO KAO PRIMJER STRUKTURE OUTPUTA)
        self.results = [
            {
                "title": "Object 1",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas bibendum nisl eu maximus convallis. Maecenas suscipit, augue eu viverra suscipit, quam est luctus neque, vel consequat eros felis eu eros. Ut mollis suscipit vulputate. Aliquam erat volutpat. Phasellus nec dui aliquet, ornare urna vitae, placerat justo. Fusce mauris ipsum, porttitor sed cursus id, venenatis a erat. Nulla dui urna, semper sit amet porta in, dapibus eget ante. Sed consequat lacinia vestibulum. Donec porttitor nisl vel dui congue vulputate. Quisque hendrerit neque vel libero lobortis efficitur.",
                "price": 100
            },
            {
                "title": "Object 2",
                "description": "Proin ac tortor et nisl pretium hendrerit eu sit amet arcu. Integer risus purus, varius eget dui auctor, dictum mollis lacus. Etiam sit amet metus ante. Donec et tortor mattis, efficitur purus vitae, porta arcu. Phasellus dictum, felis viverra euismod tristique, libero lorem facilisis odio, non luctus diam nisl vitae turpis. Aliquam at turpis quis nisl placerat tincidunt. Nam a hendrerit elit. Vivamus eget mi porta, pulvinar massa in, eleifend augue. ",
                "price": 150
            },
            {
                "title": "Object 2",
                "description": "Integer neque ex, tincidunt in suscipit in, elementum sit amet neque. Quisque pulvinar dui eget tellus porttitor, sed fringilla ligula imperdiet. Sed eu sem justo. Etiam a ullamcorper ipsum. Pellentesque varius orci vel velit cursus suscipit. Proin at congue nisl. Suspendisse vitae dolor in risus molestie tempor. Suspendisse nec metus magna. Proin sed quam lectus. Proin scelerisque dui purus, aliquam vehicula purus commodo id. Praesent fermentum ante semper erat rhoncus, eu congue ligula sollicitudin. Pellentesque viverra vehicula auctor. Sed quis lacus sem. ",
                "price": 250
            }
        ]

        return self.results

# 1. zadatak


class QuotesToScrapeClass:
    def __init__(self, html):
        self.html = html

    def get_html(self, url):
        response = requests.get(url)
        return response.text

    def parse(self, soup):
        # korištenje bs4 funkcije
        soup = BeautifulSoup(self.html, 'html.parser')
        # array varijabla
        quotes = []
        # pronaći sve div elemente sa class qoute i staviti ih u varijablu qoute_elements
        quote_elements = soup.find_all('div', class_='quote')

        # for petlja koja izvodi logiku izvlačenja svih potrebnih atributa
        for quote_element in quote_elements:
            url = quote_element.find('a')['href']
            url = 'http://quotes.toscrape.com/' + url
            text = quote_element.find('span', class_='text').text
            author = quote_element.find('small', class_='author').text
            tags = [tag.text for tag in quote_element.find_all(
                'a', class_='tag')]

            # stvaranje objekta sa url, text, author i tags parametrima
            quote = {
                'url': url,
                'text': text,
                'author': author,
                'tags': tags
            }
            # dodavanje objekta u array objekata
            quotes.append(quote)

        return quotes

# 2. zadatak


class BooksToScrapeClass:
    def __init__(self, html):
        self.html = html

    def parse(self, soup):
        # korištenje bs4 funkcije
        soup = BeautifulSoup(self.html, 'html.parser')
        # array varijabla
        books = []
        # pronaći sve article elemente sa class product_pod i staviti ih u varijablu book_elements
        book_elements = soup.find_all('article', class_='product_pod')

        # for petlja koja izvodi logiku izvlačenja svih potrebnih atributa
        for book_element in book_elements:
            # dobivanje punog URL
            url = book_element.find('h3').find('a')['href']
            url = 'https://books.toscrape.com/catalogue/' + url
            # dobivanje naziva knjige
            title = book_element.find(
                'div', class_='image_container').find('img')['alt']
            # dodavanje integera varijabli stock_broj ako je 'In stock', 0 ako nema u stocku
            stock = book_element.find('p', class_='instock availability')
            stock_broj = 1 if 'In stock' in stock.text else 0
            price = float(book_element.find(
                'p', class_='price_color').text[1:])
            # logika za vraćanje broja/integera umjesto string-a
            rating_element = book_element.find('p', class_='star-rating')
            rating_mapping = {'One': 1, 'Two': 2,
                              'Three': 3, 'Four': 4, 'Five': 5}
            rating = rating_mapping.get(rating_element['class'][1])

            # stvaranje objekta sa url, text, author i tags parametrima
            book = {
                'url': url,
                'title': title,
                'stock': stock_broj,
                'price': price,
                'rating': rating
            }
            books.append(book)

        return books

# 3. zadatak


class BookDepositoryClass:
    def __init__(self, html):
        self.html = html

    def parse(self, soup):
        soup = BeautifulSoup(self.html, 'html.parser')
        # array varijabla
        depository = []
        books = soup.find_all('div', class_='main-content')

        for book in books:
            # dobivanje url-a iz
            url = book.find('div', class_='item-img').find('a')['href']
            url = 'https://www.bookdepository.com/category/2638/History-Archaeology' + url
            # puni naslov knjige
            meta_element = book.find('meta', attrs={'itemprop': 'name'})
            title = meta_element['content']
            # dostupnost knjige
            stock = 1 if book.find('a', class_='add-to-basket') else 0
            # float broj cijene knjige
            price = float(
                book.find('span', class_='sale-price').text.replace('€', '').replace(',', '.'))
            # logika oko dobivanja low_price, ukoliko postoji onda je postavljen iz HTML koda, a ako ne postoji onda je jednak price varijabli
            low_price_element = book.find('span', class_='price-save')
            if low_price_element:
                low_price = float(low_price_element.text.replace(
                    '€', '').replace(',', '.'))
            else:
                low_price = price
            # računanje rejtinga kao float broj, pošto postoji i half-star koji sam stavio kao 0.5 vrijednost
            rating = float(len(book.find('div', class_='stars').find_all('span', class_='full-star')) +
                           (0.5*len(book.find('div', class_='stars').find_all('span', class_='half-stars'))))
            # traženje kategorije knjige pomoću find_previous bs4 metode
            category = book.find_previous('h2').text.strip()
            depo = {
                'url': url,
                'title': title,
                'stock': stock,
                'price': price,
                'low_price': low_price,
                'rating': rating,
                'category': category
            }
            depository.append(depo)

        return depository


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Invalid number of arguments.")
        sys.exit(1)
    else:
        file_name = sys.argv[1]
        # provjera postojanja HTML datoteke u folderu
        if os.path.isfile(file_name) != True:
            print("HR: Birana datoteka ne postoji.\nEN: The chosen file doesn't exist.")
            sys.exit(1)
        else:
            with open(file_name, encoding="utf8") as fp:
                soup = BeautifulSoup(fp, "lxml")
                if file_name == "quotes_to_scrape_test.html":
                    scraper = QuotesToScrapeClass(str(soup))
                elif file_name == "books_to_scrape_test.html":
                    scraper = BooksToScrapeClass(str(soup))
                elif file_name == "book_depository_test.html":
                    scraper = BookDepositoryClass(str(soup))

            results = scraper.parse(soup)
            print(results, end='\n')
    #   TODO: OVDJE NASTAVITI

    #   TODO: OVISNO O IMENU FILE-A (file_name) TREBA DODIJELITI JEDNU KLASU KOJA TREBA BITI DEFINIRANA RANIJE U KODU (ili u drugom file-u i onda importana u main)
    #   TE IZ TE KLASE ZOVNUTI parse() FUNKCIJU KOJA ĆE VRATITI LISTU OBJEKATA I DODIJELITI GA VARIJABLI

    #   TODO: AKO SE ZATRAŽI FILE KOJI NE POSTOJI TREBA SE ISPISATI PORUKA KOJA TO KAŽE
