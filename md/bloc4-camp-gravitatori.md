# Bloc 4. Camp gravitatori

---

# 1 — Concepte de camp físic

## 1.1 — Què és un camp físic

En molts fenòmens naturals, un cos pot **influir en un altre sense contacte directe**.  
Per explicar-ho, introduïm el **concepte de camp físic**.

> En una regió de l’espai hi ha un **camp físic** quan a cada punt d’aquesta regió hi està definida una determinada **magnitud física**.

Aquesta magnitud pot ser de dos tipus principals:

- **Camp escalar:** només cal un valor numèric en cada punt. Exemples: temperatura, pressió, densitat de l’aire.
- **Camp vectorial:** cal indicar el **mòdul**, la **direcció** i el **sentit**. Exemples: velocitat del vent, camp de forces.

| ![Exemples de camps](img/bloc4/0.png) |
|:--------------------------------------:|
| *[Exemples de camps físics.](https://www.tiempo.com/mapas-meteorologicos/temp2m-penin.html)* |

Un **camp de forces** és, per tant, un **tipus de camp vectorial**.  
En cada punt de l’espai, si hi col·loquem una partícula, aquesta experimenta una força.  

Aquesta idea permet **descriure de manera unificada** molts fenòmens físics:  
una massa crea un **camp gravitatori**, una càrrega elèctrica crea un **camp elèctric**, etc.  
Tots dos són casos particulars del concepte general de **camp físic**.

| ![Tipus de camps](img/bloc4/1.png) |
|:--------------------------------------:|
| *Tipus de camps físics.* |

---

## 1.2 — Intensitat de camp

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

## 1.3 — Representació del camp

Els **camps vectorials** es representen gràficament mitjançant **línies de camp**, que indiquen direcció, sentit i intensitat.

| ![Lines de camp](img/bloc4/2.png) | ![Lines de camp](img/bloc4/3.png) |
|:-----------------------:| :-----------------------:|
| *Direcció cap a la font del camp.* | *Línies de camp i intensitat.* |

- **Direcció:** la tangent a la línia de camp en aquell punt.  
- **Sentit:** cap a on actua la força.  
- **Intensitat:** proporcional a la densitat de línies (més juntes → camp més intens).

Quan la intensitat és constant a tot arreu, parlem de **camp uniforme** (línies paral·leles i equiespaiades).  
Quan varia amb la distància, parlem de **camp no uniforme** (línies radials o corbades).
En aquest cas, les linies poden ser radials, corbades o irregulars, segons la naturalesa de la font.

| ![Camp uniforme](img/bloc4/4.png) | ![Linies de camp radial central](img/bloc4/5.png) |
|:-----------------------:| :-----------------------:|
| *Camp uniforme.* | *Linies de camp radial central. Mes linies més intensitat* |

**Exemples:**
- En un camp gravitatori, les línies apunten cap a la massa que el crea.
- En un camp elèctric, les línies surten o entren segons el signe de la càrrega.

| ![Tipus de camps](img/bloc4/6.png) |
|:--------------------------------------:|
| *Exemples de camps elèctrics atractius i repulsius.* |

---

## 1.4 — Camps escalars i camps vectorials

Els camps físics es poden classificar segons el tipus de magnitud associada:

| **Tipus de camp** | **Què descriu** | **Exemples generals** | **Representació habitual** |
|:------------------|:----------------|:----------------------|:---------------------------|
| **Escalar** | Valor numèric en cada punt | Temperatura, pressió, densitat | Mapes de contorns o superfícies equipotencials |
| **Vectorial** | Valor amb mòdul, direcció i sentit | Velocitat del vent, camp de forces | Fletxes o línies de camp |

> Els camps físics més importants a la natura (gravitatori, elèctric i magnètic) són **vectorials**,  
> ja que descriuen forces amb una direcció definida.

---

## 1.5 — Camps conservatius

Un **camp conservatiu** és aquell en què el **treball realitzat per la força del camp** sobre una partícula **només depèn** dels punts inicial i final, i **no del camí** recorregut.

$$
W_{AB} = \int_A^B \vec{F}\cdot d\vec{r} = -\Delta U
$$

Això implica que, si la partícula torna al punt d’origen, el treball total és **zero**.

> Els camps conservatius permeten definir una **energia potencial associada**,  
> i descriure els fenòmens en termes d’energia en lloc de forces.

| ![Treballindependent del camí](img/bloc4/7.png) | ![Linies de camp radial central](img/bloc4/8.png) |
|:-----------------------:| :-----------------------:|
| *Treball independent del camí.* | *Treball nul en recorregut tancat.* |

El **camp gravitatori** i el **camp eléctric** en són exemples típics, peró el concepte és general:

> Qualsevol camp on el treball sigui independent del recorregut és conservatiu.

---

### — Conclusió CG1

El concepte de **camp físic** és essencial per comprendre com les forces actuen a distància.  
Permet una visió unificada de fenòmens aparentment diferents —com la gravitació, l’electricitat o el magnetisme— sota una mateixa idea:  
**l’acció d’una magnitud en tots els punts de l’espai**.

> En el següent bloc (CG2) estudiarem la **llei de la gravitació universal**,  
> una aplicació directa del concepte de camp físic al cas de la interacció entre masses.

---

# 2 — Llei de la gravitació universal

## 2.1 — Enunciat i expressió vectorial de la força gravitatoria

Isaac Newton (1642–1727) va formular la **llei de la gravitació universal** a partir de les observacions astronòmiques de **Kepler**.

Kepler va descriure **com** es movien els planetes; Newton va explicar **per què**:  
va atribuir l’acceleració d’un planeta a una **força d’atracció mútua** entre el Sol i el planeta, que **disminueix amb el quadrat de la distància**.

Aquesta força existeix entre **qualsevol parella de masses de l’univers**.

Enunciat de la **llei de la gravitació universal**: 
> Tota partícula de matèria atrau qualsevol altra amb una força **directament proporcional** al producte de les seves masses i **inversament proporcional** al **quadrat de la distància** que les separa.

**Expressió vectorial:**

$$
\overrightarrow{F_{g}} = -G \cdot \frac{m_1 m_2}{r^2} \cdot \hat{u}_r \qquad \text{on} \qquad \hat{u}_r = \frac{\overrightarrow{r}}{r}
$$

on:  
- $G$ és la **constant de gravitació universal**,  
- $r$ és la **distància** entre les dues masses,  
- $\hat{u}_r$ és el **vector unitari** que uneix les dues masses.

| ![Representació vectorial de la força gravitatòria](img/bloc4/9.png) |
|:------------------------------------------------------------------------:|
| *Llei de gravitació universal: $\overrightarrow{F_{g}} = -G \cdot \frac{m_1 m_2}{r^2} \cdot \hat{u}_r$* |


El signe negatiu indica que la força és **d’atracció**:  
- cada massa atrau l’altra seguint la direcció de la recta que les uneix.  
- L’orientació del vector unitari justifica aquest signe:  
- la direcció de la força gravitatòria és oposada a la del vector $\hat{u}_r$.


---

## 2.2 — Constant de gravitació universal $G$ i unitats

La constant de gravitació universal **determina la intensitat** d’aquesta interacció:

$$
G = 6.67\times10^{-11}\ \mathrm{N·m^2/kg^2}
$$

Va ser determinada experimentalment per **Henry Cavendish (1798)** amb la seva famosa **balança de torsió**.

Les seves unitats garanteixen la coherència dimensional de la llei i asseguren que la força es mesura en **newtons (N)** quan:
- les masses s’expressen en **quilograms (kg)**,
- i la distància en **metres (m)**.

---

## 2.3 — Força entre dues masses: mòdul, direcció i sentit

La **força gravitatòria** és sempre **atractiva**, té **direcció radial** i **sentit cap al centre de la massa** que crea el camp.

Cada massa experimenta una força de la **mateixa magnitud** però de **sentit oposat**, formant un **parell d’acció i reacció** segons la tercera llei de Newton.

| ![Força entre dues masses](img/bloc4/10.png) |
|:-----------------------------------------------:|
| *3ª Llei de Newton: LLei d'acció i reacció.* |

**Expressió escalar:**

$$
F = G \cdot \frac{m_1 m_2}{r^2}
$$

> És una **força central**, ja que actua al llarg de la línia que uneix els centres de les dues masses.


---

## 2.4 — Comparació qualitativa amb la llei de Coulomb

La llei de Newton té una forma **matemàtica molt similar** a la **llei de Coulomb** de l’electrostàtica.

| **Característica** | **Gravitació** | **Electrostàtica** |
|:-------------------|:---------------|:-------------------|
| **Font del camp** | Masses | Càrregues elèctriques |
| **Tipus de força** | Sempre atractiva | Atractiva o repulsiva |
| **Proporcionalitat** | $F \propto \frac{m_1 m_2}{r^2}$ | $F \propto \frac{q_1 q_2}{r^2}$ |
| **Constant** | $G$ | $k = \frac{1}{4\pi\varepsilon_0}$ |
| **Abast** | Universal | Depèn del medi |

> La **gravetat és molt més feble** que la força elèctrica, però és sempre **atractiva** i predomina a **escala planetària i còsmica**.

---

## 2.5 — Superposició de forces en sistemes de masses

Quan hi ha **més d’una massa** que actua sobre un cos, la força total és la **suma vectorial** de totes les forces individuals:

$$
\overrightarrow{F_\text{total}} = \sum_i \overrightarrow{F_i}
$$

Aquest és el **principi de superposició**, que permet calcular la **força resultant** en punts on actuen diverses fonts gravitatòries.

> Per exemple, el punt on les forces de dues masses iguals es compensen és exactament el punt mig entre elles.

| ![Superposició de forces gravitatòries](img/bloc4/11.png) |
|:-------------------------------------------------------------:|
| *La força total és la suma vectorial de totes les forces individuals.* |

---

## 2.6 — Resum del bloc CG2

| **Concepte** | **Expressió** | **Comentari** |
|:--------------|:---------------|:---------------|
| **Llei de Newton** | $\overrightarrow{F} = -G \cdot \frac{m_1 m_2}{r^2} \cdot \hat{u}_r$ | Força atractiva i central |
| **Mòdul** | $F = G \cdot \frac{m_1 m_2}{r^2}$ | Disminueix amb $r^2$ |
| **Constant $G$** | $6.67\times10^{-11}\ \mathrm{N·m^2/kg^2}$ | Determinada per Cavendish |
| **Comparació amb Coulomb** | Mateixa estructura formal | Gravitació només atractiva |
| **Superposició** | $\overrightarrow{F_\text{total}} = \sum_i \overrightarrow{F_i}$ | Força resultant en sistemes múltiples |

---

### — Conclusió CG2

La **llei de la gravitació universal** de Newton estableix la base de tota la **mecànica celeste** i de la comprensió de l’estructura de l’univers. Gràcies a ella, és possible descriure **òrbites planetàries, moviments de satèl·lits** i les interaccions gravitacionals entre cossos massius.

> En el següent bloc (CG3), es desenvolupa el **camp gravitatori** com a extensió d’aquesta llei, introduint els conceptes de **potencial gravitatori** i **energia potencial**.

---

# 3 — El camp gravitatori

## 3.1 — Definició

El **camp gravitatori** és el camp de forces que una massa crea al seu voltant i que actua sobre altres masses.  
En un punt de l’espai, la **intensitat del camp gravitatori** és la força per unitat de massa..

$$
\vec{g} = \frac{\vec{F}}{m}
$$

Com que la força gravitatoria és atractiva, el vector **g** apunta sempre **cap al centre de la massa que crea el camp**.  
Les seves unitats són **N/kg** o **m/s²**, ja que equival a una acceleració.

| ![Representació del camp gravitatori](img/bloc4/12.png) |
|:--------------------------------------:|
| *Representació del camp gravitatori. Més linies de camp representa més intensitat.* |

---

## 3.2 — Direcció, sentit i dependència amb la distància

Per una massa puntual $M$:

$$
\vec{g} = -G\frac{M}{r^2}\hat{u_r}
$$

- **Direcció**: línia que uneix el punt amb el centre de la massa.
- **Sentit**: cap a la massa que genera el camp.
- **Mòdul**: proporcional a la massa $M$ i inversament proporcional al quadrat de la distància $r$.

<!--🖼️ *[Imatge 2: Línies de camp d’una massa puntual i de dues masses iguals]* -->

A mesura que ens allunyem del cos, la intensitat del camp disminueix ràpidament.
 
| ![Disminució de g amb la distància](img/bloc4/13.png) |
|:--------------------------------------:|
| *Disminució de g amb la distància.* |

---

## 3.3 — Valor de g a la superfície d’un astre

Per a un planeta de massa \(M\) i radi \(R\):

$$
g_0 = \frac{GM}{R^2}
$$

Aquesta és la **intensitat de camp gravitatori** (o acceleració de la gravetat) a la superfície del planeta.  
El **pes** d’un cos és la força amb què la Terra (o un altre astre) l’atrau:

$$
\vec{p_0} = m\vec{g_0}
$$

---

## 3.4 — Variació de g amb l’altura

En un punt situat a una altura \(h\) respecte a la superfície:

$$
g_h = G\frac{M}{(R+h)^2}
$$

Com que $(R+h)^2 > R^2$, es compleix que $g_h < g_0$ :  
la intensitat del camp disminueix amb l’altura.

<!--🖼️ *[Imatge 3: Intensitat del camp en funció de l’altura]* -->

---

## 3.5 — Camp d’un sistema de masses

El **camp total** creat per diverses masses és la **suma vectorial** dels camps que crea cadascuna:

$$
\vec{g}_{total} = \sum_i \vec{g_i} = -G\sum_i \frac{m_i}{r_i^2}\hat{r_i}
$$

Això s’anomena **principi de superposició**.

<!--🖼️ *[Imatge 4: Camp creat per una distribució de masses puntuals]* ]: #
🖼️ *[Imatge 5: Equivalència entre massa esfèrica i massa puntual]* -->
 
