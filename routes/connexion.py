from flask_restful import Api, Resource, reqparse
import os
from sqlalchemy.engine.url import make_url
import mysql.connector

def getMysqlConnection():
	url = make_url(os.getenv('DATABASE_URL'))
	mydb = mysql.connector.connect(host=url.host,user=url.username,passwd=url.password,database=url.database)
	return mydb

def mycursor_execute(sql,mycursor):
	try:
		mycursor.execute(sql)
		return {"statut":True}
	except Exception as e:
		return {"statut":False,"erreur":e}

def mycursor_fetchall(mycursor):
	try:
		s = mycursor.fetchall()
		return {"statut":True,"retour":s}
	except Exception as e:
		return {"statut":False,"erreur":e}

def mydb_commit(mydb):
	try:
		mydb.commit()
		return {"statut":True}
	except Exception as e:
		return {"statut":False,"erreur":e}


connexion1_post_args = reqparse.RequestParser()
connexion1_post_args.add_argument("param1",type=str,required=True)
connexion1_post_args.add_argument("param2",type=str,required=True)
connexion2_post_args = reqparse.RequestParser()
connexion2_post_args.add_argument("param3",type=int,required=True)
connexion2_post_args.add_argument("param4",type=int,required=True)


class connexion1(Resource):
	def post(self): #s_inscrire
		body = connexion1_post_args.parse_args()
		[param1,param2] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		mycursor.execute("INSERT INTO Utilisateur (Nom,Prenom,Adresse_mail,Mdp) VALUES (\""+param1+"\",\""+param2+"\",\"ok\",\"ok\")")
		mydb.commit()

		mycursor.close()
		mydb.close()

		return "ok"


class connexion2(Resource):
	def post(self): #verifier_son_adresse_mail
		body = connexion2_post_args.parse_args()
		[param3,param4] = [body[i] for i in body]
		mydb = getMysqlConnection()
		mycursor = mydb.cursor()

		mycursor.execute("SELECT * FROM Utilisateur")
		resultat = mycursor.fetchall()

		mycursor.close()
		mydb.close()

		return resultat


