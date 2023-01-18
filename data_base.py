import sqlite3


class Sqlite3DB:

    def __init__(self,name):
        self.connect = sqlite3.connect(name)
        self.open = self.connect.cursor()

    def create_table_not_exists(self, name, columons):
        columons_in_execute_structure = self.prepare_table_columns(columons)
        execute_line = 'CREATE TABLE IF NOT EXISTS "' + name + '" ' + columons_in_execute_structure
        self.open.execute(execute_line)
        self.connect.commit()

    def prepare_table_columns(self, columons):
        columons_str = "(" + columons[0]

        for columon in range(len(columons) - 1):
            columon += 1
            columons_str += ", " + columons[columon]
        
        columons_str += ")"

        return columons_str

    def excute_data_base_structure(self,tables):
            
            for table in tables:
                self.create_table_not_exists(table['table_title'], table['table_columons'])
                
