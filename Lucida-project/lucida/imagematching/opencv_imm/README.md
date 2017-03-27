# OpenCV IMM

OpenCV IMM utilise [OpenCV](http://opencv.org/), une bibliothèque open source sous licence BSD
qui inclue des centaines d'algorithme de reconnaissance d'image par ordinateurr. 

## Dependances majeures

- [OpenCV](http://opencv.org/)
- [Facebook Thrift](https://github.com/facebook/fbthrift)
- [MongoDB](https://www.mongodb.com/)
 et [C++ legacy driver](https://github.com/mongodb/mongo-cxx-driver/tree/legacy)

# Structure

- `server/`: implementation du serveur IMM
- `test/`: implementation du client test IMM

## Compilation

```
make
```

## Lancement

Start the server:

```
make start_server
```

Attendez de voir `IMM at 8082`.

Sinon,

```
cd server
./imm_server
```

## Test

```
make start_test
```

Sinon,

```
cd test
./imm_client (num_images)
```

7 images `test/test*.jpg` sont fournies.

## Notes de développement

1. Le linker flags dans `server/Makefile` sont compliqués et doivent être modifiés avec précaution.
Spécifiquement, `-lmongoclient` doit être précédé par `-lssl` et `-lcrypto`.

2. `server/Image.cpp` utilise `cv::SurfFeatureDetector` pour transformer une image dans une matrice de description representés comme `std::string`,
et `server/IMMHandler.cpp` sauvegarde la matrice à l'intérieur et la charge depuis cette forme.
[GridFS](https://docs.mongodb.com/manual/core/gridfs/).
