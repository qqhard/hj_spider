cd splash_demo
scrapy crawl hj_spider > /tmp/hj_data.txt
cd ..
cat /tmp/hj_data.txt | python hj_select.py
