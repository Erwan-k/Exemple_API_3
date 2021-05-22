Hello,

Here you will find a docker-compose that manages two services : 
- a database based on mysql official image
- an API built from the files you will find next to our docker-compose

When building, the database use the data-init/dump.sql file.
The flask API allows you to adress two routes : connexion1 and connexion2.

connexion1 route allows you to add values to the table "Utilisateur".
connexion2 route allows you to fetch all values from the same table.

Enjoy,

Erwan