---

## 3.6 — Components de g en coordenades

Si expressem el camp gravitatori en components:

- En **cartesianes**:  

$$
\vec{g} = g_x \hat{i} + g_y \hat{j} + g_z \hat{k}
$$

- En **polars** (entorn d’una massa central):  

$$
\vec{g} = -G\frac{M}{r^2}\hat{u_r}
$$

Aquestes formes permeten calcular el camp quan hi ha simetria esfèrica o en punts d’un sistema de masses.

<!--
### 🧭 Referències visuals

| Codi | Descripció |
|------|-------------|
| Imatge 1 | Variació del mòdul de g amb r |
| Imatge 2 | Línies de camp d’una massa puntual / dues masses |
| Imatge 3 | Disminució de g amb l’altura |
| Imatge 4 | Camp d’una distribució de masses puntuals |
| Imatge 5 | Equivalència massa esfèrica ↔ massa puntual |
-->

---

# 4 — Potencial i energia potencial gravitatòria

## 4.1 — Potencial gravitatori

Quan una massa crea un camp gravitatori, en qualsevol punt d’aquest camp hi ha associada una **energia per unitat de massa**.
Aquesta magnitud rep el nom de **potencial gravitatori**.

> El potencial indica **quant treball faria el camp** per portar una massa unitària des de l’infinit fins a un punt del camp.

