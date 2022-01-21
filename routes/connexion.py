from flask_restful import Resource, reqparse

def getMysqlConnection():
	url = make_url(os.getenv('DATABASE_URL'))
	mydb = mysql.connector.connect(host=url.host,user=url.username,passwd=url.password,database=url.database)
	return mydb


connexion1_post_args = reqparse.RequestParser()
connexion1_post_args.add_argument("param1",type=str,required=True)
connexion1_post_args.add_argument("param2",type=str,required=True)


class connexion1(Resource):
	def post(self): 
		body = connexion1_post_args.parse_args()
		[param1,param2] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		mycursor.execute("INSERT INTO Utilisateur (Nom,Prenom,Adresse_mail,Mdp) VALUES (\""+param1+"\",\""+param2+"\",\"ok\",\"ok\")")
		mydb.commit()

		mycursor.close()
		mydb.close()

		return "ok"


