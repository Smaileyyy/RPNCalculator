Installez les dépendances Python à l'aide de pip :
pip install -r requirements.txt

Exécuter uvicorn à partir du répertoire parent de main.py et lancez le serveur FastAPI en exécutant la commande suivante :
uvicorn main:app --reload

Ouvrez votre navigateur et accédez à l'URL suivante pour accéder à Swagger et tester l'API :
http://localhost:8000/docs