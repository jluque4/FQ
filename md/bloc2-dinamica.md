# Bloc 2 — Dinàmica

# 1 — Concepte de dinàmica

> La **dinàmica** és la part de la física que estudia les causes que originen els canvis en el moviment dels cossos.

Un cos canvia el seu moviment quan canvia el **vector velocitat** (mòdul, direcció o sentit).
Aquests canvis es descriuen mitjançant l’**acceleració**:

$$
\vec a = \frac{d\vec v}{dt}
$$

La dinàmica estableix que aquests canvis són conseqüència d’**interaccions**, que s’expressen mitjançant el concepte de **força**.

$$
\text{Forces} \longrightarrow \text{Acceleració} \longrightarrow \text{Moviment}
$$

---

# 2 — Magnituds de la dinàmica

La magnitud fonamental de la dinàmica és la **força**.

---

## 2.1 — Concepte de força

> Una **força** és tota causa capaç d’alterar l’estat de moviment d’un cos o de provocar-ne una deformació.

Alterar l’estat de moviment significa canviar la velocitat del cos, és a dir, crear una acceleració.
La força és una **magnitud vectorial** i la seva unitat en el Sistema Internacional és el **newton (N)**:

$$
1 N = 1 kg \cdot m/s^2
$$

Quan sobre un cos actuen diverses forces, l’efecte global ve determinat per la **força resultant**:

$$
\vec F_{net} = \sum \vec F = \vec F_1 + \vec F_2 + \vec F_3 + \text{...} + \vec F_n
$$

| ![Força resultant](img/bloc2/1.png) |
|:--------------------------------------:|
| *Força resultant d'un sistema de forces.* |

> Per calcular la força resultant d'un sistema de forces ho podem fer mitjançant la suma vectorial o a partir de la suma de les seves components.

| ![Descomposició de forces](img/bloc2/2.png) |
|:--------------------------------------:|
| *Descomposició de forces.* |

---

# 3 — Principals tipus de forces

En els problemes de dinàmica apareixen diferents tipus de forces associades a interaccions entre cossos. Les forces més habituals són:

- pes
- força normal
- força de tensió
- força de fregament
- força elàstica

---

## 3.1 — Pes $\vec P$

El **pes** és la força amb què la Terra atrau un cos a causa de la interacció gravitatòria. Característiques:

- direcció **vertical**
- sentit **cap al centre de la Terra**
- aplicat al **centre de massa del cos**

$$
\vec P = m\vec g
$$

on

- $m$ és la massa del cos
- $\vec g$ és l’acceleració de la gravetat

| ![Força pes](img/bloc2/3.png) |
|:--------------------------------------:|
| *Força pes.* |

---

## 3.2 — Força normal $\vec N$

La **força normal** és la força que exerceix una superfície sobre un cos que està en contacte amb ella. Característiques:

- és **perpendicular** a la superfície de contacte
- apareix com a reacció al fet que el cos pressiona la superfície

En una superfície horitzontal i sense altres forces verticals:

$$
N = P
$$

| ![Força normal](img/bloc2/4.png) |
|:--------------------------------------:|
| *Força normal.* |

---

## 3.3 — Força de tensió $\vec T$

La **tensió** és la força que actua sobre un cos quan és estirat per una **corda, cable o fil**. Característiques:

- té la **direcció del fil o corda**
- sempre **estira el cos**
- apareix en sistemes de cossos units per cordes o cables

| ![Força tensió](img/bloc2/5.jpg) |
|:--------------------------------------:|
| *Força de tensió.* |

---

## 3.4 — Força de fregament $\vec F_r$

La **força de fregament** és una força de contacte que apareix entre dues superfícies i que **s’oposa al moviment relatiu** entre elles. Actua **paral·lela a la superfície de contacte**. Es poden distingir dos tipus:

> *Fregament estàtic*

Actua quan el cos **està en repòs**.

$$
F_{r} \le \mu_s \cdot N
$$

on $\mu_s$ és el **coeficient de fregament estàtic**.

> *Fregament dinàmic*

Actua quan el cos **ja està en moviment**.

$$
F_{r} = \mu_d \cdot N
$$

on $\mu_d$ és el **coeficient de fregament dinàmic**.

---

## 3.5 — Força elàstica $\vec F_e$

La **força elàstica** apareix quan un cos elàstic es deforma. Un exemple típic és una **molla**.
La relació entre la força i la deformació ve donada per la **llei de Hooke**:

$$
\vec F_e = -k \cdot \vec x
$$

on

- $k$ és la **constant elàstica**
- $x$ és la **deformació respecte a la posició d’equilibri**

El signe negatiu indica que la força és **recuperadora**, és a dir, s’oposa a la deformació.

| ![Força elàstica](img/bloc2/6.png) |
|:--------------------------------------:|
| *Força elàstica.* |

---

# 4 — Lleis de Newton

