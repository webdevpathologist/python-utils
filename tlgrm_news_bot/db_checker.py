import tlgram_sender as df
import pymysql
import urllib.parse

# df.send_msg
def db_chk(agg_urls):
    titles_agg=[]
    for tm in agg_urls:
        if agg_urls.index(tm)%2==0:
            titles_agg.append(tm)
    
    cnctn = pymysql.connect(host='localhost',user='root',password='datpl@123',db='vs_mysql',charset='utf8mb4')
    cursor = cnctn.cursor()	
    cursor.execute("SELECT title FROM tl_news where sent_flag=1 order by row_id") 
    rows = cursor.fetchall()
    titles_db=[]
    for row in rows:
        titles_db.append(row[0])
        # print(f"{row[0]},{url[0]}")
    # titles_new=list(titles_agg.difference(titles_db))
    titles_new=[]
    for i in titles_agg:
        if i not in titles_db:
            titles_new.append(i)

    # print(titles_new)
    # print(agg_urls)
    # print(titles_agg)
   
    for i in titles_new:
        for j in agg_urls:
            # print(j)
            if i==j:
                # print(f"{i}=={j}")
                title=str(j)#.replace("&","&amp")
                url=agg_urls[agg_urls.index(j)+1]
                msg=title+"  "+url
                msg=urllib.parse.quote(msg)
                # msg.replace
                print(msg)
                sent_flag=df.send_msg(msg)
                if sent_flag:
                    ins_qry=f"insert into tl_news(url,title,sent_flag) values(\"{i}\",\"{j}\",1)"
                    cursor.execute(ins_qry)
                    print(ins_qry)
                if sent_flag==False:
                    ins_qry=f"insert into tl_news(url,title,sent_flag) values(\"{i}\",\"{j}\",0)"
                    cursor.execute(ins_qry)
                    print(ins_qry)
    cnctn.commit()
    cnctn.close()



    


if __name__ == "__main__":
    lnk=[["Updated: Nokia 6.1, Nokia 6.1 Plus, Nokia 7 Plus & Nokia 7.1 receiving August Security update now",
    "https://nokiapoweruser.com/nokia-7-1-nokia-6-1-plus-nokia-7-plus-receiving-august-security-update-now/"],
    ["test1","test1"]]
    db_chk(lnk)