# Djinn and Tonic

## Dépendances majeures

- [Caffe](http://caffe.berkeleyvision.org/)
- [Facebook Thrift](https://github.com/facebook/fbthrift)

# Structure

- `dig/`: implementation du service de reconnaissance de chiffres
- `face/`: implementation du service de reconnaissance faciale
- `imc/`: implementation du service de classification d'image
- `models/`: modèles DNN nécessaire pour les services précités
- `tools/`: dependances nécéssaires pour Djinn and Tonic

## Installation

```
make
```

## Lancement

```
cd dig # or face, or imc
make start_server
```

## Test

```
cd dig # or face, or imc
make start_test
```
