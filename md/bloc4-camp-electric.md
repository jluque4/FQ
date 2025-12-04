# Bloc 4. Camp elèctric

---

# 1 — Càrrega elèctrica Q

---

## 1.1 — Origen de la càrrega elèctrica 

La matèria està formada per àtoms, constituïts per:
- **protons** (+)
- **electrons** (−)
- **neutrons** (0)

En un àtom neutre hi ha el mateix nombre de protons que d’electrons.<br>
En determinades situacions es produeix un **intercanvi d’electrons**:  
- si un cos **perd electrons**, queda **carregat positivament** formant un iò positiu o **catió**
- si un cos **guanya electrons**, queda **carregat negativament** formant un iò negatiu o **anió**

|        ![Àtoms, iò, aniò i catiò](img/bloc4/27.png)   |
| :---------------------------------------------------: |
| *Àtoms, ions, anions i cations.* |

> Només els **electrons** es mouen; els protons continuen al nucli. <br>
> Les càrregues **iguals es repel·leixen** i les **oposades s’atreuen**.

|        ![Atracció i repulsió de càrregues elèctriques](img/bloc4/26.jpeg)   |
| :---------------------------------------------------: |
| *Atracció i repulsió de càrregues elèctriques.* |

---

## 1.2 — Quantització i conservació de la càrrega

La càrrega elèctrica és:
- **quantitzada**:  
$q = n\cdot e$ amb $e = 1{.}602\times10^{-19}$ C

- **conservada**:  
  en qualsevol procés, la càrrega total **no canvia**, només es transfereix.

La unitat de càrrega del SI és el **coulomb (C)**.
> El **coulomb** es defineix com la **quantitat de càrrega elèctrica** total que passa per una **secció transversal d'un conductor** pel qual circula un corrent elèctric **d'un ampere** durant **un segon**. 

> 1 C equival a la càrrega de $6.24\times 10^{18}$ electrons.

Una **càrrega puntual** és una càrrega concentrada en un punt o en un cos molt petit comparat amb la distància del problema.

---

## 1.3 — Materials conductors i aïllants.

Segons la mobilitat dels electrons:

- **Conductors**  
  Tenen electrons lliures → la càrrega es reparteix fàcilment.  
  *Exemples: metalls.*

- **Aïllants**  
  Electrons fortament lligats → la càrrega queda localitzada.  
  *Exemples: vidre, plàstic.*

Tot i que un mol d’un metall conté molts electrons disponibles, en la pràctica els cossos **no poden carregar-se tant**: abans es descarreguen a l’aire (ruptura dielèctrica).

---

---

# 2 — Força electrostàtica: llei de Coulomb

## 2.1 — Interacció entre càrregues: atracció i repulsió

Les **càrregues elèctriques** interactuen entre elles mitjançant una força:

- **Del mateix signe** → es **repel·leixen**.
- **De signe oposat** → s’**atrauen**.

Aquesta força actua al llarg de la recta que uneix les dues càrregues i és un exemple de **força a distància**, igual que la gravetat, però pot ser **atractiva o repulsiva**.

---

## 2.2 — Llei de Coulomb

Per dues **càrregues puntuals** $q_1$ i $q_2$ separades una distància $r$, la **força electrostàtica** ve donada per la **llei de Coulomb**:

$$
\vec F = k \cdot \frac{q_1 q_2}{r^2}\cdot \hat u_r
$$

on:

- $k$ és la **constant elèctrica**.
- $r$ és la distància entre les càrregues.
- $\hat u_r$ és el vector unitari en la direcció que uneix les dues càrregues.

- **Mòdul de la força:**

$$
F = k \cdot \frac{|q_1 q_2|}{r^2}
$$

- **Direcció:** la recta que uneix les dues càrregues.  
- **Sentit:**  
  - si $q_1$ i $q_2$ tenen **el mateix signe**, la força és **repulsiva**;  
  - si tenen **signe oposat**, és **atractiva**.

