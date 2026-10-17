# Panoplie d’équations mathématiques « artistiques »
## Guide de traçage, paramètres et variantes

Ce document répertorie des courbes célèbres que l’on peut tracer dans **Desmos**, **GeoGebra**, **Wolfram Alpha**, **Matplotlib/Python**, **MATLAB** ou tout traceur acceptant les coordonnées polaires ou paramétriques.

## 1. Comment entrer les équations

### Coordonnées polaires
Une équation polaire s’écrit \(r=f(\theta)\). Dans Desmos, taper directement :

```text
r = a*cos(n*theta)
```

ou, selon le logiciel :

```text
r = a*cos(nθ)
```

- \(\theta\) est l’angle, souvent noté `theta` ou `t`.
- \(r\) est la distance au point d’origine.
- Faire varier \(\theta\) de \(0\) à \(2\pi\), ou davantage pour les spirales.

### Coordonnées paramétriques
Une courbe paramétrique donne \(x\) et \(y\) en fonction d’un paramètre \(t\) :

\[
x=x(t),\qquad y=y(t)
\]

Dans Desmos, la syntaxe est par exemple :

```text
(16sin^3(t), 13cos(t)-5cos(2t)-2cos(3t)-cos(4t))
0 <= t <= 2pi
```

Les courbes paramétriques sont indispensables pour le cœur détaillé, le papillon de Fay et de nombreuses animations.

### Constantes à faire varier
| Constante | Rôle général |
|---|---|
| \(a\) | Taille globale de la courbe |
| \(b\) | Vitesse de croissance, décalage ou épaisseur |
| \(n\) ou \(k\) | Nombre de branches, pétales ou répétitions |
| \(t\) ou \(\theta\) | Paramètre de parcours de la courbe |
| Décalage \(\varphi\) | Rotation ou phase de la figure |

Pour animer une courbe, remplacer une constante par un curseur, par exemple `a` variant de `0.1` à `5`.

---

## 2. Le cœur

### 2.1 Cœur paramétrique classique
C’est la version la plus reconnaissable, avec une pointe nette en bas et deux lobes en haut.

\[
x=16\sin^3(t)
\]

\[
y=13\cos(t)-5\cos(2t)-2\cos(3t)-\cos(4t)
\]

**Domaine :** \(0\le t\le 2\pi\).

**Syntaxe Desmos :**

```text
(16sin^3(t), 13cos(t)-5cos(2t)-2cos(3t)-cos(4t))
0 <= t <= 2pi
```

**Paramètres modifiables :**
- Multiplier \(x\) par \(k\) pour élargir le cœur.
- Multiplier \(y\) par \(k\) pour l’allonger.
- Ajouter un décalage : \(x+h\), \(y+v\).
- Faire tourner le cœur avec une rotation :

\[
x'=x\cos(\alpha)-y\sin(\alpha)
\]

\[
y'=x\sin(\alpha)+y\cos(\alpha)
\]

### 2.2 Cœur implicite simple
\[
(x^2+y^2-1)^3-x^2y^3=0
\]

**Syntaxe Desmos :**

```text
(x^2+y^2-1)^3 - x^2*y^3 = 0
```

C’est une équation implicite : le logiciel trace l’ensemble des points \((x,y)\) qui vérifient l’égalité. Elle donne un cœur symétrique et très esthétique.

### 2.3 Cœur polaire simple
\[
r=a(1-\sin\theta)
\]

**Syntaxe :**

```text
r = a(1 - sin(theta))
0 <= theta <= 2pi
```

C’est techniquement une **cardioïde orientée vers le haut** ; elle ressemble à un cœur arrondi. Pour un vrai cœur plus fin, préférer la version paramétrique.

---

## 3. Spirale logarithmique

### Équation polaire
\[
r=ae^{b\theta}
\]

**Syntaxe Desmos :**

```text
r = a*e^(b*theta)
0 <= theta <= 12pi
```

**Paramètres :**
- \(a\) : taille initiale de la spirale.
- \(b\) : vitesse d’ouverture. Si \(b>0\), la spirale s’éloigne de l’origine ; si \(b<0\), elle s’en rapproche.
- \(\theta\) : augmenter le domaine, par exemple jusqu’à \(20\pi\), pour obtenir plusieurs tours.

