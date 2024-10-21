# Lancement de la base locale 
```
docker compose -f docker-compse.db.yml up
```

# Lancement de l'api
```
fastapi dev app/main.py
```

# Génération d'un nouvelle version de bdd
Modifier les models définis dans app/database/models.py
```
alembic revision --autogenerate -m "Message de modification"
```
La mise à jour de la base se fait automatiquement au démarrage de l'application

# Données de dev
Des données de tests peuvent être injectées via le script ./sql/init.sql en allant dans la console de webdb sur [http://localhost:22071](http://localhost:22071)

# Build de l'image locale 
```
docker build -t annuaire-entreprise
```

# Lancement de l'image locale
> [!WARNING]\
> ** Pré requis, la bdd doit être lancée **
```
docker run -e DATABASE_USERNAME=annuaire -e DATABASE_PASSWORD=annuaire -e DATABASE_NAME=annuaire -e DATABASE_URL=127.0.0.1 --network host annuaire-entreprise
```
