import requests
from bs4 import BeautifulSoup as bsoup
import db_checker as dbchk

def get_response(url,site_tag):
    aggr_urls=[]
    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    site_req_url = requests.get(url, headers=agent)
    site_req_html= bsoup(site_req_url.content,'html.parser')
    # site_req_html.prettify()
    # print(site_req_html)
    
    if site_tag=="N7P":
        links=site_req_html.find_all('a', href=True, text=True,rel=True)
        for lk in links:
            # print(lk)
            for i in lk['rel']:
                if i=='bookmark':
                    # print(lk.string)
                    # print(lk['href'])
                    aggr_urls.append(lk.string)
                    aggr_urls.append(lk['href'])
    
    if site_tag=="W10":
        for i in site_req_html.select('article[class*="mspuloop"]'):#find_all('article',{"class":arti_tag})#'div', {"class": "shunno-loop-article-meta"})
            # print(i)
            lk=i.find_all('a',href=True,title=True)[0]
            aggr_urls.append(lk['title'])
            aggr_urls.append(lk['href'])

    return(aggr_urls)




if __name__ == "__main__":
    main_url=[("https://nokiapoweruser.com/tag/nokia-7-plus/","N7P"),
    ("https://mspoweruser.com/tag/windows-10/","W10")]
    # main_url=[("https://mspoweruser.com/tag/windows-10/","W10")]
    for i in main_url:
        # print(f"\n\n{i}")
        rslt=get_response(i[0],i[1])
        # flag=1
        dbchk.db_chk(rslt)
        # print(f"{i[0]},{i[1]}")
        # for a in rslt:
        #     print(a)