import mysql.connector
import luigi

class LoadFromMySQL(luigi.Task):
    def run(self):
        cnx = mysql.connector.connect(user='root', password = 'root', database='sampledb', host='localhost',port = '3306')
        cursor = cnx.cursor()
        
        query = ("SELECT id,score FROM core_stats where id > 1")
        idip = 1
        
        cursor.execute(query, (idip))
        with self.output().open("w") as out_file:
            out_file.write("id,score")
            out_file.write("\n")
            for (id,score) in cursor:
                s = str(id)+","+str(score)
                out_file.write(s)
                out_file.write("\n")
        cursor.close()
        cnx.close()
    
    def output(self):
        return luigi.LocalTarget("data/loadFromMySQL.csv")
        

        
    
    
