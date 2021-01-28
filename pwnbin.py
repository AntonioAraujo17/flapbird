import  time
import  urllib
import  datetime
import  sys, getopt
import  bs4 import BeautifulSoup
import  gzip
from io import StringIO

def main(arqv):

    length = 0
    time_out = False
    found_kw = []
    paste_list = set([])
    root_url = 'http://pastebin.com'
    raw_url = 'http://pastebin.com/raw/'
    start_time = datetime.datetime.now()
    file_name, kw, append, run_time, match_total, crawl_total = initialize_options(arqv)

    print('\n  Crawling %s Press ctrl+c to save file to %s' % (root_url, file_name))

    try:
        while True:

            root_html = BeautifulSoup(fetch_page(root_url), 'html.parser')

            for paste in find_new_pastes(root_html):

                length = len(paste_list)
                paste_list.add(paste)

                if len(paste_list) > length:

                    raw_paste = raw_url + paste
                    found_kw = find_keywords(raw_paste, found_kw, kw)

                else:

                    time_out = True

                if time_out:
                    time.sleep(2)

                sys.stdout.write("\r Crawled total of %d Pastes, Keyword matches %d" % (len(paste_list), len(found_kw)))
                sys.stdout.flush()














