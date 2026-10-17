# Équations mathématiques animées
## Deuxième édition : nouvelles courbes, paramètres et logiciels gratuits

Ce document est la **seconde version**, plus approfondie, du guide des courbes mathématiques visuelles. Il ajoute de nouvelles représentations, explique précisément comment animer les paramètres et propose des logiciels gratuits pour voir le résultat en temps réel.

L’objectif est de pouvoir saisir une équation, créer un curseur pour une constante telle que \(a\), \(b\), \(n\) ou \(\varphi\), puis observer immédiatement la déformation, la rotation, l’ouverture ou la pulsation de la courbe.

---

## 1. Les trois niveaux d’animation

### Animation manuelle
Tu déplaces toi-même un curseur. C’est le meilleur mode pour comprendre l’effet exact d’un paramètre.

Exemple :

```text
r = a*cos(n*theta)
```

- Fais glisser `a` : la rose grandit ou rétrécit.
- Fais glisser `n` : le nombre de pétales change.

### Animation automatique
Le logiciel fait varier automatiquement un paramètre entre une valeur minimale et une valeur maximale.

Dans GeoGebra, un curseur peut être animé automatiquement : on choisit `Animation On`, puis on règle la vitesse, le sens et le mode de répétition. [web:31][web:36]

Dans Desmos, les curseurs permettent de jouer différentes valeurs d’une variable ; on peut contrôler leur vitesse, leur direction et leurs bornes. [web:33][web:39]

### Animation temporelle
Le paramètre dépend du temps, souvent noté `time`, `t` ou `frameCount`.

Exemple :

\[
a(t)=1+0.3\sin(t)
\]

La courbe respire alors continuellement :

```text
r = (1 + 0.3sin(t))*cos(5theta)
```

---

## 2. Vocabulaire des animations

| Terme | Signification | Exemple visuel |
|---|---|---|
| Pulsation | La courbe grossit puis rétrécit | \(a=1+0.3\sin(t)\) |
| Rotation | La figure tourne autour de l’origine | \(\theta\mapsto\theta+\omega t\) |
| Oscillation | Un paramètre varie périodiquement | \(b=2+\sin(t)\) |
| Déphasage | La forme se décale dans le temps | \(\varphi=\omega t\) |
| Morphing | Une courbe se transforme progressivement en une autre | Variation continue de \(n\) |
| Traçage progressif | La courbe se dessine au fil du temps | \(0\le\theta\le T(t)\) |
| Spirale dynamique | La courbe s’enroule ou se déroule | \(r=e^{b(t)\theta}\) |

---

## 3. Méthode universelle pour animer

### Étape 1 : identifier le paramètre
Choisis une constante dans l’équation : \(a\), \(b\), \(n\), \(k\) ou \(\varphi\).

### Étape 2 : créer un curseur
Donne-lui un intervalle pertinent.

| Paramètre | Intervalle conseillé | Effet |
|---|---|---|
| \(a\) | 0,1 à 5 | Taille |
| \(b\) | -1 à 1 | Vitesse de spirale |
| \(n\) | 1 à 12 | Pétales ou branches |
| \(\varphi\) | 0 à \(2\pi\) | Rotation ou phase |
| \(t\) | 0 à \(20\pi\) | Parcours ou temps |

### Étape 3 : remplacer une constante par une fonction du temps
Utilise une fonction périodique :

\[
a(t)=a_0+A\sin(\omega t+\varphi)
\]

- \(a_0\) : valeur moyenne.
- \(A\) : amplitude de la variation.
- \(\omega\) : vitesse de l’animation.
- \(\varphi\) : décalage initial.

### Étape 4 : tester plusieurs vitesses
Une valeur trop grande de \(\omega\) rend l’animation illisible. Commence par :

```text
omega = 0.2
```

---

## 4. Animations de la rose de Rhodonea

### Rose pulsante
\[
r=(1+0.3\sin t)\cos(5\theta)
\]

**Syntaxe Desmos :**

```text
r = (1 + 0.3sin(t))*cos(5theta)
0 <= theta <= 2pi
```

