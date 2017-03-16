from ConfigParser import SafeConfigParser
import urllib
import xlrd

config = SafeConfigParser()
config.read('utilities/config.ini')

# Read team data
teams_data_url = config.get('data_source', 'teams_data_url')
testfile = urllib.URLopener()
testfile.retrieve(teams_data_url, "teams.xls")
book = xlrd.open_workbook("teams.xls")
# book = xlrd.open_workbook("teams.xls")
# sheet = book.sheet_by_name("League Table")

#team_data_processing
# team_data_processing = team_data_processing(es_host, es_port)

# Establish a MySQL connection
#database = MySQLdb.connect (host="localhost", user = "root", passwd = "", db = "players")
# Get the cursor, which is used to traverse the database, line by line
#cursor = database.cursor()
