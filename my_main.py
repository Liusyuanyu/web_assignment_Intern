import wlog
import scrapwebsite

url_ai = "https://thenextweb.com/vocabulary/artificial-intelligence/"
url_smart_phone = "https://thenextweb.com/vocabulary/smartphone-2/"
url_da = "https://thenextweb.com/vocabulary/data-analysis/"

wlog.set_custom_log_info('html/error.log')
news_scrap = scrapwebsite.NewsScraper(url_ai, wlog)

news_scrap.retrieve_webpage()
news_scrap.write_webpage_as_html()
news_scrap.read_webpage_from_html()
news_scrap.convert_data_to_bs4()
ai_list = news_scrap.scrap_links(count=10)


news_scrap.change_url(url_smart_phone)
news_scrap.retrieve_webpage()
news_scrap.write_webpage_as_html()
news_scrap.read_webpage_from_html()
news_scrap.convert_data_to_bs4()
sp_list = news_scrap.scrap_links(count=10)

news_scrap.change_url(url_da)
news_scrap.retrieve_webpage()
news_scrap.write_webpage_as_html()
news_scrap.read_webpage_from_html()
news_scrap.convert_data_to_bs4()
da_list = news_scrap.scrap_links(count=10)


## Output to html files
homepath = 'html/my_front_page.html'
home_page= './my_front_page.html'

smart_phone_path = 'html/my_smart_phone_page.html'
smart_phone_page= './my_smart_phone_page.html'

da_path = 'html/my_da_page.html'
da_page= './my_da_page.html'

back_home = "<H4><a href=\"" + home_page+"\">Back Home</a></H4>"
goto_smartphone = "<H4><a href=\"" + smart_phone_page+"\">Go to Smart Phone</a></H4>"
goto_da = "<H4><a href=\"" + da_page+"\">Go to Data Aalysis</a></H4>"


with open(smart_phone_path, 'w') as fobj:
    title = str("<BODY><H3> TNW: smart phone </H3>")
    fobj.write(title)
    for tag in ai_list:
        fobj.write(str(tag.prettify()))
        fobj.write("<br/>")
    fobj.write(back_home)
    
with open(da_path, 'w') as fobj:
    title = str("<BODY><H3> TNW: data-analysis</H3>")
    fobj.write(title)
    for tag in sp_list:
        fobj.write(str(tag.prettify()))
        fobj.write("<br/>")
    fobj.write(back_home)

with open(homepath, 'w') as fobj:
    title = str("<BODY><H3> TNW: artificial-intelligence </H3>")
    fobj.write(title)
    for tag in da_list:
        fobj.write(str(tag.prettify()))
        fobj.write("<br/>")
    fobj.write(goto_smartphone)
    fobj.write(goto_da)  