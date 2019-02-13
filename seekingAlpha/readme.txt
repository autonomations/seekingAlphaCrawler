scrapy runspider SeekingAlphaSpider.py -a stocks='amd'


Python project and global variables may require different versions of the same package to function properly.  Therefore, it is important to set up virtual
environments such as 'pip install virtualenvwrapper' 'pip install virtualenv' or download Anaconda Navigator and use this to change your python virtual environment
variables

Major difference example:
Python 2 vs Python 3 handles their 'super method' differently which is a calling to their parent's class method
super(SeekingAlphaSpider, self).__init__(**kwargs)  # python3

USE:
Anaconda navigator and created a virtual environment and then went into my PyCharm and changed the terminal interpreter to that env
for using Scrapy library and for machine learning

Package Manager Examples
pip - Python ** we will be using this the majority of the time with python.  Use 'pip install _______'
apt-get - Windows
npm - Node Python Manager
yum

Goal 1: Acquire information in daily 'snapshots'
Goal 2: Add daily information to aggregate data
Goal 3: Separate out 'good data' or successful prediction
Goal 4: Using Natural Language Processing Sentiment Analysis, give every comment a score rank
Goal 5: Find 'commentors' or people that have more influence and give them a weighted eigan page rank (similar to google)

Next: Database:
CSV, JSON, and Document Object Store.  JSON and CSV are both pretty straight forward but to store in a database style
then we need to install Mongo.  Our natural language processor handles better with this style of input data organization
Install mongo + mongod
'mongod' #runserver

## How to look into Mongo Database
'''
    $ mongo
    $ show dbs #shows all dbs
    $ db # show current db
    $ use seekingalpha_db # switch to using that database
    $ show collections
    $ db.COLLECTION_NAME.find()
    $ db.COLLECTION_NAME.find().pretty()
'''


# Running
$ mongod #start server
$ scrapy runspider ./spiders/SeekingAlphaSpider.py -a stocks='amd, tsla, nvda' #run script to download



### Aim
To examine a number of different forecasting techniques to predict future stock returns based on past returns and numerical news indicators to construct a portfolio of multiple stocks in order to diversify the risk. We do this by applying supervised learning methods for stock price forecasting by interpreting the seemingly chaotic market data.

## Setup Instructions
```
    $ workon myvirtualenv                                  [Optional]
	$ pip install -r requirements.txt
	$ python scripts/Algorithms/regression_models.py <input-dir> <output-dir>
```

Download the Dataset needed for running the code from [here](https://drive.google.com/open?id=0B2lCmt16L_r3SUtrTjBlRHk3d1E).

## Project Concept Video
[![Project Concept Video](screenshots/presentation.gif)](https://www.youtube.com/watch?v=z6U0OKGrhy0)

### Methodology
1. Preprocessing and Cleaning
2. Feature Extraction
3. Twitter Sentiment Analysis and Score
4. Data Normalization
5. Analysis of various supervised learning methods
6. Conclusions

### Research Paper
- [Machine Learning in Stock Price Trend Forecasting. Yuqing Dai, Yuning Zhang](http://cs229.stanford.edu/proj2013/DaiZhang-MachineLearningInStockPriceTrendForecasting.pdf)
- [Stock Market Forecasting Using Machine Learning Algorithms. Shunrong Shen, Haomiao Jiang. Department of Electrical Engineering. Stanford University](http://cs229.stanford.edu/proj2012/ShenJiangZhang-StockMarketForecastingusingMachineLearningAlgorithms.pdf)
- [How can machine learning help stock investment?, Xin Guo](http://cs229.stanford.edu/proj2015/009_report.pdf)


### Datasets used
1. http://www.nasdaq.com/
2. https://in.finance.yahoo.com
3. https://www.google.com/finance


### Useful Links
- **Slides**: http://www.slideshare.net/SharvilKatariya/stock-price-trend-forecasting-using-supervised-learning
- **Video**: https://www.youtube.com/watch?v=z6U0OKGrhy0
- **Report**: https://github.com/scorpionhiccup/StockPricePrediction/blob/master/Report.pdf

### References
- [Scikit-Learn](http://scikit-learn.org/stable/)
- [Theano](http://deeplearning.net/software/theano/)
- [Recurrent Neural Networks - LSTM Models](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [ARIMA Models](http://people.duke.edu/~rnau/411arim.htm)
- https://github.com/dv-lebedev/google-quote-downloader
- [Book Value](http://www.investopedia.com/terms/b/bookvalue.asp)
- http://www.investopedia.com/articles/basics/09/simplified-measuring-interpreting-volatility.asp
- [Volatility](http://www.stock-options-made-easy.com/volatility-index.html)
- https://github.com/dzitkowskik/StockPredictionRNN
