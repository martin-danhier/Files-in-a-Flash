# Mazemerising-Cat

## Pour éviter de se marcher sur les pieds : 

- **Ne jamais commit directement dans master** (je m'occuperai des merges) => préférez créer une nouvelle branche à partir de master et travaillez dedans. Une fois que vous êtes contents de votre code, vous pouvez faire une pull request (une demande de merge) et je mergerai tout ça dans master si c'est bon et sans bugs. Il faut que le code dans master soit nickel, sans bugs, ni rien (final quoi); c'est pourquoi c'est préférable de travailler parallèlement

- si vous voulez utiliser l'invite de commande, il vous faudra enregistrer une "SSH KEY". Cela permet à github de savoir que l'utilisateur de la console est le même que votre compte github (impossible de savoir sinon). Voici [la page](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/) qui explique comment faire (c'est facile si on fait bien étape par étape) 

- Pour faire une pull request, allez juste dans l'onglet [Pull Requests](https://github.com/martin-danhier/Mazemerising-Cat/pulls) du repo et faites "nouvelle pull request". Sélectionnez votre branche (exemple : martin-branch) dans 'compare' et master dans 'base'. Ensuite vous validez :)

## Voici la liste des commandes utiles
Vous pouvez télécharger git bash (l'invite de commande) [à ce lien](https://git-scm.com/downloads). Si vous êtes sur linux, c'est préinstallé dans la plupart des cas.

- `git add <filename>` : ajouter un fichier à votre commit
- `git commit -m "<message>"` : faire un commit en local (message est une courte description de votre commit)
- `git commit -a -m "<message>"` : combine les deux commandes ci-dessus (add tous les fichiers modifiés et commit)
- `git status` : obtenir le status du repo
- `git log` : obtenir l'historique de la branche
- `git branch <branch name>` : crée une nouvelle branche à partir de la branche sur laquelle vous vous trouvez
- `git checkout <branch name or commit id>` : sélectionne la branche/le commit indiqué et update les fichiers en conséquence. Vous pouvez voir où vous êtes en faisant `git log --graph --all` (HEAD = où vous êtes) (MASTER = le plus à jour)
- `git merge <branch>` merge la branche indiquée vers la branche HEAD (où vous êtes). Vous n'aurez normalement pas besoin de cette commande, puisqu'on utilise des pull requests
- `git push -u origin <branch>` envoie la branche indiquée sur le serveur github (ne pushez pas master)
- `git pull` : met à jour votre repo local par rapport au repo en ligne "remote","origin"
- `git clone https://github.com/martin-danhier/Mazemerising-Cat.git` : crée une copie du repository en local et prépare toute la configuration (remote etc)
