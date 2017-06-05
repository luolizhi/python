from scrapy import cmdline

cmdline.execute("scrapy crawl quoteSpider  ".split())
# cmdline.execute("scrapy crawl quoteSpider -o quotesall.jl  ".split())
# cmdline.execute("scrapy crawl quoteSpider -s CLOSESPIDER_ITEMCOUNT=4  ".split())