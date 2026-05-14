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

### b) La força varia linealment amb la posició

Quan la força varia amb la posició, el treball ja no es pot calcular simplement multiplicant força per desplaçament.
En aquests casos és necessari calcular l’àrea sota la corba $F-x$, per exemple en el cas d'una molla que segueix la llei de Hooke:

| ![Força varia linealment amb la distància.](img/bloc3/3.png) | ![Treball força constant](img/bloc3/4.png) |
|:--------------------------------------:|:--------------------------------------:|
| *Força varia amb la posició segons la llei de Hooke.* | *Treball fet per la força F aplicada a la molla.* |

Obtenim que el treball realitzat per una **força** que varia **linealment amb la posició** és:

$$
|W|=\frac12·k·\Delta r^2
$$

El signe final del treball dependrà del sentit de la força respecte el desplaçament.

---

### c) Força variable

És el cas més general. També calculem el treball amb l’àrea ombrejada fent el mateix raonament anterior.

| ![Força variable.](img/bloc3/5.png) |
|:--------------------------------------:|
| *Calculem l’àrea total ombrejada i obtenim el treball total.* |

---

# 3 — Energia

L’energia és una magnitud associada a la capacitat d’un sistema per produir canvis o transformacions.

Al llarg d’un procés físic, l’energia pot:
- transferir-se entre cossos,
- transformar-se d’un tipus a un altre,
- o conservar-se dins del sistema.

> En física, l’energia és la capacitat que té un cos per realitzar treball.

### a) Energia cinètica

En l’apartat anterior hem definit el treball mecànic com la transferència d’energia produïda per una força al llarg d’un desplaçament. Ara estudiarem el membre dret de l’expressió obtinguda a partir de la segona llei de Newton:

$$
\int m·\vec v · d\vec v
$$

i integrant entre una velocitat inicial i una final per una massa constant:

$$
m\int_{v_i}^{v_f} v·dv = m\left[\frac12 v^2\right]_{v_i}^{v_f}
$$

obtenim:

$$
\frac12 mv_f^2-\frac12 mv_i^2
$$

Aquesta expressió suggereix definir una nova magnitud física anomenada **energia cinètica**:

$$
\boxed{
E_c=\frac12 mv^2
}
$$

> L’energia cinètica representa l’energia associada al moviment d’un cos.

Per tant, el membre dret de la igualtat es pot escriure com:

$$
\Delta E_c = E_{c_f}-E_{c_i}
$$

i obtenim finalment el **principi del treball i l’energia cinètica**:

$$
\boxed{W=\Delta E_c}
$$

> El treball total realitzat sobre un cos és igual a la variació de la seva energia cinètica.

### b) Forces conservatives

> Es diu que una força és conservativa qual el treball que realitza per desplaçar un cos d'un punt A a un punt B npmés depèn de les posicions inicial i final i no del cami seguit.

Són forces conservatives: el pes, la força electrostàtica i la força elàstica. La força de fregament és una força no conservativa.

| ![Força conservativa.](img/bloc3/6.png) | 
|:--------------------------------------:|
| *Treballs efectuats per la força aplicada en diferents re­correguts.* |

Les forces conservatives permeten definir una nova forma d’energia associada a la posició del sistema anomenada **energia potencial**.

### c) Energia potencial

> És l’energia que té un cos per la seva posició en una zona de l’espai on actuen forces conservatives.

| ![Energia potencial.](img/bloc3/7.png) | 
|:--------------------------------------:|
| *Variació de l'energia potencial associada al pes d'un cos.* |

Definim la variació de l’energia potencial d’una partícula com el treball, can­viat de signe, realitzat per una força conservativa sobre la par­tícula; aquest treball és igual a la disminució d’energia potencial que experimenta la partícula.

$$
W = −ΔE_p
$$

> *Energia potencial gravitatòria*

L’energia potencial gravitatòria és l’energia que té un cos per la posició que ocupa dins d’una zona de l’espai on actuïn forces gravitatòries.

| ![Energia potencial gravitatòria.](img/bloc3/8.png) | 
|:--------------------------------------:|
| *Energia potencial gravitatòria.* |

$$
W_p = \vec F · \Delta \vec y = m·g·h_A - m·g·H_b = −(Ep_B − Ep_A) = -\Delta E_p
$$

En general, l’energia potencial gravitatòria d’un cos de massa m situat a una altura h val:

$$
\boxed{E_p = m·g·h}
$$

> *Energia potencial elàstica*

L’energia potencial elàstica és l’energia que té un cos elàstic en virtut del seu estat de deformació.

| ![Energia potencial elàstica.](img/bloc3/9.png) | 
|:--------------------------------------:|
| *Deformació de la molla en aplicar una força externa.* |

$$
W_{molla} = \int \vec F · \Delta \vec x = \frac12·k·x_A^2 - \frac12·k·x_B^2 = −(Ep_B − Ep_A) = -\Delta E_p
$$

En general, l’energia potencial elàstica d’un cos de massa m i constant k és:

$$
\boxed{E_p = \frac12·k·x^2}
$$