Fais varier `t` de \(0\) à \(20\pi\). La rose grossit puis se contracte.

### Rose dont le nombre de pétales évolue
\[
r=\cos(n\theta)
\]

```text
r = cos(n*theta)
0 <= theta <= 2pi
```

Crée un curseur :

```text
n = 3
```

Fais-le varier de 1 à 10. Pour des valeurs entières, la forme change par paliers ; pour des valeurs non entières, la rose devient incomplète ou entrelacée.

### Rose en rotation
\[
r=\cos(5(\theta-\omega t))
\]

**Syntaxe :**

```text
r = cos(5(theta - 0.2t))
0 <= theta <= 2pi
```

La rose tourne continuellement.

### Rose spirale
\[
r=e^{0.08\theta}\cos(5\theta)
\]

```text
r = e^(0.08theta)*cos(5theta)
0 <= theta <= 8pi
```

Pour animer l’ouverture :

\[
r=e^{b\theta}\cos(5\theta)
\]

```text
r = e^(b*theta)*cos(5theta)
0 <= theta <= 8pi
```

Fais varier `b` entre 0 et 0,2.

---

## 5. Animations du cœur

### Cœur qui bat
Partir du cœur paramétrique classique :

\[
x=16\sin^3u
\]

\[
y=13\cos u-5\cos(2u)-2\cos(3u)-\cos(4u)
\]

Ajouter un facteur de pulsation :

\[
s(t)=1+0.08\sin(t)
\]

\[
x=s(t)\cdot16\sin^3u
\]

\[
y=s(t)\left(13\cos u-5\cos(2u)-2\cos(3u)-\cos(4u)\right)
\]

**Syntaxe Desmos :**

```text
s = 1 + 0.08sin(t)
(s*16sin^3(u), s*(13cos(u)-5cos(2u)-2cos(3u)-cos(4u)))
0 <= u <= 2pi
```

Fais varier `t` de \(0\) à \(20\pi\). Le cœur bat.

### Cœur qui tourne
Appliquer une rotation d’angle \(\alpha=\omega t\) :

\[
x'=x\cos\alpha-y\sin\alpha
\]

\[
y'=x\sin\alpha+y\cos\alpha
\]

### Cœur qui se déforme
Fais varier séparément la largeur et la hauteur :

\[
x=h(t)\cdot16\sin^3u
\]

\[
y=v(t)\left(13\cos u-5\cos(2u)-2\cos(3u)-\cos(4u)\right)
\]

Exemple :

```text
h = 1 + 0.15sin(t)
v = 1 + 0.10cos(t)
(h*16sin^3(u), v*(13cos(u)-5cos(2u)-2cos(3u)-cos(4u)))
0 <= u <= 2pi
```

---

## 6. Animations du papillon de Fay

### Papillon statique
\[
r=e^{\sin\theta}-2\cos(4\theta)+\sin^5\left(\frac{2\theta-\pi}{24}\right)
\]

```text
r = e^(sin(theta))-2cos(4theta)+sin((2theta-pi)/24)^5
0 <= theta <= 12pi
```

### Papillon qui bat des ailes
Remplacer le coefficient \(2\) par une fonction périodique :

\[
c(t)=2+0.5\sin(t)
\]

\[
r=e^{\sin\theta}-c(t)\cos(4\theta)+\sin^5\left(\frac{2\theta-\pi}{24}\right)
\]

**Syntaxe :**

```text
c = 2 + 0.5sin(t)
r = e^(sin(theta))-c*cos(4theta)+sin((2theta-pi)/24)^5
0 <= theta <= 12pi
```

### Papillon qui tourne
\[
r=e^{\sin(\theta-\omega t)}-2\cos(4(\theta-\omega t))+\sin^5\left(\frac{2(\theta-\omega t)-\pi}{24}\right)
\]

**Syntaxe :**

```text
w = 0.15
r = e^(sin(theta-w*t))-2cos(4(theta-w*t))+sin((2(theta-w*t)-pi)/24)^5
0 <= theta <= 12pi
```