$$
V_A = - W_{\infty \rightarrow A} = - \int_{\infty}^{r_A} \vec{F} \cdot \mathrm{d}\vec{r}
$$

**Expressió per a una massa M:**

$$
V = -\frac{G \cdot M}{r}
$$

* El potencial $V$ és una magnitud **escalar**.
* El signe “−” indica que el camp és **atractiu**.
* A mesura que ens **allunyem**, el valor del potencial s’aproxima a **zero** $\rightarrow V_{r_\infty} = 0.$
* La seva **unitat** és el joule per quilogram (**J/kg**).

|     ![Potencial d’una massa puntual](img/bloc4/14.png)    |
| :-------------------------------------------------------: |
| *Potencial d’una massa puntual en un punt A.* |

---

## 4.2 — Potencial gravitatori d’un sistema de masses

El **potencial gravitatori total** creat per diverses masses és la **suma de les quantitats escalars** dels potencials que crea cadascuna:

$$
V_{total} = \sum_i V_i = - G \sum_i \frac{m_i}{r_i}
$$

Això s’anomena **principi de superposició**.
> Sumem quantitats escalars que són sempre negatives i dona un resultat també negatiu.

| ![Superposició de potencials gravitatòries](img/bloc4/19.png) |
|:-------------------------------------------------------------:|
| *El $V_{total}$ és la suma escalar de tots els $V_i$ individuals.* |

