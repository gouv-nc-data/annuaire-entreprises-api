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