---

## 7. Nouvelles courbes à explorer

### 7.1 Hypotrochoïde
Une hypotrochoïde est obtenue lorsqu’un point situé sur un cercle roule à l’intérieur d’un autre cercle.

\[
x=(R-r)\cos t+d\cos\left(\frac{R-r}{r}t\right)
\]

\[
y=(R-r)\sin t-d\sin\left(\frac{R-r}{r}t\right)
\]

**Paramètres :**
- \(R\) : rayon du cercle fixe.
- \(r\) : rayon du cercle roulant.
- \(d\) : distance du point au centre du cercle roulant.

**Exemple animé :**

```text
R = 5
r = 3
d = 5
((R-r)*cos(t)+d*cos((R-r)/r*t), (R-r)*sin(t)-d*sin((R-r)/r*t))
0 <= t <= 2pi
```

Fais varier `d` pour voir le motif se déformer.

### 7.2 Épitrochoïde
Un point situé sur un cercle roule à l’extérieur d’un autre cercle.

\[
x=(R+r)\cos t-d\cos\left(\frac{R+r}{r}t\right)
\]

\[
y=(R+r)\sin t-d\sin\left(\frac{R+r}{r}t\right)
\]

**Exemple :**

```text
R = 4
r = 1
d = 2
((R+r)*cos(t)-d*cos((R+r)/r*t), (R+r)*sin(t)-d*sin((R+r)/r*t))
0 <= t <= 2pi
```

### 7.3 Courbe de la spirale hyperbolique
\[
r=\frac{a}{\theta}
\]

```text
r = a/theta
theta > 0
0 < theta <= 12pi
```

Fais varier `a` pour changer la taille de la spirale.

### 7.4 Conchoïde de Nicomède
\[
r=a+\frac{b}{\cos\theta}
\]

```text
r = a + b/cos(theta)
-pi/2 < theta < pi/2
```

**Paramètres :**
- `a` déplace la courbe.
- `b` contrôle l’écartement des branches.

### 7.5 Cissoïde de Dioclès
\[
y^2=\frac{x^3}{2a-x}
\]

```text
y^2 = x^3/(2a-x)
x < 2a
```

### 7.6 Strophoïde
\[
r=a\frac{\cos(2\theta)}{\cos\theta}
\]

```text
r = a*cos(2theta)/cos(theta)
-pi/2 < theta < pi/2
```

### 7.7 Courbe du diable
\[
y^2(y^2-x^2)=x^2(a^2-x^2)
\]

```text
y^2(y^2-x^2) = x^2(a^2-x^2)
```

### 7.8 Courbe du nœud de trèfle
En coordonnées paramétriques :

\[
x=\sin t+2\sin(2t)
\]

\[
y=\cos t-2\cos(2t)
\]

\[
z=-\sin(3t)
\]

Pour une représentation plane, on peut tracer \(x\) et \(y\) seulement :

```text
(sin(t)+2sin(2t), cos(t)-2cos(2t))
0 <= t <= 2pi
```

### 7.9 Courbe de l’étoile à cinq branches
\[
r=1+0.4\cos(5\theta)
\]

```text
r = 1 + 0.4cos(5theta)
0 <= theta <= 2pi
```

Pour l’animer :

```text
r = 1 + (0.2 + 0.2sin(t))*cos(5theta)
0 <= theta <= 2pi
```

### 7.10 Courbe de la méduse
\[
r=1+0.3\sin(6\theta)+0.1\sin(18\theta)
\]

```text
r = 1 + 0.3sin(6theta) + 0.1sin(18theta)
0 <= theta <= 2pi
```

Pour une pulsation :

```text
r = 1 + (0.2 + 0.15sin(t))*sin(6theta) + 0.1sin(18theta)
0 <= theta <= 2pi
```

---

## 8. Courbes harmoniques composées

Ces équations permettent de créer des motifs très riches à partir de quelques curseurs.

### Fleur harmonique
\[
r=a+b\cos(n\theta)+c\sin(m\theta)
\]