---

## 4.3 — Energia potencial

Si la massa que es troba dins el camp no és unitària, la seva **energia potencial** és:

$$
E_p = m \cdot V = -\frac{G\cdot M\cdot m}{r}
$$

Aquesta energia representa la **capacitat del camp per fer treball** sobre la massa.
Com més lluny és la massa, **menys negativa** és l’energia potencial (el camp té menys “efecte”).

|         ![Potencial d’un conjunt de masses puntuals](img/bloc4/15.png)        |
| :---------------------------------------------------------------------------: |
| *Energia potencial gravitatòria.* |

---

## 4.4 — Relació amb el camp gravitatori

El **camp gravitatori** i el **potencial** estan relacionats:
on el camp és més intens, el potencial varia més ràpidament.

**Per a una massa puntual:**

$$
g = \frac{G\cdot M}{r^2}
\qquad\Rightarrow\qquad
V = -\frac{G\cdot M}{r}
\qquad\Rightarrow\qquad
g = - \frac{dV}{dr}
$$

Això vol dir que el camp (vector) es pot obtenir a partir del potencial (escalar).
En un diagrama, el pendent de $V(r)$ dona la intensitat del camp.

<!--
| ![Diagrames F-r i V-r](img/bloc4/16.png) |
| :--------------------------------------: |
|    *Fig. 1.28 – Gràfiques F–r i V–r.*    |
-->