**Exemples :**
- \(r=e^{0.15\theta}\) : spirale douce.
- \(r=e^{0.35\theta}\) : spirale qui s’ouvre rapidement.
- \(r=2e^{-0.2\theta}\) : spirale inversée.

La spirale logarithmique est aussi appelée spirale équiangulaire ou *spira mirabilis* ; son rayon croît exponentiellement avec l’angle. [web:14][web:4]

### Forme paramétrique
\[
x=ae^{b\theta}\cos\theta
\]

\[
y=ae^{b\theta}\sin\theta
\]

**Syntaxe :**

```text
(a*e^(b*t)*cos(t), a*e^(b*t)*sin(t))
0 <= t <= 12pi
```

---

## 4. Papillon de Clifford / papillon de Fay

La courbe souvent appelée « papillon de Clifford » est plus précisément le **papillon transcendant de Temple H. Fay**, publié en 1989. [web:18][web:26]

### Équation polaire
\[
r=e^{\sin\theta}-2\cos(4\theta)+\sin^5\left(\frac{2\theta-\pi}{24}\right)
\]

**Syntaxe Desmos :**

```text
r = e^(sin(theta)) - 2cos(4theta) + sin((2theta-pi)/24)^5
0 <= theta <= 12pi
```

**Paramètres importants :**
- Le terme \(e^{\sin\theta}\) crée le corps et les ailes principales.
- \(-2\cos(4\theta)\) crée les ondulations internes.
- \(\sin^5\left(\frac{2\theta-\pi}{24}\right)\) ajoute l’asymétrie délicate des ailes.
- Le domaine doit aller jusqu’à \(12\pi\), sinon le papillon reste incomplet. [web:18]

### Équation paramétrique
\[
x=\sin t\left(e^{\cos t}-2\cos(4t)-\sin^5\left(\frac{t}{12}\right)\right)
\]

\[
y=\cos t\left(e^{\cos t}-2\cos(4t)-\sin^5\left(\frac{t}{12}\right)\right)
\]

**Domaine :** \(0\le t\le 12\pi\). [web:18]

**Syntaxe Desmos :**

```text
(sin(t)*(e^(cos(t))-2cos(4t)-sin(t/12)^5),
 cos(t)*(e^(cos(t))-2cos(4t)-sin(t/12)^5))
0 <= t <= 12pi
```

---

## 5. Rose de Rhodonea

La rose de Rhodonea, ou courbe rose de Grandi, a pour équation générale :

\[
r=a\cos(n\theta)
\]

ou

\[
r=a\sin(n\theta)
\]

**Syntaxe Desmos :**

```text
r = a*cos(n*theta)
0 <= theta <= 2pi
```

**Règle des pétales :**
- Si \(n\) est **impair** : la rose possède \(n\) pétales.
- Si \(n\) est **pair** : la rose possède \(2n\) pétales.
- Si \(n\) est rationnel \(p/q\), le nombre de pétales dépend de la parité de \(p\) et \(q\). [web:17][web:21][web:23]

| Valeur de \(n\) | Équation | Nombre de pétales |
|---:|---|---:|
| 2 | \(r=a\cos(2\theta)\) | 4 |
| 3 | \(r=a\cos(3\theta)\) | 3 |
| 4 | \(r=a\cos(4\theta)\) | 8 |
| 5 | \(r=a\cos(5\theta)\) | 5 |
| 7 | \(r=a\sin(7\theta)\) | 7 |

**Variantes à essayer :**
- \(r=3\cos(5\theta)\) : rose à cinq pétales.
- \(r=3\cos(4\theta)\) : fleur à huit pétales.
- \(r=3\cos(2.5\theta)\) : rose à pétales entrelacés ; augmenter le domaine de \(\theta\).
- \(r=3\cos(5\theta)+1\) : décale la courbe et produit une forme florale moins régulière.

---

## 6. Lemniscate de Bernoulli

La lemniscate de Bernoulli a la forme d’un \(8\) horizontal ou d’un symbole \(\infty\).

### Équation polaire
\[
r^2=a^2\cos(2\theta)
\]

**Syntaxe Desmos :**

```text
r^2 = a^2*cos(2theta)
-pi/4 <= theta <= pi/4
```

Certains traceurs n’acceptent pas \(r^2\). Utiliser alors la forme paramétrique.