```text
r = a + b*cos(n*theta) + c*sin(m*theta)
0 <= theta <= 2pi
```

**Exemple :**

```text
a = 2
b = 1
c = 0.5
n = 5
m = 7
```

### Coquille harmonique
\[
r=e^{b\theta}(a+c\cos(n\theta))
\]

```text
r = e^(b*theta)*(a + c*cos(n*theta))
0 <= theta <= 12pi
```

### Fleur vibrante
\[
r=a+b\cos(n\theta+c\sin(k\theta))
\]

```text
r = a + b*cos(n*theta + c*sin(k*theta))
0 <= theta <= 2pi
```

Fais varier `c` pour créer une déformation ondulatoire.

### Spirale fleurie
\[
r=e^{b\theta}\left(a+c\cos(n\theta)\right)
\]

```text
r = e^(b*theta)*(a + c*cos(n*theta))
0 <= theta <= 16pi
```

---

## 9. Superformula animée

La superformula est l’une des familles les plus puissantes pour créer des formes organiques.

\[
r(\theta)=\left(\left|\frac{\cos\left(\frac{m\theta}{4}\right)}{a}\right|^{n_2}
+\left|\frac{\sin\left(\frac{m\theta}{4}\right)}{b}\right|^{n_3}\right)^{-1/n_1}
\]

### Version pulsante
Fais varier \(n_1\) :

\[
n_1(t)=0.5+0.2\sin(t)
\]

```text
n1 = 0.5 + 0.2sin(t)
r = ((abs(cos(m*theta/4)/a)^(n2) + abs(sin(m*theta/4)/b)^(n3))^(-1/n1))
0 <= theta <= 2pi
```

### Version rotative
Fais tourner la figure en décalant \(\theta\) :

\[
r\left(\theta-\omega t\right)
\]

```text
w = 0.2
r = ((abs(cos(m*(theta-w*t)/4)/a)^(n2) + abs(sin(m*(theta-w*t)/4)/b)^(n3))^(-1/n1))
0 <= theta <= 2pi
```

### Paramètres conseillés

| Forme | \(m\) | \(a\) | \(b\) | \(n_1\) | \(n_2\) | \(n_3\) |
|---|---:|---:|---:|---:|---:|---:|
| Étoile à 5 branches | 5 | 1 | 1 | 0,3 | 0,3 | 0,3 |
| Fleur à 6 pétales | 6 | 1 | 1 | 0,5 | 0,5 | 0,5 |
| Feuille | 2 | 1 | 1 | 0,7 | 0,3 | 0,3 |
| Polygone arrondi | 4 | 1 | 1 | 1 | 1 | 1 |
| Forme complexe | 8 | 1 | 1 | 0,4 | 0,6 | 0,6 |

---

## 10. Courbes de Lissajous animées

### Forme de base
\[
x=A\sin(at+\varphi)
\]

\[
y=B\sin(bt)
\]

```text
(A*sin(a*t+phi), B*sin(b*t))
0 <= t <= 2pi
```

### Animation par déphasage
Fais varier \(\varphi\) avec le temps :

\[
\varphi=\omega t
\]

```text
w = 0.3
(3sin(3t+w*t), 2sin(2t))
0 <= t <= 2pi
```

La figure se transforme continuellement sans changer ses fréquences.

### Animation par fréquence
\[
a(t)=3+0.5\sin(t)
\]

```text
a = 3 + 0.5sin(t)
(3sin(a*t), 2sin(2t))
0 <= t <= 2pi
```

### Nœud harmonique
\[
x=3\sin(3t+\pi/2)
\]

\[
y=2\sin(2t)
\]

```text
(3sin(3t+pi/2), 2sin(2t))
0 <= t <= 2pi
```

---

## 11. Logiciels gratuits recommandés

### 11.1 Desmos
**Type :** traceur graphique en ligne et application.

**Usage idéal :**
- Tester rapidement une équation polaire, paramétrique ou implicite.
- Créer des curseurs pour \(a\), \(b\), \(n\), \(\varphi\).
- Voir la courbe se modifier instantanément.
- Exporter une image ou partager un graphique.