---

## 4.5 — Treball i diferència de potencial

El **treball del camp gravitatori** quan una massa es mou entre dos punts **només depèn de les posicions inicial i final**, no del camí.

$$
W = - m \cdot [V(B) - V(A)] = -\Delta E_p
$$

> Això confirma que el camp gravitatori és **conservatiu**.

|                        ![Treball A→B](img/bloc4/15b.png)                      |
| :---------------------------------------------------------------------------: |
| *Treball per desplaçar una massa d’A a B (independent del camí).* |

---

## 4.6 — Energia mecànica

En absència de fregaments, la **suma de l’energia cinètica i potencial** és constant:

$$
E_m = E_c + E_p = \frac{1}{2} \cdot m \cdot v^2 - G \cdot \frac{M \cdot m}{r} = \text{constant}
$$

Per tant es compleix el **principi de conservació de l’energia**:

$$
\Delta E_m = \Delta E_c + \Delta E_p = 0
$$

Això vol dir que si una massa **guanya energia cinètica**, **perd energia potencial**, i a l’inrevés.
La variació d’una compensa la de l’altra.

<!--
| ![Força central i òrbita circular](img/bloc4/19.png) |
| :--------------------------------------------------: |
|   *Fig. 1.40 – Força central i moviment circular.*   |
-->

---

<!--
## 4.6 — Energia en moviments orbitals

Per a un cos que gira al voltant d’un planeta (òrbita circular):

$$
v = \sqrt{\frac{G,M}{r}} \qquad
E_c = \frac{G,M,m}{2r} \qquad
E_p = -\frac{G,M,m}{r} \qquad
E_m = -\frac{G,M,m}{2r}
$$

