# Files in a Flash
## Proposer un changement
1. Dans les fichiers du projet, ouvrez le fichier que vous voulez modifier, et cliquez sur le crayon pour éditer.
2. Faites vos modifications (ctrl+v, ou directement dans l'éditeur en ligne)
3. Tout en bas, dans "Titre", décrivez en 2 mots ce que vous avez fait (ex: "Spécification de get_frequences")
4. Sélectionnez **Créer une nouvelle branche et créer une pull request**, et puis cliquez sur le bouton vert "Propose file changes".
5. Cliquez sur le bouton "Créer une pull request" .

**Vous avez donc proposé les changements dans une pull request, et j'irai checker si c'est bien.**
- **Si c'est bien** : je mergerai vos changements dans la branche master (qui contient uniquement le code clean et sans bugs, pour éviter justement des mauvaises blagues).
- **S'il faut changer quelque chose** (exemples : syntax error, ou pylint pas content), je vous le dirai soit en répondant à la pull request, soit sur discord. À ce moment là, vous pouvez éditer vos changements :
  1. **Dans votre pull request**, cliquez sur l'onglet "**Fichiers modifiés**".
  2. **Ouvrez le fichier** à modifier, **éditez-le** via le crayon comme tout à l'heure.
  3. **Modifiez** le fichier, **nommez** vos changements mais cette fois, au lieu de créer une nouvelle branche et une nouvelle pull request, sélectionnez "**commit directement dans [nom de la branche]**" (la branche s'appelle par exemple martin-danhier-patch-1). Vérifiez juste que vous ne commitez pas directement dans la branche master.
  4. Vous avez alors modifié votre pull request, et je la checkerai à nouveau, et s'il faut encore changer quelque chose, c'est le même principe. Quand les changements deviennent parfaits, on les merge dans master. À terme, le code de master sera efficace, fonctionnel et propre et il y aura très peu de modif à faire dessus.


Ca peut faire peur au début, mais on s'y habitue vite et c'est pas si compliqué au final :)






## Infos : 

- **Ne jamais commit directement dans master** (je m'occuperai des merges) => préférez créer une nouvelle branche à partir de master et travaillez dedans. Une fois que vous êtes contents de votre code, vous pouvez faire une pull request (une demande de merge) et je mergerai tout ça dans master si c'est bon et sans bugs. Il faut que le code dans master soit nickel, sans bugs, ni rien (final quoi); c'est pourquoi c'est préférable de travailler parallèlement

- Pour faire une pull request, allez juste dans l'onglet [Pull Requests](https://github.com/martin-danhier/Files-in-a-Flash/pulls) du repo et faites "nouvelle pull request". Sélectionnez votre branche (exemple : martin-branch) dans 'compare' et master dans 'base'. Ensuite vous validez :)