**Avantages :**
- Très simple, gratuit et accessible depuis un navigateur.
- Les curseurs permettent d’animer les paramètres et de contrôler leur vitesse, direction et bornes. [web:33][web:39][web:41]
- Excellent pour prototyper une équation avant de la coder.

**Limite :**
- Moins adapté aux vidéos complexes ou aux animations très personnalisées.

**Conseil :** commence toujours par Desmos pour valider une équation.

### 11.2 GeoGebra
**Type :** logiciel de mathématiques dynamiques.

**Usage idéal :**
- Créer des curseurs animés automatiquement.
- Construire des figures géométriques interactives.
- Tracer des courbes polaires et paramétriques.
- Explorer des transformations en 2D et 3D.

**Avantages :**
- Gratuit, utilisable en ligne ou hors ligne.
- GeoGebra permet d’animer des nombres, angles et points contraints sur des objets ; la vitesse et le mode de répétition sont réglables. [web:31][web:36]
- La suite GeoGebra permet de tracer fonctions, équations, courbes et surfaces en 2D et 3D, avec des curseurs. [web:48][web:51][web:52]

**Limite :**
- Interface plus dense que Desmos.

**Conseil :** utilise GeoGebra lorsque tu veux une animation automatique, une construction géométrique ou une exploration 3D.

### 11.3 p5.js
**Type :** bibliothèque JavaScript de creative coding.

**Usage idéal :**
- Créer des animations interactives dans le navigateur.
- Faire dépendre les paramètres du temps avec `frameCount`.
- Ajouter couleurs, transparence, particules, souris et clavier.
- Publier une animation web directement.

**Avantages :**
- Gratuit et open source.
- Très adapté aux projets artistiques et génératifs.
- La bibliothèque `p5.Polar` facilite le passage des coordonnées polaires aux coordonnées cartésiennes et propose des exemples d’animation avec `sin()` et `frameCount`. [web:53][web:56]

**Limite :**
- Nécessite d’écrire du code JavaScript.

**Exemple minimal :**

```javascript
function setup() {
  createCanvas(600, 600);
}

function draw() {
  background(15);
  translate(width / 2, height / 2);
  noFill();
  stroke(255);

  beginShape();
  for (let theta = 0; theta < TWO_PI; theta += 0.01) {
    let r = 150 * cos(5 * theta + frameCount * 0.02);
    let x = r * cos(theta);
    let y = r * sin(theta);
    vertex(x, y);
  }
  endShape(CLOSE);
}
```

Ici, `frameCount` fait tourner progressivement la rose.

### 11.4 Manim Community
**Type :** bibliothèque Python pour créer des vidéos mathématiques.

**Usage idéal :**
- Réaliser des vidéos explicatives de haute qualité.
- Animer une équation, sa courbe et ses paramètres.
- Créer des transitions, du texte mathématique et des rendus MP4.

**Avantages :**
- Gratuit et open source.
- Conçu précisément pour les animations mathématiques.
- Manim permet d’animer les propriétés d’un objet avec `play()` et `animate()`. [web:34][web:37][web:38]
- Le rendu d’une scène se fait notamment avec une commande telle que `manim -pql scene.py SquareToCircle`. [web:35][web:44]

**Limite :**
- Demande Python et un peu de programmation.
- Ce n’est pas le meilleur outil pour une exploration instantanée par curseurs.

**Conseil :** utilise Manim après avoir validé l’équation dans Desmos ou GeoGebra, afin de produire une vidéo finale.

### 11.5 Wolfram Alpha
**Type :** moteur de calcul et visualisation.

**Usage idéal :**
- Vérifier une équation.
- Tracer rapidement une courbe polaire ou paramétrique.
- Explorer des variantes mathématiques.

**Limite :**
- Moins pratique pour créer des animations interactives complètes.

### 11.6 Matplotlib avec Python
**Type :** bibliothèque Python de visualisation.

