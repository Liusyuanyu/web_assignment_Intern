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

filepath = 'html/my_file.html'

link_list = {'TNW: artificial-intelligence': ai_list}
link_list['TNW: smart phone'] = sp_list
link_list['TNW: data-analysis'] = da_list

news_scrap.write_result_as_html(filepath, link_list)