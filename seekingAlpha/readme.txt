Python project and global variables may require different versions of the same package to function properly.  Therefore, it is important to set up virtual
environments such as 'pip install virtualenvwrapper' 'pip install virtualenv' or download Anaconda Navigator and use this to change your python virtual environment
variables

Major difference example:
Python 2 vs Python 3 handles their 'super method' differently which is a calling to their parent's class method
super(SeekingAlphaSpider, self).__init__(**kwargs)  # python3

I USE:
Anaconda navigator and created a virtual environment and then went into my PyCharm and changed the terminal interpreter to that env
for using Scrapy library and for machine learning

Package Managers
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

Look at collections
mongo
show dbs #shows all dbs
db # show current db
use seekingalpha_db # switch to using that database
show collections
db.COLLECTION_NAME.find()
db.COLLECTION_NAME.find().pretty()




Terminal
mongod #start server
scrapy runspider ./spiders/SeekingAlphaSpider.py -a stocks='amd, tsla, nvda' #run script to download
