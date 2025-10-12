# **CG1 — Concepte de camp físic**

---

## **1.1 — Què és un camp físic**

En molts fenòmens naturals, un cos pot **influir en un altre sense contacte directe**.  
Per explicar-ho, introduïm el **concepte de camp físic**.

> En una regió de l’espai hi ha un **camp físic** quan a cada punt d’aquesta regió hi està definida una determinada **magnitud física**.

Aquesta magnitud pot ser de dos tipus principals:

- **Camp escalar:** només cal un valor numèric en cada punt.  
  *Exemples:* temperatura, pressió, densitat de l’aire.
- **Camp vectorial:** cal indicar el **mòdul**, la **direcció** i el **sentit**.  
  *Exemples:* velocitat del vent, camp de forces.

Un **camp de forces** és, per tant, un **tipus de camp vectorial**.  
En cada punt de l’espai, si hi col·loquem una partícula, aquesta experimenta una força.  

Aquesta idea permet **descriure de manera unificada** molts fenòmens físics:  
una massa crea un **camp gravitatori**, una càrrega elèctrica crea un **camp elèctric**, etc.  
Tots dos són casos particulars del concepte general de **camp físic**.

---

## **1.2 — Intensitat de camp**

La **intensitat de camp** indica “**com de fort**” és el camp en un punt determinat.  
Es defineix com la **força per unitat de magnitud característica** (massa, càrrega, etc.) que actua sobre una partícula.

En cada tipus de camp hi ha una magnitud pròpia:

| Tipus de camp | Magnitud associada |
|:---------------|:------------------|
| Camp gravitatori | Massa |
| Camp elèctric | Càrrega elèctrica |
| Camp magnètic | Moviment de càrregues |

En general, la intensitat del camp pot variar segons la **distància o distribució** de la font.  
Quan disminueix amb el quadrat de la distància ($1/r^2$), parlem de **camps centrals newtonians**, un comportament molt comú a la natura.

---

## **1.3 — Representació del camp**

Els **camps vectorials** es representen gràficament mitjançant **línies de camp**, que indiquen direcció, sentit i intensitat.

| ![Línies de camp](img/camp_línies.png) |
|:--------------------------------------:|
| *Les línies de camp permeten visualitzar la direcció i intensitat del camp en cada punt.* |

- **Direcció:** la tangent a la línia de camp en aquell punt.  
- **Sentit:** cap a on actua la força.  
- **Intensitat:** proporcional a la densitat de línies (més juntes → camp més intens).

Quan la intensitat és constant a tot arreu, parlem de **camp uniforme** (línies paral·leles i equiespaiades).  
Quan varia amb la distància, parlem de **camp no uniforme** (línies radials o corbades).
En aquest cas, les linies poden ser radials, corbades o irregulars, segons la naturalesa de la font.

**Exemples:**
- En un camp gravitatori, les línies apunten cap a la massa que el crea.
- En un camp elèctric, les línies surten o entren segons el signe de la càrrega.

---

## **1.4 — Camps escalars i camps vectorials**

Els camps físics es poden classificar segons el tipus de magnitud associada:

| **Tipus de camp** | **Què descriu** | **Exemples generals** | **Representació habitual** |
|:------------------|:----------------|:----------------------|:---------------------------|
| **Escalar** | Valor numèric en cada punt | Temperatura, pressió, densitat | Mapes de contorns o superfícies equipotencials |
| **Vectorial** | Valor amb mòdul, direcció i sentit | Velocitat del vent, camp de forces | Fletxes o línies de camp |

> Els camps físics més importants a la natura (gravitatori, elèctric i magnètic) són **vectorials**,  
> ja que descriuen forces amb una direcció definida.

---

## **1.5 — Camps conservatius**

Un **camp conservatiu** és aquell en què el **treball realitzat per la força del camp** sobre una partícula **només depèn** dels punts inicial i final, i **no del camí** recorregut.

$$
W_{AB} = \int_A^B \vec{F}\cdot d\vec{r} = -\Delta U
$$

