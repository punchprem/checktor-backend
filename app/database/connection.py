
import MySQLdb
from dotenv import load_dotenv

db_config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': 'pp201102',
    'db': 'checktor',
}
conn = MySQLdb.connect(**db_config)