### Équation cartésienne
\[
(x^2+y^2)^2=a^2(x^2-y^2)
\]

**Syntaxe Desmos :**

```text
(x^2+y^2)^2 = a^2*(x^2-y^2)
```

Cette forme est la plus fiable dans la plupart des logiciels. [web:13][web:12]

### Forme paramétrique
\[
x=\frac{a\sqrt{2}\cos t}{1+\sin^2 t}
\]

\[
y=\frac{a\sqrt{2}\cos t\sin t}{1+\sin^2 t}
\]

**Domaine :** \(0\le t\le 2\pi\).

**Paramètre :**
- \(a\) contrôle la largeur totale de la lemniscate.
- Remplacer \(\cos(2\theta)\) par \(\sin(2\theta)\) fait tourner la figure de \(45^\circ\).

---

## 7. Cardioïde

### Équation polaire
\[
r=a(1+\cos\theta)
\]

**Syntaxe :**

```text
r = a(1 + cos(theta))
0 <= theta <= 2pi
```

**Variantes :**
- \(r=a(1-\cos\theta)\) : cardioïde orientée vers la gauche.
- \(r=a(1+\sin\theta)\) : cardioïde orientée vers le haut.
- \(r=a(1-\sin\theta)\) : cardioïde orientée vers le bas, souvent utilisée comme cœur arrondi. [web:30]

### Équation paramétrique
\[
x=a(1+\cos t)\cos t
\]

\[
y=a(1+\cos t)\sin t
\]

**Domaine :** \(0\le t\le 2\pi\).

---

## 8. Astroïde

L’astroïde est une courbe en forme d’étoile à quatre branches, comme un diamant aux côtés concaves.

### Équation implicite
\[
x^{2/3}+y^{2/3}=a^{2/3}
\]

**Syntaxe Desmos :**

```text
x^(2/3) + y^(2/3) = a^(2/3)
```

### Équation paramétrique
\[
x=a\cos^3 t
\]

\[
y=a\sin^3 t
\]

**Domaine :** \(0\le t\le 2\pi\).

**Syntaxe :**

```text
(a*cos(t)^3, a*sin(t)^3)
0 <= t <= 2pi
```

---

## 9. Deltoïde

La deltoïde ressemble à un triangle aux côtés incurvés vers l’intérieur.

### Équation paramétrique
\[
x=2a\cos t+a\cos(2t)
\]

\[
y=2a\sin t-a\sin(2t)
\]

**Domaine :** \(0\le t\le 2\pi\).

**Syntaxe :**

```text
(2a*cos(t)+a*cos(2t), 2a*sin(t)-a*sin(2t))
0 <= t <= 2pi
```

---

## 10. Épicycloïde et hypocycloïde

Ce sont des courbes obtenues par le roulement d’un cercle sur un autre cercle.

### Épicycloïde
Un cercle de rayon \(r\) roule à l’extérieur d’un cercle de rayon \(R\) :

\[
x=(R+r)\cos t-r\cos\left(\frac{R+r}{r}t\right)
\]

\[
y=(R+r)\sin t-r\sin\left(\frac{R+r}{r}t\right)
\]

### Hypocycloïde
Le cercle roule à l’intérieur :

\[
x=(R-r)\cos t+r\cos\left(\frac{R-r}{r}t\right)
\]

\[
y=(R-r)\sin t-r\sin\left(\frac{R-r}{r}t\right)
\]

**Paramètres clés :**
- \(R\) : rayon du cercle fixe.
- \(r\) : rayon du cercle roulant.
- Le rapport \(R/r\) détermine le nombre de pointes.

**Exemples :**
- \(R=5\), \(r=1\) : hypocycloïde à 5 pointes.
- \(R=4\), \(r=1\) : astroïde.
- \(R=3\), \(r=1\) : deltoïde.

---

## 11. Courbes de Lissajous

Les courbes de Lissajous sont très intéressantes pour créer des motifs oscillants, des nœuds visuels et des animations.

\[
x=A\sin(at+\varphi)
\]

\[
y=B\sin(bt)
\]

**Syntaxe :**

```text
(A*sin(a*t+phi), B*sin(b*t))
0 <= t <= 2pi
```

**Paramètres :**
- \(A\), \(B\) : largeur et hauteur.
- \(a\), \(b\) : fréquences horizontale et verticale.
- \(\varphi\) : déphasage ; il change la forme sans changer les fréquences.