Les unitats garanteixen que la força es mesura en **newtons (N)** quan les càrregues estan en **coulombs (C)** i la distància en **metres (m)**. 

---

## 2.3 — Influència del medi: permitivitat relativa

L’intensitat de la força depèn també del **medi** on es troben les càrregues, mitjançant la **permitivitat del medi** $\varepsilon$:

$$
F = \frac{1}{4\pi\varepsilon}\cdot \frac{|q_1 q_2|}{r^2}
$$

Definim la **permitivitat relativa** d’un medi determinat $\varepsilon_r$, com la relació entre la permitivitat del medi i la del buit:
$$
\varepsilon_r = \frac{\varepsilon}{\varepsilon_0}
$$ 

Això explica, per exemple, que les interaccions electrostàtiques entre ions siguin molt menys intenses en **aigua** que en el buit.

---

## 2.4 — Comparació amb la llei de gravitació universal

La llei de Coulomb és **formalment molt similar** a la llei de Newton:

$$
F_g = G\cdot \frac{m_1 m_2}{r^2}
\qquad\text{vs}\qquad
F_e = k\cdot \frac{q_1 q_2}{r^2}
$$

| Aspecte              | Gravitació                          | Electrostàtica                          |
|----------------------|-------------------------------------|-----------------------------------------|
| Magnitud d’origen    | massa $m$                         | càrrega $q$                           |
| Tipus de força       | sempre **atractiva**                | **atractiva o repulsiva**               |
| Constant             | $G$                               | $k = 1/(4\pi\varepsilon_0)$           |
| Dependència amb $r$| $\propto 1/r^2$                   | $\propto 1/r^2$                       |
| Medi                 | no depèn del medi                   | depèn de la **permitivitat** $\varepsilon_r$ |

---

## 2.5 — Principi de superposició de forces electrostàtiques

Quan un punt del espai està sotmès a la influència de **més d’una càrrega elèctrica**, la força total és la **suma vectorial** de totes les forces exercides per cadascuna de les càrregues:

$$
\vec F_{\text{total}} = \sum_i \vec F_i
$$

Això és possible perquè la força electrostàtica és una força **lineal** i **conservativa**, igual que la gravitació. Per tant, podem calcular cada força individual amb la **llei de Coulomb** i fer-ne la suma vectorial final.

| ![Superposició de forces electrostàtiques](img/bloc4/28.png) |
|:-------------------------------------------------------------:|
| *La força total és la suma vectorial de totes les forces individuals.* |

---

#### Exemple:

- Si un punt està situat entre dues càrregues **iguals i del mateix signe**, les forces tenen direcció oposada i el **punt mig** és on es compensen (força total = 0).
- Si les càrregues tenen **signe oposat**, les dues forces tenen el **mateix sentit** i el punt de força zero queda més a prop de la càrrega de menor mòdul.

Aquesta idea serà essencial per resoldre problemes típics de PAU sobre:
- punts on la força és nul·la,
- punts on el **camp elèctric** és nul,
- interaccions entre **sistemes de diverses càrregues**.

---

Perfecte — podem reformular **tot l'apartat del camp elèctric** evitant la idea de “càrrega de prova”, que ja no és l’enfocament modern recomanat, i substituint-la per la definició fonamental:

> **El camp elèctric és la força elèctrica per unitat de càrrega.**

A continuació tens l’apartat **3 — Camp elèctric** revisat i ajustat a aquest enfocament.

---

# 3 — Camp elèctric

## 3.1 — Definició

El camp elèctric és el camp de forces que una càrrega crea al seu voltant i que actua sobre altres càrregues.
En un punt de l’espai, la intensitat del camp elèctric és la **força per unitat de càrrega**:

$$
\vec{E} = \frac{\vec{F}}{q}
$$

on:

* $\vec{F}$ és la **força elèctrica** que experimentaria qualsevol càrrega situada en aquell punt,
* $q$ és el **valor de la càrrega** sobre la qual actua la força.

