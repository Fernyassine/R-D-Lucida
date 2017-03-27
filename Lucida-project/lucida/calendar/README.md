# Calendar

Calendar est un service Lucida qui parse les entrées texte en date.
Le command center est responsable de l'envoie des dates au front end,
et le front end recupères les évènements depuis votre calendrier Google.
Par exemple, pour la question entrée : `"Quelle était mon calendrier Google l'an passé ?"`
La reponse du service calendrier serait `"2015-01-01T00:00:00 2015-12-31T23:59:59"`
(basé sur le calendrier actuel).

## Déploiement local de Calendar

- Depuis ce dossier, tapez `make` pour compiler, puis tapez `make start_server` pour démarrer le service. Ce dernier a besoin de Java 8 pour fonctionner. 

- Depuis ce dossier, tapez `make start_test` pour tester le service lancé.
