from pymongo import MongoClient
uri = "mongodb+srv://raihanazmi37_db_user:Hasanarrazaq37@cluster0.j18eyus.mongodb.net/?appName=Cluster0"
try:
    client = MongoClient(uri)
    print("Koneksi berhasil!")
    print(client.list_database_names())
except Exception as e:
    print("Koneksi gagal:", e)