* L’energia total és **negativa**, perquè el cos està **lligat** al camp.
* Si l’òrbita és més alta (r↑), el cos té **menys velocitat** i **energia total més gran** (menys negativa).

|        ![Gràfiques Ec, Ep i E](img/bloc4/20.png)        |
| :-----------------------------------------------------: |
| *Fig. 1.41 – Variació d’Ec, Ep i E amb la distància r.* |

---

-->

## 4.7 — Gràfiques i tipus d’òrbita

El **valor de l’energia total** determina el tipus de trajectòria possible:

| **Energia total** |  **Significat físic**  |         **Trajectòria**         |
| :---------------: | :--------------------: | :-----------------------------: |
|     $E_m < 0$     | Cos **lligat** al camp |   Òrbita circular o el·líptica  |
|     $E_m = 0$     |      Cas **límit**     |   Parabòlica (escapament just)  |
|     $E_m > 0$     |    Cos **no lligat**   | Hiperbòlica (escapament sobrat) |

|             ![Trajectòries segons energia](img/bloc4/18.png) | ![Seccions còniques](img/bloc4/18b.png)|
| :---------------------------------: | :-----------------------------------: |
| *Trajectòries possibles segons el valor de l’energia total.* | *Seccions còniques.* |

> Les seccions còniques són les corbes obtingudes en tallar un con amb un pla, i són fonamentals per descriure trajectòries en física.

---

## 4.8 — Superfícies equipotencials

En els **camps conservatius**, com el **gravitatori** o l’**elèctric**, és útil introduir el concepte de **superfícies equipotencials** per interpretar situacions energètiques de manera visual.

> **Definició:**</br>
> Una **superfície equipotencial** és el conjunt de punts on el **potencial $V$** té el **mateix valor**.
> Si una massa es mou dins d’una superfície equipotencial, **el seu potencial no canvia**.

---

- **Treball nul dins d’una superfície equipotencial:** </br>

   Si $V(A) = V(B)$, aleshores:
   $$
   W_{A\to B} = -m \cdot [V(B) - V(A)] = 0
   $$
   El camp **no realitza treball** quan la massa es mou dins d’una superfície equipotencial.

-  **Perpendicularitat amb el camp:** </br>

   Les **línies de camp** són sempre **perpendiculars** a les **superfícies equipotencials**, ja que el camp apunta **en el sentit decreixent de $V$** (cap on el potencial disminueix).

|        ![Superfícies equipotencials](img/bloc4/20.png)        |
| :-----------------------------------------------------: |
| *Superfícies equipotencials perpendiculars a les línies de camp.* |

---

## 4.9 — Resum del bloc CG4

| Concepte          | Expressió         | Comentari                   |
| :---------------- | :---------------- | :-------------------------- |
| Potencial         | $V = -GM/r$       | Energia per unitat de massa |
| Energia potencial | $E_p = -GMm/r$    | Depèn de la posició         |
| Treball del camp  | $W = -\Delta E_p$ | Independent del camí        |
| Energia mecànica  | $E_m = E_c + E_p$ | Es conserva                 |
<!--| Òrbita circular   | $E_m = -GMm/(2r)$ | Cos lligat al planeta       | -->

---

### — Conclusió CG4

> Els conceptes de **potencial** i **energia potencial** permeten descriure el camp gravitatori **en termes d’energia** en lloc de forces.
> Això facilita l’estudi de moviments orbitals i problemes de conservació d’energia.

---

# 5 — Dinàmica orbital

---

## 5.1 — Equilibri en òrbites circulars

Quan un cos (com un satèl·lit o la Lluna) gira al voltant d’un planeta, està sotmès a la **força gravitatòria** del planeta, que actua com a **força centrípeta** necessària per mantenir-lo en òrbita.

$$
F_g = F_c
$$

On:
$$
\frac{GMm}{r^2} = \frac{mv^2}{r}
$$

> L’equilibri entre la força d’atracció gravitatòria i la força centrípeta manté el cos en moviment circular.

