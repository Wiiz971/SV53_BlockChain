# SV53 projet d'initiation aux BlockChains


#### Informations générales :

* [Depôt Github](https://github.com/Wiiz971/SV53_BlockChain)
* Outils utilisés pour le projet :
    * Python 3.6.8
    * Spider version 5.2.2 
    * Importer le module ecdsa ’pip install ecdsa’ pour vérifier l’émetteur de la transaction
    * Importer le module hashlib ’pip install hashlib’ pour vérifier utiliser les clés de hachage (SHA256)

 #### Objectif du projet :

L’objectif du TP est de vous initier aux blockchains. 
Sur la blockchain qui sera conçu, lui manquera la preuve de travail à cause des temps de calculs impraticables avec les moyens mis à votre disposition. 

La structure de la blockchain étudiée est constituée comme suit:

  * 1. L’empreinte numériquedu blockprécédent: Utilisation de l’algorithme de hachagesha256
  * 2. La donnée du block:transaction
* 3. La signature de la transaction: La personne qui a le droit de réaliser la transaction, chiffre la transaction avec sa clé privée en utilisant ECDSA (Elliptic Curve Digital Signature Algorithm)
* 4. Preuve de travail : La phrase ajoutée par unmineur pour permettre d’obtenir un résultat d’empreinte numérique qui répond à la contrainte(20 zéros au début).
* 5. L’empreintenumérique du block actuel 

À la suite de cette définition,répondre aux questions suivantes:

* 1- Soit le code présenté dans le fichier main.py. Analyser le code et donner la structure des blockchains présents
* 2- Quels sont les parties manquantes de la blockchainet comment l’enrichir?
* 3- Ajouter la signature, pour vérifier l’émetteurde la transaction en utilisant [ecdsa](https://pypi.org/project/ecdsa/). Vous pouvez utiliser ecdsa pour générer votre proprepaire de clés,signer et vérifier la signature de la transaction.
* 4- Quel risque comporte cette blockchain, étant donné l’absence de la preuve de travail ?