**Exemples :**
- \(a=3\), \(b=2\), \(\varphi=\pi/2\) : nœud élégant.
- \(a=5\), \(b=4\), \(\varphi=0\) : motif complexe.
- \(a=b\), \(\varphi=\pi/2\) : cercle ou ellipse.

---

## 12. Spirale d’Archimède

### Équation polaire
\[
r=a+b\theta
\]

**Syntaxe :**

```text
r = a + b*theta
0 <= theta <= 10pi
```

**Paramètres :**
- \(a\) : point de départ.
- \(b\) : espacement entre les spires.
- Plus \(b\) est grand, plus la spirale s’écarte vite.

Contrairement à la spirale logarithmique, l’écartement entre deux tours est constant. [web:15]

---

## 13. Spirale de Fermat

### Équation polaire
\[
r^2=a^2\theta
\]

ou :

\[
r=a\sqrt{\theta}
\]

**Syntaxe :**

```text
r = a*sqrt(theta)
0 <= theta <= 12pi
```

Elle s’ouvre plus lentement que la spirale d’Archimède et produit un motif très régulier.

---

## 14. Lituus

### Équation polaire
\[
r^2\theta=a^2
\]

ou :

\[
r=\frac{a}{\sqrt{\theta}}
\]

**Syntaxe :**

```text
r = a/sqrt(theta)
theta > 0
0 < theta <= 12pi
```

C’est une spirale qui se rapproche progressivement de l’origine.

---

## 15. Folium de Descartes

### Équation implicite
\[
x^3+y^3-3axy=0
\]

**Syntaxe :**

```text
x^3 + y^3 - 3a*x*y = 0
```

### Équation paramétrique
\[
x=\frac{3at}{1+t^3}
\]

\[
y=\frac{3at^2}{1+t^3}
\]

**Domaine conseillé :** \(-20\le t\le 20\), en évitant \(t=-1\).

---

## 16. Courbe du papillon algébrique

À ne pas confondre avec le papillon de Fay. Cette courbe sextique a pour équation implicite :

\[
y^6=x^2-x^6
\]

**Syntaxe Desmos :**

```text
y^6 = x^2 - x^6
```

Elle donne un papillon plus géométrique et symétrique, différent du papillon transcendant de Fay. [web:2]

---

## 17. Néphroïde

### Équation polaire
\[
r=a(1+2\cos\theta)
\]

**Syntaxe :**

```text
r = a(1 + 2cos(theta))
0 <= theta <= 2pi
```

Elle ressemble à un rein ou à une fève.

---

## 18. Courbe du limaçon

### Équation polaire
\[
r=a+b\cos\theta
\]

**Syntaxe :**

```text
r = a + b*cos(theta)
0 <= theta <= 2pi
```

**Cas importants :**
- \(a=b\) : cardioïde.
- \(a<b\) : limaçon avec boucle interne.
- \(a>b\) : limaçon sans boucle interne.
- Remplacer \(\cos\) par \(\sin\) fait pivoter la courbe.

---

## 19. Courbes superformula : famille très puissante

La **superformula** de Johan Gielis permet de générer une immense variété de formes : fleurs, étoiles, feuilles, coquillages, polygons arrondis, etc.

\[
r(\theta)=\left(\left|\frac{\cos\left(\frac{m\theta}{4}\right)}{a}\right|^{n_2}
+\left|\frac{\sin\left(\frac{m\theta}{4}\right)}{b}\right|^{n_3}\right)^{-1/n_1}
\]

**Syntaxe Desmos :**

```text
r = ((abs(cos(m*theta/4)/a)^(n2) + abs(sin(m*theta/4)/b)^(n3))^(-1/n1))
0 <= theta <= 2pi
```

**Paramètres :**
- \(m\) : nombre de branches ou de pétales.
- \(a\), \(b\) : symétrie horizontale et verticale.
- \(n_1\) : arrondi ou pincement global.
- \(n_2\), \(n_3\) : forme des branches.

**Exemples :**
- \(m=5\), \(a=b=1\), \(n_1=0.3\), \(n_2=n_3=0.3\) : étoile à cinq branches.
- \(m=6\), \(n_1=1\), \(n_2=n_3=1\) : forme hexagonale arrondie.
- \(m=8\), \(n_1=0.5\), \(n_2=n_3=0.5\) : fleur complexe.