|        ![Equilibri de forces](img/bloc4/21.png)        |
| :---------------------------------------------------: |
| *La força gravitatòria actua com a força centrípeta.* |

---

## 5.2 — Deducció de la velocitat orbital

De la igualtat anterior:

$$
\frac{GMm}{r^2} = \frac{mv^2}{r}
$$

Simplificant $m$, $r$ i aïllant $v$:

$$
v = \sqrt{\frac{GM}{r}}
$$

> La velocitat orbital **no depèn de la massa del satèl·lit**, sinó només de la massa del planeta $M$ i de la distància $r$.

A mesura que augmenta $r$, la velocitat $v$ **disminueix**.

<!--
|         ![Velocitat orbital](img/bloc4/21.png)         |
| :---------------------------------------------------: |
| *La velocitat orbital és menor en òrbites més altes.* |
-->

---

## 5.3 — Període orbital i dependència amb la distància

El **període orbital** és el temps que triga el satèl·lit a fer una volta completa:

$$
T = \frac{2\pi r}{v}
$$

Substituint $v = \sqrt{\frac{GM}{r}}$:

$$
T = 2\pi \sqrt{\frac{r^3}{GM}}
$$

Això és la **tercera llei de Kepler**:

> El quadrat del període és proporcional al cub del radi de l’òrbita.

$$
T^2 \propto r^3
$$

|      ![Període orbital](img/bloc4/22.png)      |
| :-------------------------------------------: |
| *Òrbites més allunyades → període més llarg.* |

---

## 5.4 — Energies en òrbita circular

Un satèl·lit en òrbita té:

- **Energia cinètica:**

$$
E_c = \frac{1}{2}mv^2 = \frac{GMm}{2r}
$$

- **Energia potencial gravitatòria:**

$$
E_p = -\frac{GMm}{r}
$$

- L’**energia mecànica total** és:

$$
E_m = E_c + E_p = -\frac{GMm}{2r}
$$

<!--
> L’energia total és negativa: el satèl·lit està **gravitacionalment lligat** al planeta.

|                    ![Energies en òrbita](img/bloc4/24.png)                   |
| :-------------------------------------------------------------------------: |
| *L’energia potencial és el doble (en valor absolut) de l’energia cinètica.* |
-->

---

## 5.5 — Canvis d’òrbita (variacions de r, v i Em)

Quan un satèl·lit canvia d’altura (per exemple, de $r_1$ a $r_2$):

* Si **augmenta $r$** → **disminueix $v$** i **augmenta $E_m$** (menys negativa).
* Si **disminueix $r$** → **augmenta $v$** i **disminueix $E_m$** (més negativa).

> Per pujar d’òrbita cal **afegir energia**; per baixar-ne, **cal perdre’n**.