---

## 3.2 — Camp elèctric creat per una càrrega puntual

La força entre dues càrregues ve donada per la **llei de Coulomb**:

$$
\vec{F} = k \cdot \frac{Q\cdot q}{r^2} \cdot \hat u_r
$$

Si dividim entre la càrrega $q$ que rep la força, obtenim el camp creat per **Q**:

$$
\vec{E} = k\cdot \frac{Q}{r^{2}} \cdot \hat u_r
$$

Característiques:

* Si **Q > 0**, les línies de camp **surten** de la càrrega.
* Si **Q < 0**, les línies de camp **entren** cap a la càrrega.
* Igual que la gravetat, el camp disminueix amb la distància com $1/r^{2}$.

| ![Disminució de E amb la distància](img/bloc4/34.png) |
|:--------------------------------------:|
| *Disminució de $\vec{E}$ amb la distància.* |

---

## 3.3 — Línies de camp elèctric

Les línies de camp són una representació visual del camp elèctric.
En qualsevol punt:

* La **tangent** a la línia indica la direcció de $\vec{E}$.
* La **densitat de línies** mostra la intensitat del camp.
* Surten de càrregues **positives**, entren en **negatives**.
* No es tallen mai entre si.

Configuracions importants:

* **Una sola càrrega** → línies radials.

| ![Representació del camp elèctric](img/bloc4/29.png) | ![Representació del camp elèctric](img/bloc4/30.png) |
|:--------------------------------------:|:--------------------------------------:|
| *Línies de camp elèctric d’una càrrega puntual positiva +Q.* | *Línies de camp elèctric d’una càrrega puntual negativa −Q.* |

* **Dues càrregues iguals** → repulsió i zona simètrica sense línies.

| ![Representació del camp elèctric](img/bloc4/31.png) | 
|:--------------------------------------:|
| *Línies de camp elèctric creat per dues càrregues puntuals iguals.* |

* **Dipol** ($+Q$ i $–Q$) → línies corbades que connecten les dues càrregues.

El camp elèctric per a dues càrregues de signe contrari però d’igual valor absolut és l’indicat en la figura, on s’observa que les línies es tanquen, ja que hi ha atracció entre les càrregues.

> En aquest últim cas, tenim un dipol, és a dir, dues càrregues d’igual valor absolut però de signe contrari separades una distància relativament petita.

| ![Representació del camp elèctric](img/bloc4/32.png) | 
|:--------------------------------------:|
| *Línies de camp creades per un dipol elèctric.* |

---

## 3.4 — Camp elèctric uniforme

Es produeix en un **condensador pla** ideal amb una placa carregada positivament i l’altra negativament però el mateix valor absolut.

Propietats:

* El camp és **constant** en mòdul i direcció.
* El sentit és **de la placa positiva cap a la negativa**.
* Les línies de camp són paral·leles i equidistants.
* Serveix per estudiar moviments rectilinis de càrregues sota una força constant.

Per qualsevol càrrega $q$ dins del camp:

$$
\vec{F} = q\cdot \vec{E}
$$

| ![Representació del camp elèctric uniforme d’un condensador](img/bloc4/33.png) | 
|:--------------------------------------:|
| *Camp elèctric uniforme d’un condensador.* |

---

## 3.5 — Camp creat per un sistema de càrregues

Quan diverses càrregues creen camp en el mateix punt, el camp total és la **suma vectorial** dels camps individuals:

$$
\vec{E}_{\text{total}} = \sum_i \vec{E}_i
$$

Això permet:

* Calcular el camp en configuracions amb moltes càrregues.
* Determinar punts on el camp es fa **zero**.
* Analitzar dipols, quadrupols i geometries simètriques.

**Exemple conceptual:**
Dues càrregues positives iguals generen un punt al mig on:

$$
\vec{E}_1 + \vec{E}_2 = 0
$$

perquè els vectors són iguals i oposats.

---
