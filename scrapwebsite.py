from urllib.request import urlopen 
from bs4 import BeautifulSoup

url_default   = 'https://thenextweb.com/'
filepath = 'html/output.html'
    
class NewsScraper:
    __url   = ''
    __data  = ''
    __wlog  = None
    __soup  = None 
    
    def __init__(self, url, wlog):
        self.__url  = url 
        self.__wlog = wlog 
    
    def retrieve_webpage(self):
        try:
            html = urlopen(self.__url)
        except Exception as e:
            print (e)
            self.__wlog.report(str(e))
        else:
            self.__data = html.read()
            if len(self.__data) > 0:
                print ("Grabed successfully: " , self.__url)
            
    def write_webpage_as_html(self, filepath=filepath, data=''):
        try:
            with open(filepath, 'wb') as fobj:
                if data:
                    fobj.write(data)
                else:
                    fobj.write(self.__data)
        except Exception as e:
            print(e)
            self.__wlog.report(str(e))
            
    def read_webpage_from_html(self, filepath=filepath):
        try:
            with open(filepath,encoding="utf8") as fobj:
                self.__data = fobj.read()
        except Exception as e:
            print (e)
            self.__wlog.report(str(e))
            
    def change_url(self, url):
        self.__url = url
            
    def convert_data_to_bs4(self):
        self.__soup = BeautifulSoup(self.__data, "html.parser")
		
    def scrap_links(self, count):
        link_list =[]
        news_list = self.__soup.find_all(['h4'])
        for tag in news_list:
            if count==0:
                break;
            if tag.a.get('href'):
                # print (tag.a.string.strip(),"\n",tag.a.get('href'))
                link_list.append(tag.a)	
                count -=1
        return link_list
    
    def write_result_as_html(self, filepath=filepath, links={}):
        try:
            if links :
                # fobj.write(data)
                with open(filepath, 'w') as fobj:
                    for name, link_list in links.items():
                        title = str("<BODY><H3>" + name + "</H3>")
                        fobj.write(title)
                        for tag in link_list:
                            fobj.write(str(tag.prettify()))
                            fobj.write("<br/>")
        except Exception as e:
            print(e)
            self.__wlog.report(str(e))