<!--
|         ![Canvi d'òrbita](img/bloc4/25.png)         |
| :------------------------------------------------: |
| *Canvi d’òrbita per impuls o maniobra energètica.* |
-->

---

<!--
## 5.6 — Òrbites baixes i òrbites altes (comparació qualitativa)

| **Tipus d’òrbita** | **Altura**                    | **Velocitat** | **Període**           | **Energia total** |
| :----------------- | :---------------------------- | :------------ | :-------------------- | :---------------- |
| Òrbita baixa (LEO) | Petita (pocs centenars de km) | Gran          | Curt (minuts o hores) | Més negativa      |
| Òrbita alta (GEO)  | Gran (milers de km)           | Petita        | Llarg (fins a 24 h)   | Menys negativa    |

> Com més lluny del planeta, més lent es mou el satèl·lit i més llarg és el seu període.

| ![Òrbites baixes i altes](img/bloc4/26.png) |
| :----------------------------------------: |
| *Comparació entre òrbites baixes i altes.* |

---
-->

### — Conclusió CG5

La dinàmica orbital combina la **gravitació de Newton** amb la **cinemàtica circular**.
A partir de la relació $F_g = F_c$ s’obtenen totes les expressions bàsiques de $v$, $T$ i $E_m$, que descriuen de manera completa el moviment dels satèl·lits i planetes.

> En el següent bloc estudiarem els **moviments no circulars (òrbites el·líptiques)** i la seva relació amb les **lleis de Kepler**.

---

# 6 — Lleis de Kepler

---

## 6.1 — Primera llei de Kepler

> *Els planetes descriuen òrbites el·líptiques al voltant del Sol, amb el Sol situat en un dels focus.*

Una **el·lipse** es defineix pels paràmetres següents:

- **Semieix major**: $a$ 
- **Semieix menor**: $b$  
- **Semidistància focal**: $c$

La relació entre ells és:

$$
a^2 = b^2 + c^2
$$

L’**excentricitat** és la mesura de com d’allargada és l’el·lipse:

$$
e = \frac{c}{a} = \sqrt{1 - \frac{b^2}{a^2}}
$$

> Si $e = 0$ → òrbita circular  
> Si $0 < e < 1 $→ òrbita el·líptica  

|        ![Primera llei de kepler](img/bloc4/23.png)   |
| :---------------------------------------------------: |
| *Òrbita el·líptica amb focus i definició de paràmetres.* |

---

## 6.2 — Segona llei de Kepler

> *El radi vector que uneix el planeta amb el Sol escombra àrees iguals en temps iguals.*

Això significa que:

- Quan el planeta és al **periheli** (punt més pròxim al Sol), es mou **més de pressa**.  
- Quan és a l’**afeli** (punt més llunyà), es mou **més lentament**.

Aquesta llei expressa la **conservació del moment angular**:

$$
\vec{L} = \vec{r} \times m\vec{v}
$$

Com que la força gravitacional és **central** (dirigida cap al Sol), el **moment de la força** és nul:

$$
\vec{M} = \vec{r} \times \vec{F} = 0
$$

> Això implica que $\vec{L}$  és constant i que la velocitat areolar també ho és:

$$
\frac{ΔS}{Δt} = \text{const.}
$$

|        ![Segona llei de kepler](img/bloc4/24.png)   |
| :---------------------------------------------------: |
| *Àrees iguals en temps iguals — periheli i afeli.* |

---

## 6.3 — Tercera llei de Kepler

> *El quadrat del període orbital és directament proporcional al cub de la distància mitjana al Sol.*

$$
T^2 = k \cdot r^3
$$

on la constant $k$ és comuna per a tots els planetes del sistema solar:

$$
k = \frac{4\pi^2}{G M}
$$

---

## 6.4 — Moment angular i conservació

El **moment angular** d’un planeta respecte del Sol és:

$$
L = mvrsin\alpha
$$

Com que la força és central, no hi ha moment de força extern $M=0$, i per tant:

$$
\frac{dL}{dt} = 0 \Rightarrow L = \text{constant}
$$

Això implica que el producte $v \cdot r$ es conserva:

$$
v_p r_p = v_a r_a
$$

on els subíndexs $p$ i $a$ indiquen **periheli** i **afeli**.

|        ![Conservació moment angular](img/bloc4/25.png)   |
| :---------------------------------------------------: |
| *vectors de posició i velocitat en periheli i afeli.* |

---

## 6.5 — Energia en òrbites el·líptiques

En un moviment el·líptic:

- La velocitat és **màxima al periheli** i **mínima a l’afeli**.
- L’**energia mecànica total** és constant i negativa:

$$
E = E_c + E_p = -\frac{G M m}{2a}
$$

---

### — Conclusió CG6

| **Llei** | **Forma matemàtica** | **Conseqüència** |
|:----------|:----------------------|:------------------|
| **1a — Òrbita el·líptica** | $r = \frac{a(1 - e^2)}{1 + e\cos\theta}$ | Trajectòries tancades, Sol en un focus |
| **2a — Àrees iguals** | $\frac{dA}{dt} = \text{constant}$ | Conservació de moment angular |
| **3a — Relació $T^2 \propto r^3$** | $T^2 = \frac{4\pi^2 r^3}{GM}$ | Planetes llunyans → períodes més llargs |

---


