from data_base import Sqlite3DB
from data_base_structure import data_structure

# create the base of dataBase of the program:
project_DB = Sqlite3DB('progressive.sqlite')
project_DB.excute_data_base_structure(data_structure)


