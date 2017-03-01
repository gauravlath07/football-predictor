# noinspection PyPep8
import urllib
import json
import xlrd
import MySQLdb
import urllib2
import urllib
from ConfigParser import SafeConfigParser
from utilities.elasticsearch_interaction import ElasticSearchInteraction
from utilities.team_data_processing import team_data_processing

config = SafeConfigParser()
config.read('utilities/config.ini')

# elastic search
es_host = config.get('elasticsearch', 'HOST')
es_port = config.getint('elasticsearch', 'PORT')
es_index_name = config.get('elasticsearch', 'INDEX')
es_doc_type = config.get('elasticsearch', 'DOC_TYPE')
es = ElasticSearchInteraction(es_host, es_port)

# data sources
player_data_url = config.get('data_source', 'player_form_url')
team_data_url = config.get('data_source', 'teams_data_url')

# Read team data
# teams_data_url = config.get('data_source', 'teams_data_url')
# testfile = urllib.URLopener()
# testfile.retrieve(teams_data_url, "teams.xls")
# book = xlrd.open_workbook("teams.xls")
# sheet = book.sheet_by_name("League Table")

#team_data_processing
team_data_processing = team_data_processing()

# Establish a MySQL connection
#database = MySQLdb.connect (host="localhost", user = "root", passwd = "", db = "players")
# Get the cursor, which is used to traverse the database, line by line
#cursor = database.cursor()

#es.create_index(es_index_name)
# response = urllib.urlopen(player_data_url)
# data = json.loads(response.read())
# es.create_index(es_index_name)
# es.index_content(es_index_name, es_doc_type, data)

team_data_processing.get_team_names(es_host, es_port)