**Usage idéal :**
- Tracer des courbes très précises.
- Créer des animations exportables en GIF ou MP4.
- Automatiser la génération de centaines de variantes.

**Limite :**
- Moins interactif que Desmos, GeoGebra ou p5.js.

---

## 12. Quel logiciel choisir ?

| Besoin | Logiciel conseillé | Pourquoi |
|---|---|---|
| Tester une équation rapidement | Desmos | Curseurs simples et visualisation immédiate |
| Animer automatiquement un paramètre | GeoGebra | Animation native des curseurs |
| Créer une animation web interactive | p5.js | Contrôle total du temps, des couleurs et des interactions |
| Produire une vidéo pédagogique | Manim Community | Rendu vidéo professionnel |
| Faire des calculs et vérifications | Wolfram Alpha | Calcul symbolique et tracés rapides |
| Générer beaucoup d’images ou de vidéos | Python + Matplotlib | Automatisation facile |

---

## 13. Atelier pratique : rose animée dans Desmos

1. Ouvre Desmos.
2. Tape :

```text
r = (1 + 0.3sin(t))*cos(5theta)
0 <= theta <= 2pi
```

3. Desmos proposera de créer un curseur pour `t`.
4. Clique sur le bouton de lecture du curseur.
5. Règle le domaine de `t` entre 0 et \(20\pi\).
6. Observe la rose pulser.

## 14. Atelier pratique : papillon animé dans GeoGebra

1. Ouvre GeoGebra.
2. Crée un curseur `t` entre 0 et \(20\pi\).
3. Active l’animation du curseur.
4. Tape une équation polaire animée :

```text
r = e^(sin(theta - 0.15t)) - 2cos(4(theta - 0.15t)) + sin((2(theta - 0.15t) - pi)/24)^5
```

5. Observe le papillon tourner.

GeoGebra permet précisément de définir un curseur avec un intervalle, un incrément, une vitesse et un mode d’animation. [web:36][web:58]

## 15. Atelier pratique : rose interactive en p5.js

```javascript
let n = 5;

function setup() {
  createCanvas(700, 700);
}

function draw() {
  background(10);
  translate(width / 2, height / 2);
  noFill();
  stroke(0, 200, 255);

  beginShape();
  for (let theta = 0; theta < TWO_PI; theta += 0.005) {
    let r = 220 * cos(n * theta + frameCount * 0.01);
    let x = r * cos(theta);
    let y = r * sin(theta);
    vertex(x, y);
  }
  endShape(CLOSE);
}

function keyPressed() {
  if (keyCode === RIGHT_ARROW) {
    n += 1;
  }
  if (keyCode === LEFT_ARROW && n > 1) {
    n -= 1;
  }
}
```

- Les flèches gauche et droite changent le nombre de pétales.
- `frameCount` anime la rotation.
- Tu peux remplacer `220` par `200 + 40*sin(frameCount/30)` pour créer une pulsation.

---

## 16. Bibliothèque de 30 équations animées

