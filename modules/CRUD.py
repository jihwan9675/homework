from database import Databases

class CRUD(Databases):
    def insertDB(self, schema, table, colum, data):
        sql = " INSERT INTO {schema}.{table}({colum}) VALUES ('{data}') ;".format(schema=schema,table=table,colum=colum,data=data)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e :
            print(" insert DB err ",e) 
    
    def readDB(self,schema,table,colum):
        sql = " SELECT {colum} from {schema}.{table}".format(colum=colum,schema=schema,table=table)
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except Exception as e :
            result = (" read DB err",e)
        
        return result

if __name__ == "__main__":
    db = CRUD()
    db.insertDB(schema='myschema',table='table',colum='ID',data='유동적변경')
    print(db.readDB(schema='myschema',table='table',colum='ID'))