C’est probablement la meilleure famille d’équations si tu veux créer une **galerie générative** avec des curseurs.

---

## 20. Courbes de Maurey / courbes harmoniques

Une généralisation intéressante des roses :

\[
r=a+b\cos(n\theta)
\]

**Syntaxe :**

```text
r = a + b*cos(n*theta)
0 <= theta <= 2pi
```

**Exemples :**
- \(a=1\), \(b=2\), \(n=5\) : fleur asymétrique.
- \(a=2\), \(b=1\), \(n=7\) : motif floral régulier.
- \(a=0\), \(b=3\), \(n=4\) : rose classique à huit pétales.

---

## 21. Courbe du trèfle à quatre feuilles

### Équation polaire
\[
r=a\sin(2\theta)
\]

**Syntaxe :**

```text
r = a*sin(2theta)
0 <= theta <= 2pi
```

C’est un cas particulier de la rose de Rhodonea avec \(n=2\), donnant quatre feuilles.

---

## 22. Courbe du trèfle à trois feuilles

### Équation polaire
\[
r=a\sin(3\theta)
\]

**Syntaxe :**

```text
r = a*sin(3theta)
0 <= theta <= 2pi
```

Elle donne trois pétales.

---

## 23. Courbe de la coquille de Nautilus

Une variante naturelle de la spirale logarithmique :

\[
r=e^{0.18\theta}
\]

**Syntaxe :**

```text
r = e^(0.18*theta)
0 <= theta <= 16pi
```

Pour un effet coquille, ajouter une modulation :

\[
r=e^{0.18\theta}(1+0.15\cos(8\theta))
\]

**Syntaxe :**

```text
r = e^(0.18*theta)*(1+0.15cos(8theta))
0 <= theta <= 16pi
```

---

## 24. Courbe de l’étoile de mer

### Équation polaire
\[
r=1+0.5\cos(5\theta)
\]

**Syntaxe :**

```text
r = 1 + 0.5cos(5theta)
0 <= theta <= 2pi
```

**Paramètres :**
- Remplacer \(5\) par \(6\), \(7\) ou \(8\) pour changer le nombre de bras.
- Augmenter \(0.5\) pour des bras plus saillants.

---

## 25. Courbe de la fleur de vie simplifiée

On peut obtenir un motif floral en superposant plusieurs cercles :

```text
x^2+y^2=1
(x-1)^2+y^2=1
(x+1)^2+y^2=1
x^2+(y-1)^2=1
x^2+(y+1)^2=1
```

Ce n’est pas une seule équation, mais une composition de courbes. C’est très utile pour créer des motifs géométriques.

---

## 26. Tableau récapitulatif

| Nom | Type | Équation principale | Paramètre clé | Effet visuel |
|---|---|---|---|---|
| Cœur paramétrique | Paramétrique | \(x=16\sin^3t\), \(y=13\cos t-5\cos2t-2\cos3t-\cos4t\) | \(t\in[0,2\pi]\) | Cœur détaillé |
| Cœur implicite | Implicite | \((x^2+y^2-1)^3=x^2y^3\) | Aucun curseur nécessaire | Cœur symétrique |
| Spirale logarithmique | Polaire | \(r=ae^{b\theta}\) | \(b\) | Spirale naturelle |
| Papillon de Fay | Polaire/paramétrique | \(r=e^{\sin\theta}-2\cos4\theta+\sin^5\left(\frac{2\theta-\pi}{24}\right)\) | Domaine \(12\pi\) | Papillon |
| Rose de Rhodonea | Polaire | \(r=a\cos(n\theta)\) | \(n\) | Fleur à pétales |
| Lemniscate de Bernoulli | Polaire/implicite | \(r^2=a^2\cos2\theta\) | \(a\) | Symbole infini |
| Cardioïde | Polaire | \(r=a(1+\cos\theta)\) | \(a\) | Cœur arrondi |
| Astroïde | Paramétrique | \(x=a\cos^3t\), \(y=a\sin^3t\) | \(a\) | Étoile à 4 branches |
| Deltoïde | Paramétrique | \(x=2a\cos t+a\cos2t\) | \(a\) | Triangle incurvé |
| Lissajous | Paramétrique | \(x=A\sin(at+\varphi)\), \(y=B\sin(bt)\) | \(a,b,\varphi\) | Nœuds et oscillations |
| Spirale d’Archimède | Polaire | \(r=a+b\theta\) | \(b\) | Spirale régulière |
| Superformula | Polaire | Voir section 19 | \(m,n_1,n_2,n_3\) | Fleurs, étoiles, feuilles |