Les **lleis de Newton** descriuen la relació entre les forces que actuen sobre un cos i el seu moviment. Aquestes lleis constitueixen la base de la dinàmica clàssica.

---

## 4.1 — Principi d’inèrcia

Anomenem **inèrcia** la resistència dels cossos a canviar el seu estat de moviment.

> Si la **força resultant** que actua sobre un cos és nul·la, el cos manté el seu estat de repòs o de moviment rectilini uniforme.

$$
\sum \vec F = 0
$$

En aquestes condicions:

- el cos pot romandre **en repòs**
- o moure’s amb **velocitat constant**

Això significa que **no és necessària cap força per mantenir un moviment rectilini uniforme**.

Un exemple és un cos en repòs damunt d’una taula: el **pes** i la **força normal** tenen el mateix mòdul i sentits oposats, de manera que la força resultant és nul·la.

| ![Primera llei de Newton](img/bloc2/7.png) |
|:--------------------------------------:|
| *Cos en equilibri: la força resultant és nul·la.* |

---

## 4.2 — Principi fonamental de la dinàmica

La **segona llei de Newton** relaciona la força resultant que actua sobre un cos amb l’acceleració que experimenta.

$$
\sum \vec F = m \vec a
$$

on

- $m$ és la **massa del cos**
- $\vec a$ és l’**acceleració**

Aquesta expressió indica que:

- l’acceleració és **proporcional a la força resultant**
- l’acceleració té **la mateixa direcció i sentit que la força resultant**
- la **massa mesura la inèrcia** del cos (resistència a canviar el moviment)

A partir d’aquesta llei es defineix la unitat de força del SI:

$$
1 \text{ }N = 1 \text{ } kg \cdot m/s^2
$$

| ![Segona llei de Newton](img/bloc2/8.png) |
|:--------------------------------------:|
| *La força resultant produeix una acceleració.* |

---

## 4.3 — Principi d’acció i reacció

> Quan un cos exerceix una força sobre un altre cos, el segon cos exerceix simultàniament una força sobre el primer.

Aquestes forces tenen:

- **mateix mòdul**
- **mateixa direcció**
- **sentits oposats**

$$
\vec F_{AB} = - \vec F_{BA}
$$

Aquestes forces formen un **parell acció–reacció**.

És important remarcar que aquestes forces:

- actuen sobre **cossos diferents**
- per tant **no s’anul·len entre si**

| ![Tercera llei de Newton](img/bloc2/9.png) |
|:--------------------------------------:|
| *Parell d’acció i reacció entre dos cossos.* |

---

---

# 5 — Diagrama de forces DCL

Per resoldre problemes de dinàmica és molt útil representar totes les forces que actuen sobre un cos mitjançant un **diagrama del cos lliure (DCL)**.

Un **diagrama del cos lliure** consisteix a representar un cos aïllat i dibuixar totes les forces que actuen sobre ell.

Aquest mètode permet identificar les forces que intervenen i aplicar correctament les **lleis de Newton**.

---

> *1 — Llegir atentament l’enunciat*

Identificar:

- els cossos que intervenen
- les magnituds conegudes
- les magnituds que es volen determinar

| ![Diagrama de forces](img/bloc2/10.png) |
|:--------------------------------------:|
| *Diagrama de forces.* |

---

> *2 — Definir el sistema de referència i identificar totes les forces*

Triar un sistema d’eixos adequat:

- normalment **un eix en la direcció del moviment**
- l’altre **perpendicular**

Això simplifica el plantejament de les equacions.

Dibuixar totes les forces que actuen sobre cada cos:

| ![Diagrama del cos lliure](img/bloc2/11.png) |
|:--------------------------------------:|
| *diagrama del cos lliure.* |

---

> *3 — Descompondre les forces en components*

Si alguna força no és paral·lela als eixos escollits, cal **descompondre-la en components**.

Per exemple:

$$
F_x = F \cos\theta
$$

$$
F_y = F \sin\theta
$$

---

> *4 — Aplicar la segona llei de Newton*

Aplicar la segona llei a cada eix de coordenades i cada cos.

$$
\sum \vec{F} = m\vec{a} 
$$

Equacions per a cada cos:

* Cos 3:

$\text{Eix x: } T - F_r = m_3 a$

$\text{Eix y: } N_3 - m_3 g = 0$

* Cos 2:

$\text{Eix x: No hi ha forces}$

$\text{Eix y: } m_2 g + F_{12} - T = m_2 a$

* Cos 1:

$\text{Eix x: No hi ha forces}$

$\text{Eix y: } m_1 g - F_{12} = m_1 a$

---

> *5 — Substituir les dades i resoldre les equacions*

Introduir els valors coneguts i resoldre el sistema d’equacions per trobar les incògnites.

---

> *7 — Interpretar el resultat*

Comprovar:

- que les **unitats siguin correctes**
- que el **resultat tingui sentit físic**
- que el **sentit de les forces o acceleracions sigui coherent**

---
