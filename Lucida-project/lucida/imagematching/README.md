# Reconnaissance d'Image (Image Matching: IMM)

L'implémentation actuelle de IMM utilise [OpenCV](http://opencv.org/), une bibliothèque open source sous licence BSD-licensed 
qui contient plusieurs centaines d'algorithmes de visions par ordinateur. 

## Notes:

1. `opencv_imm` contient l'implémentation du service OpenCV IMM. 

2. Si vous voulez créé et utiliser un autre module IMM,
vous pouvez commencer par crééer un dossier parallèle à `opencv_asr` et modifier `Makefile`.
Assurez vous de faire référence à `../lucidaservice.thrift` et `../lucidatypes.thrift`.

3. Tapez `make` pour construire toutes les implémentations de IMM,
ou tapez `cd opencv_imm` et `make` pour construire le service OpenCV IMM.
