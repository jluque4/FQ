# Bloc 3 — Treball i energia

# 1 — Moviment com a funció de la posició

Fins ara hem estudiat el moviment relacionant totes les magnituds amb el temps:

$$
r(t),\ v(t),\ a(t)
$$

utilitzant les lleis de Newton per determinar l’acceleració i descriure el moviment instant a instant.

En aquesta unitat introduirem un nou enfocament en què estudiarem el moviment relacionant les magnituds amb la posició i el desplaçament. Aquest canvi de formulació serà especialment útil quan la força no sigui constant i depengui de la posició:

$$
F(x)
$$

Per obtenir aquesta nova formulació partim de la segona llei de Newton $\vec F=m\vec a$ i de la definició d’acceleració $\vec a = \frac{d\vec v}{dt}$, substituint:

$$
\vec F = m\frac{d\vec v}{dt}
$$

utilitzant que $\vec v=\frac{d\vec r}{dt}$ i per tant $d\vec r = \vec v·dt$ podem escriure:

$$
\vec F \cdot d\vec r = m·\vec v·d\vec v
$$

Integrant entre una posició inicial i una final obtenim l'expressió matemàtica:

$$
\boxed{\int \vec F \cdot d\vec r = \int m·\vec v·d \vec v}
$$

> Aquesta expressió és fonamental perquè permet estudiar el moviment sense necessitat de conèixer l’evolució temporal del sistema.

# 2 — Treball mecànic

A partir de l’expressió anterior començarem estudiant el membre esquerre de la igualtat:

$$
\int \vec F \cdot d\vec r
$$

Aquesta expressió representa l’efecte acumulat d’una força al llarg d’un desplaçament i rep el nom de **treball mecànic**.

Per tant, definim el treball com:

$$
W=\int \vec F \cdot d\vec r
$$

El treball mesura la transferència d’energia produïda per una força quan actua sobre un cos mentre aquest es desplaça. Al Sistema Internacional:

$$
\boxed{1\ \text{J}=1\ \text{N·m}}
$$

La unitat del treball és el **joule (J)**.

---

> *Interpretació geomètrica del treball*

Com que el treball es calcula integrant la força respecte la posició, les gràfiques força-posició $F-x$ adquireixen una gran importància. Geomètricament:

> El treball realitzat per una força és igual a l’àrea sota la corba en una gràfica $F-x$.

---

### a) Força constant

| ![Força constant](img/bloc3/1.png) | ![Treball força constant](img/bloc3/2.png) |
|:--------------------------------------:|:--------------------------------------:|
| *Força constant aplicada a un cos.* | *Calculant l’àrea ombrejada obtenim el treball.* |

Obtenim que el treball realitzat per una **força constant** és:

$$
W = F·\Delta r·cos\alpha = \vec F · \vec \Delta r  \text{ (producte escalar del vector força i desplaçament)}
$$

---

### b) La força varia linealment amb la distància

Quan la força varia amb la posició, el treball ja no es pot calcular simplement multiplicant força per desplaçament.
En aquests casos és necessari calcular l’àrea sota la corba $F-x$, per exemple en el cas d'una molla que segueix la llei de Hooke:

| ![Força varia linealment amb la distància.](img/bloc3/3.png) | ![Treball força constant](img/bloc3/4.png) |
|:--------------------------------------:|:--------------------------------------:|
| *Força varia amb la distància segons la llei de Hooke.* | *Treball fet per la força F aplicada a la molla.* |

Obtenim que el treball realitzat per una **força** que varia **linealment amb la distància** és:

$$
|W|=\frac12 k\Delta r^2
$$

El signe final del treball dependrà del sentit de la força respecte el desplaçament.