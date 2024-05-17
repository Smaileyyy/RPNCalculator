# ToDo

## Améliorations à apporter

1. **Gestion des erreurs** : 
   - Ajouter des messages d'erreur plus informatifs.

2. **Tests unitaires** :
   - Écrire des tests unitaires pour chaque endpoint de l'API (on peut utiliser par exemple pytest pour automatiser les tests).

3. **Documentation** :
   - Ajouter des commentaires détaillés dans le code et améliorer la documentation Swagger pour inclure des descriptions plus détaillées des endpoints et des paramètres.

4. **Sécurité** :
   - Implémenter l'authentification et l'autorisation pour sécuriser les endpoints de l'API.

5. **Optimisation** :
   - Optimiser le stockage des piles pour une meilleure performance (On peut utiliser une base de données pour persister les piles au lieu de les stocker en mémoire).

## Raccourcis pris

1. **Stockage en mémoire** :
   - Les piles sont actuellement stockées en mémoire, ce qui est suffisant pour un prototype mais doit être remplacé par une solution persistante pour une utilisation en PROD.

2. **Gestion des utilisateurs** :
   - Aucune gestion des utilisateurs n'a été implémentée. Chaque pile est accessible par tous les utilisateurs, ce qui n'est pas sécurisé.

3. **Interface utilisateur** :
   - Aucune interface utilisateur (UI) n'a été créée. Seule l'interface Swagger est disponible pour interagir avec l'API.

4. **Logs** :
   - Les logs ne sont pas mis en place. Cela doit être ajouté pour surveiller l'état de l'API.

5. **Tests minimaux** :
   - Seuls des tests basiques ont été effectués, des tests plus complets et automatisés sont nécessaires pour assurer la stabilité du projet.