Això implica que, si la partícula torna al punt d’origen, el treball total és **zero**.

> Els camps conservatius permeten definir una **energia potencial associada**,  
> i descriure els fenòmens en termes d’energia en lloc de forces.

El **camp gravitatori** i el **camp eléctric** en són exemples típics, peró el concepte és general:

> Qualsevol camp on el treball sigui independent del recorregut és conservatiu.

---

## **Resum gràfic**

| **Figura** | **Tema visual** | **Idea principal** |
|:------------|:----------------|:-------------------|
| 1 | Tipus de camps | Diferència conceptual i classificació |
| 2 | Forces centrals newtonianes | Direcció cap a la font del camp |
| 3 | Línies de camp i intensitat | Densitat de línies = intensitat |
| 4 | Camp uniforme | Força constant a tot l’espai |
| 5 | Línies de camp radial | Exemple de camp central |
| 6 | Camps atractius i repulsius | Direcció segons el tipus de font |
| 7 | Treball independent del camí | Propietat conservativa |
| 8 | Treball nul en recorregut tancat | Confirmació d’un camp conservatiu |

---

## **1.6 — Conclusió**

El concepte de **camp físic** és essencial per comprendre com les forces actuen a distància.  
Permet una visió unificada de fenòmens aparentment diferents —com la gravitació, l’electricitat o el magnetisme— sota una mateixa idea:  
**l’acció d’una magnitud en tots els punts de l’espai**.

> En el següent bloc (CG2) estudiarem la **llei de la gravitació universal**,  
> una aplicació directa del concepte de camp físic al cas de la interacció entre masses.

---

# **CG2 — Llei de la gravitació universal**

---

## **2.1 — Enunciat i expressió vectorial de la força gravitatoria**

Isaac Newton (1642–1727) va formular la **llei de la gravitació universal** a partir de les observacions astronòmiques de **Kepler**.

Kepler va descriure **com** es movien els planetes; Newton va explicar **per què**:  
va atribuir l’acceleració d’un planeta a una **força d’atracció mútua** entre el Sol i el planeta, que **disminueix amb el quadrat de la distància**.

Aquesta força existeix entre **qualsevol parella de masses de l’univers**.

> **Enunciat de la llei de la gravitació universal:**  
> Tota partícula de matèria atrau qualsevol altra amb una força **directament proporcional** al producte de les seves masses i **inversament proporcional** al **quadrat de la distància** que les separa.

---

### **Expressió vectorial**

$$
\overrightarrow{F_{12}} = -\,G\,\frac{m_1 m_2}{r^2}\,\hat{u}_r
$$

on:  
- $G$ és la **constant de gravitació universal**,  
- $r$ és la **distància** entre les dues masses,  
- $\hat{u}_r$ és el **vector unitari** que uneix les dues masses.

> El signe negatiu indica que la força és **d’atracció**:  
> cada massa atrau l’altra seguint la direcció de la recta que les uneix.  
> L’orientació del vector unitari justifica aquest signe:  
> la direcció de la força gravitatòria és oposada a la del vector $\hat{u}_r$.

| ![Representació vectorial de la força gravitatòria](img/gravitacio1.png) |
|:------------------------------------------------------------------------:|
| *Les dues masses s’atrauen amb forces iguals i oposades sobre la línia que les uneix.* |

---

## **2.2 — Constant de gravitació universal $G$ i unitats**

La constant de gravitació universal **determina la intensitat** d’aquesta interacció:

$$
G = 6.67\times10^{-11}\ \mathrm{N·m^2/kg^2}
$$

Va ser determinada experimentalment per **Henry Cavendish (1798)** amb la seva famosa **balança de torsió**.

Les seves unitats garanteixen la coherència dimensional de la llei i asseguren que la força es mesura en **newtons (N)** quan:
- les masses s’expressen en **quilograms (kg)**,
- i la distància en **metres (m)**.