---

## 27. Méthode pratique pour explorer

1. **Commencer par la forme polaire simple** : \(r=a\cos(n\theta)\).
2. **Ajouter un curseur** pour \(a\) et \(n\).
3. **Modifier le domaine** de \(\theta\) : \(2\pi\), \(4\pi\), \(12\pi\).
4. **Ajouter un terme correcteur** : \(r=a\cos(n\theta)+b\).
5. **Remplacer \(\cos\) par \(\sin\)** pour faire tourner la figure.
6. **Multiplier par une enveloppe**, par exemple \(e^{k\theta}\), pour transformer une fleur en spirale fleurie.
7. **Ajouter un déphasage** : \(\cos(n(\theta-\varphi))\).
8. **Superposer plusieurs courbes** avec des couleurs différentes.

### Exemple de transformation
Partir d’une rose :

\[
r=\cos(5\theta)
\]

Ajouter une croissance exponentielle :

\[
r=e^{0.08\theta}\cos(5\theta)
\]

**Syntaxe :**

```text
r = e^(0.08*theta)*cos(5theta)
0 <= theta <= 8pi
```

On obtient une **rose spirale** : les pétales tournent et s’agrandissent progressivement.

---

## 28. Bibliothèque de variantes à tester

| Courbe | Équation à saisir | Domaine conseillé |
|---|---|---|
| Rose à 5 pétales | `r = 3cos(5theta)` | \(0\le\theta\le2\pi\) |
| Rose à 8 pétales | `r = 3cos(4theta)` | \(0\le\theta\le2\pi\) |
| Cœur arrondi | `r = 2(1-sin(theta))` | \(0\le\theta\le2\pi\) |
| Spirale logarithmique | `r = e^(0.2theta)` | \(0\le\theta\le12\pi\) |
| Spirale inversée | `r = e^(-0.2theta)` | \(0\le\theta\le12\pi\) |
| Papillon de Fay | `r = e^(sin(theta))-2cos(4theta)+sin((2theta-pi)/24)^5` | \(0\le\theta\le12\pi\) |
| Lemniscate | `(x^2+y^2)^2 = 4(x^2-y^2)` | Fenêtre \([-3,3]\times[-2,2]\) |
| Astroïde | `(4cos(t)^3, 4sin(t)^3)` | \(0\le t\le2\pi\) |
| Lissajous | `(3sin(3t+pi/2), 2sin(2t))` | \(0\le t\le2\pi\) |
| Fleur modulée | `r = 2 + cos(6theta)` | \(0\le\theta\le2\pi\) |
| Rose spirale | `r = e^(0.08theta)cos(5theta)` | \(0\le\theta\le8\pi\) |

---

## 29. Conseils pour un projet visuel ou génératif

- Utilise \(n\) entier pour des fleurs régulières.
- Utilise \(n\) rationnel pour des motifs qui se recoupent.
- Utilise \(b\) petit dans \(e^{b\theta}\) pour une spirale élégante.
- Ajoute un terme \(+c\) à \(r\) pour déformer une rose en coquillage.
- Utilise \(|\cos|\) et \(|\sin|\) dans la superformula pour créer des pointes.
- Pour une animation, fais varier \(n\), \(b\), \(\varphi\) ou le domaine de \(t\).
- Pour une identité visuelle, combine une courbe principale et une courbe secondaire en transparence.

## Sources principales

- Wolfram MathWorld : spirale logarithmique, rose de Rhodonea, lemniscate de Bernoulli. [web:14][web:21][web:13]
- Britannica : définition et équation générale de la spirale logarithmique. [web:4]
- Plus Maths et Cerritos College : règle du nombre de pétales des roses. [web:17][web:16]
- Wikipédia et sources spécialisées : papillon transcendant de Temple Fay. [web:18][web:26]
- Mathwords : équations du cœur, y compris la forme paramétrique classique. [web:30]
- Desmos : syntaxe des équations paramétriques. [web:1]
