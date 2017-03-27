# Déployer Lucida en utilisant Kubernetes

[instructions.ipynb](instructions.ipynb) est un tutoriel complet pour le déploiement de Lucida sur Mac en utilisant une machine virtuelle utilisant Ubuntu 14.04 (64 bits). Si vous êtes familier avec les commandes linux, les étapes suivantes devraient être suffisantes.

## Etapes

1. Pré-requis:
  Docker est installé et le port 8080 n'est pas utilisé, vous disposez d'au moins 18Go d'espace libre sur votre disque et de 7Go de mémoire.
  Si vous déployer sur [OS X](http://kubernetes.io/docs/getting-started-guides/minikube/), Virtualbox ou VMWare Fusion doivent être installés.
  L'image Docker contient toutes les dépendances compilés, les modèles ASR, les modèles DNN, Stanford CoreNLP packages, etc.
  En outre, assurez vous que votre Docker vous autorise à pull une image de 18Go.
  L'activité du disque à mesure que les données utilisateurs seront ajoutés à Lucida.
  Si vous avez besoin de définir des limites de mémoires RAM et CPU pour Kubernetes, référez vous au lien [this](http://kubernetes.io/docs/admin/limitrange/).

2. Lancer `sudo ./cluster_up_<your_os>.sh` pour créer un cluster Kubernetes sur une machine via Docker.
  Si vous avez besoin de créer un cluster sur plus d'une machine, référez vous à [the official documentation](http://kubernetes.io/docs/).

3. Ouvez `mongo-controller.yaml` et `qa-controller.yaml` et modifiez le champs `hostPath` pour pointer vers le dossier ou vous voulez stocker les données pour MongoDB et OpenEphyra.
  Assurez vous d'accorder les droits de lectures et écritures au dossier spécifié.

  Si vous choisissez Wikipédia comme source de données additionnelle pour la base de connaissance utilisateur, déplacez le dossier cible vers le répertoire créé à l'étape précedente selon le champs dans le fichier  `qa-controller.yaml`.
  Sinon, suprimez le champs `export wiki_indri_index=...` from the `args`.

  Modifiez le nombre de replication `*-controller`s si le nombre par défaut n'est pas suffisant.

4. Si vous préférez créer l'image Docker depuis [the top level Dockerfile](../../Dockerfile)
  plutôt que récuperer depuis [our Dockerhub](https://hub.docker.com/r/claritylab/lucida/), il est nécessaire de modifier le champs `image` de tous les `*-controller` et programmer un container local Kubernetes dans le registre.

5. Si vous avez un certificat SSL généré par [letsencrypt](https://letsencrypt.org/)
   et desirez installer https, il est nécessaire de modifier les fichiers suivant selon leurs commentaires: 

  ```
  web-controller-https.yaml
  asrmaster-controller-https.yaml
  ```
  
  , et de renommer ensuite les fichiers suivants:
  
  ```
  mv asrworker-controller-https.yaml asrworker-controller.yaml
  mv asrmaster-controller-https.yaml asrmaster-controller.yaml
  mv web-controller-https.yaml web-controller.yaml
  mv web-service-https.yaml web-service.yaml
  ```

6. Lancer `sudo ./start_services.sh` pour lancer tous les services et pods Kubernetes. 
  Il considère qu'un cluster local est installé.
  La récupération de l'image peut prendre un certain temps, et vous êtes susceptibles de voir des statuts d'erreur `ImagePullBackOff` s'il n'y a plus d'espace libre disponible sur votre appareil.
  Pour débugguer, vous pouvez lancer `kubectl get service|pod` pour vérifier l'état des services et pods,
  `kubectl describe pod <pod_name>` pour voir les détails (recommandé),
  `docker ps | grep <controller_name>` suivi par `docker exec -it <running_container_id> bash` pour aller à l'interieur du container courant.
  Par exemple,si vous voyez "Internal Server Error", vous devriez vérifier votre web container,
  et controler le fichier de log dans `/usr/local/lucida/lucida/commandcenter/apache/logs/`.
  De plus, si le container MongoDB est bloqué en position 'being created' sans progresser, 
  lancer `sudo netstat -tulpn | grep 27017` et tuer l'instance courante MongoDB qui utilise aussi le port 27017.
  Cela s'applique aussi pour les autres container, Memcached, qa, etc. Pour lesquelles les ports sont déjà utiliés et ne peuvent être démarrés. 

7. Ouvrer votre navigateur et aller à l'adresse `http://localhost:30000` (ou `https://<YOUR_DOMAIN_NAME>:30000` si vous avez installé https).
  Cette étape peut prendre quelques minutes avant que le serveur Apache ne se lance,
  mais si le chargement semble durer trop longtemps pour afficher la page d'index, utiliser le debug plus haut.

8. Pour détruire le cluster, lancer `docker ps`, ensuite `stop` et `rm` tous les containers lié à Kubernetes.
   La fonction ci dessous devrait vous être utile si vous souhaitez arreter et supprimer tous les container Docker.

  ```
  function docker-flush(){
    dockerlist=$(docker ps -a -q)
      if [ "${dockerlist}" != "" ]; then
        for d in ${dockerlist}; do
          echo "***** ${d}"
          docker stop ${d} 2>&1 > /dev/null
          docker rm ${d} 2>&1 > /dev/null
          done
        fi
  }
  ```