| ![Balança de torsió de Cavendish](img/gravitacio2.png) |
|:-------------------------------------------------------:|
| *Cavendish va determinar experimentalment la constant de gravitació universal.* |

---

## **2.3 — Força entre dues masses: mòdul, direcció i sentit**

La **força gravitatòria** és sempre **atractiva**, té **direcció radial** i **sentit cap al centre de la massa** que crea el camp.

Cada massa experimenta una força de la **mateixa magnitud** però de **sentit oposat**, formant un **parell d’acció i reacció** segons la tercera llei de Newton.

**Expressió escalar:**

$$
F = G\,\frac{m_1 m_2}{r^2}
$$

> És una **força central**, ja que actua al llarg de la línia que uneix els centres de les dues masses.

| ![Força entre dues masses](img/gravitacio3.png) |
|:-----------------------------------------------:|
| *La força gravitatòria és atractiva i radial.* |

---

## **2.4 — Comparació qualitativa amb la llei de Coulomb**

La llei de Newton té una forma **matemàtica molt similar** a la **llei de Coulomb** de l’electrostàtica.

| **Característica** | **Gravitació** | **Electrostàtica** |
|:-------------------|:---------------|:-------------------|
| **Font del camp** | Masses | Càrregues elèctriques |
| **Tipus de força** | Sempre atractiva | Atractiva o repulsiva |
| **Proporcionalitat** | $F \propto \frac{m_1 m_2}{r^2}$ | $F \propto \frac{q_1 q_2}{r^2}$ |
| **Constant** | $G$ | $k = \frac{1}{4\pi\varepsilon_0}$ |
| **Abast** | Universal | Depèn del medi |

> La **gravetat és molt més feble** que la força elèctrica,  
> però és sempre **atractiva** i predomina a **escala planetària i còsmica**.

| ![Comparació entre forces gravitacional i elèctrica](img/gravitacio4.png) |
|:-------------------------------------------------------------------------:|
| *La força de Coulomb pot ser atractiva o repulsiva; la gravetat, sempre atractiva.* |

---

## **2.5 — Superposició de forces en sistemes de masses**

Quan hi ha **més d’una massa** que actua sobre un cos, la força total és la **suma vectorial** de totes les forces individuals:

$$
\overrightarrow{F_\text{total}} = \sum_i \overrightarrow{F_i}
$$

Aquest és el **principi de superposició**, que permet calcular la **força resultant** en punts on actuen diverses fonts gravitatòries.

> Per exemple, el punt on les forces de dues masses iguals es compensen és exactament el punt mig entre elles.

| ![Superposició de forces gravitatòries](img/gravitacio5.png) |
|:-------------------------------------------------------------:|
| *La força total és la suma vectorial de totes les forces individuals.* |

---

## **2.6 — Resum del bloc CG2**

| **Concepte** | **Expressió** | **Comentari** |
|:--------------|:---------------|:---------------|
| **Llei de Newton** | $\overrightarrow{F} = -G\frac{m_1 m_2}{r^2}\hat{u}_r$ | Força atractiva i central |
| **Mòdul** | $F = G\frac{m_1 m_2}{r^2}$ | Disminueix amb $r^2$ |
| **Constant $G$** | $6.67\times10^{-11}\ \mathrm{N·m^2/kg^2}$ | Determinada per Cavendish |
| **Comparació amb Coulomb** | Mateixa estructura formal | Gravitació només atractiva |
| **Superposició** | $\overrightarrow{F_\text{total}} = \sum_i \overrightarrow{F_i}$ | Força resultant en sistemes múltiples |

---

## **2.7 — Conclusió**

La **llei de la gravitació universal** de Newton estableix la base de tota la **mecànica celeste** i de la comprensió de l’estructura de l’univers.  
Gràcies a ella, és possible descriure **òrbites planetàries, moviments de satèl·lits** i les interaccions gravitacionals entre cossos massius.

> En el següent bloc (CG3), es desenvolupa el **camp gravitatori** com a extensió d’aquesta llei, introduint els conceptes de **potencial gravitatori** i **energia potencial**.

---