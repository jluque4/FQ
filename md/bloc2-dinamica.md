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