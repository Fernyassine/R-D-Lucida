# Réponses aux questions (Question Answering:QA)

L'implémentation actuelle de QA utilise OpenEphyra, un projet open source de 
Carnegie Mellon.

## Notes:

1. `OpenEphyra` contient l'implémentation de OpenEphyra QA service.

2. Si vous voulez créer et utiliser un autre module QA,
Vous pouvez commencer par créer un dossier parallèle à `OpenEphyra` et modifier `Makefile`.
Assurez vous de faire référence à  `../lucidaservice.thrift` et `../lucidatypes.thrift`.

3. Tapez `make` pour construire tous les modules QA,
ou tapez `cd OpenEphyra` et `make` pour construire simplement le service OpenEphyra QA.