| Numéro | Nom | Équation à saisir | Animation |
|---:|---|---|---|
| 1 | Rose pulsante | `r = (1+0.3sin(t))*cos(5theta)` | Pulsation |
| 2 | Rose tournante | `r = cos(5(theta-0.2t))` | Rotation |
| 3 | Rose à pétales variables | `r = cos(n*theta)` | Changement de pétales |
| 4 | Rose spirale | `r = e^(0.08theta)*cos(5theta)` | Spirale |
| 5 | Cœur battant | `s=1+0.08sin(t)` puis multiplication du cœur par `s` | Battement |
| 6 | Cœur tournant | Rotation d’angle `0.1t` | Rotation |
| 7 | Cœur respirant | `h=1+0.15sin(t)`, `v=1+0.1cos(t)` | Déformation |
| 8 | Papillon vibrant | `c=2+0.5sin(t)` dans le terme `-c*cos(4theta)` | Battement d’ailes |
| 9 | Papillon tournant | Remplacer `theta` par `theta-0.15t` | Rotation |
| 10 | Cardioïde pulsante | `r = (1+0.2sin(t))*(1+cos(theta))` | Pulsation |
| 11 | Lemniscate tournante | `r^2 = 4cos(2(theta-0.2t))` | Rotation |
| 12 | Astroïde pulsante | `a=3+0.5sin(t)` | Pulsation |
| 13 | Hypotrochoïde déformée | Faire varier `d` | Motif évolutif |
| 14 | Épitrochoïde animée | Faire varier `d` ou `r` | Motif évolutif |
| 15 | Spirale d’Archimède | `r = 0.1theta` | Spirale régulière |
| 16 | Spirale logarithmique | `r = e^(0.2theta)` | Croissance exponentielle |
| 17 | Spirale inversée | `r = e^(-0.2theta)` | Contraction |
| 18 | Spirale de Fermat | `r = sqrt(theta)` | Ouverture lente |
| 19 | Lituus | `r = 1/sqrt(theta)` | Convergence |
| 20 | Spirale hyperbolique | `r = 1/theta` | Convergence |
| 21 | Fleur harmonique | `r = 2+cos(5theta)+0.5sin(7theta)` | Motif complexe |
| 22 | Coquille harmonique | `r = e^(0.1theta)*(1+0.3cos(6theta))` | Coquille |
| 23 | Fleur vibrante | `r = 2+cos(5theta+0.5sin(7theta))` | Ondulation |
| 24 | Étoile de mer pulsante | `r = 1+(0.2+0.2sin(t))*cos(5theta)` | Pulsation |
| 25 | Méduse animée | `r = 1+(0.2+0.15sin(t))*sin(6theta)+0.1sin(18theta)` | Pulsation |
| 26 | Lissajous rotatif | `(3sin(3t+0.3time), 2sin(2t))` | Morphing |
| 27 | Lissajous à fréquence variable | `a=3+0.5sin(time)` | Transformation |
| 28 | Superformula pulsante | `n1=0.5+0.2sin(t)` | Pulsation |
| 29 | Superformula tournante | Remplacer `theta` par `theta-0.2t` | Rotation |
| 30 | Nœud de trèfle plan | `(sin(t)+2sin(2t), cos(t)-2cos(2t))` | Courbe fermée |

---

## 17. Erreurs fréquentes

- **Courbe incomplète** : augmente le domaine de \(\theta\) ou \(t\).
- **Animation trop rapide** : réduis la vitesse du curseur ou la valeur de \(\omega\).
- **Rien ne change** : vérifie que le paramètre est réellement présent dans l’équation.
- **Courbe bizarre avec \(n\) non entier** : c’est normal ; utilise un domaine plus grand ou une valeur entière.
- **\(r^2\) refusé** : utilise la forme cartésienne ou paramétrique.
- **Cœur trop petit** : augmente les coefficients, par exemple remplace \(16\) par \(20\) et \(13\) par \(16\).

---

## 18. Parcours d’apprentissage conseillé

1. **Desmos** : trace une rose, un cœur et une spirale.
2. **Desmos** : crée des curseurs pour \(a\), \(n\) et \(\varphi\).
3. **GeoGebra** : automatise l’animation d’un paramètre.
4. **p5.js** : crée une animation web interactive.
5. **Manim** : produis une vidéo finale expliquant une équation.
6. **Python** : génère automatiquement une galerie d’images à partir de plusieurs valeurs de paramètres.

## Sources principales

- Desmos : curseurs, animation des paramètres, actions et tickers. [web:33][web:39][web:41]
- GeoGebra : animation des nombres, angles et points ; réglage de la vitesse et du mode de répétition. [web:31][web:36][web:58]
- GeoGebra : applications gratuites pour fonctions, courbes polaires, paramétriques, curseurs et 3D. [web:45][web:46][web:48][web:51][web:52]
- p5.js et p5.Polar : coordonnées polaires, conversion vers le cartésien et animations avec `frameCount`. [web:53][web:56]
- Manim Community : bibliothèque Python dédiée aux animations mathématiques et rendu de scènes. [web:32][web:34][web:35][web:37][web:44]
