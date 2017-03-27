# Reconnaissance Automatique du language (Automatic Speech Recognition: ASR)

L'implémentation actuelle d'ASR utilise [Kaldi](http://kaldi.sourceforge.net/),
un outil de reconnaissance vocale écrit en C++ qui est librement utilisable sous licence Apache. 

## Notes:

1. `kaldi_gstreamer_asr` contient l'implémentation des services ASR de Kaldi.

2. Si vous desirez créé et utiliser une autre implémentation d'ASR,
Vous pouvez commencer par créer un dossier parallèle à `kaldi_gstreamer_asr` et modifier le `Makefile`.
Assurez vous de faire référence à `../lucidaservice.thrift` et `../lucidatypes.thrift`.

3. Tapez `make` pour construire toutes les implémentations d'ASR ,
ou tapez `cd kaldi_gstreamer_asr` et `make` pour créer seulement le service ASR.

