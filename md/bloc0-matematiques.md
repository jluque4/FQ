# Bloc 0. Qüestions generals de matemàtiques

## 0 — Introducció

L’alumnat ha de saber:
- Calcular derivades senzilles per a magnituds variables.
- Operar amb vectors: suma, resta i productes escalar i vectorial.
- Determinar mòdul, direcció i sentit del producte vectorial.
- Expressar vectors amb coordenades cartesianes o amb vectors unitaris $\hat{\imath},\hat{\jmath},\hat{k}$.
- Utilitzar el càlcul logarítmic i exponencial.
- Aplicar trigonometria bàsica.
- Calcular longitud, superfície i volum de figures habituals.
- Conèixer els prefixos del Sistema Internacional (de pico fins a tera).
- Entendre el concepte bàsic d’integral.

Es donarà rellevància a la **representació gràfica i vectorial** (v, a, F), línies de camp i superfícies equipotencials.  
El currículum és **obert i competencial**: es poden plantejar qüestions no explícites si són **resolubles** amb les competències adquirides i la informació de l’enunciat.

---

## 1 — Magnituds i unitats

### 1.1 — Magnituds físiques

En física, com en totes les **ciències experimentals**, la **presa de dades** dels fenòmens que ocorren a la naturalesa és essencial.
En aquesta presa de dades, tota qualitat d’un cos o fenomen que es pot **mesurar** rep el nom de **magnitud física**.

Les magnituds físiques permeten **quantificar** i **comparar** propietats dels objectes o dels processos naturals (com ara la massa, la temperatura o la velocitat).

### 1.2 — Tipus de magnituds

Les **magnituds físiques** poden classificar-se en **dos tipus principals**:

* **Magnitud escalar:**
  Queda completament definida amb un valor numèric i una unitat.
  **Exemples:** massa (kg), temps (s), temperatura (K).

* **Magnitud vectorial:**
  Per definir-la cal indicar el **mòdul**, la **direcció** i el **sentit**.
  **Exemples:** força (N), velocitat (m/s), acceleració (m/s²).

> *En una magnitud vectorial, la representació gràfica es fa mitjançant una fletxa: la seva longitud representa el mòdul, i la seva orientació indica la direcció i el sentit.*

### 1.3 — Magnituds fonamentals
| Magnitud | Símbol | Unitat (SI) | Símbol |
|---|---|---|---|
| Longitud | $l$ | metre | m |
| Massa | $m$ | quilogram | kg |
| Temps | $t$ | segon | s |
| Corrent elèctric | $I$ | ampere | A |
| Quantitat de substància | $n$ | mol | mol |
| Temperatura | $T$ | kelvin | K |
| Intensitat lluminosa | $I_v$ | candela | cd |

> *Aquestes magnituds serveixen com a base per derivar-ne d’altres més complexes, com la força, l’energia o la potència.*

### 1.4 — Magnituds derivades

Les **magnituds derivades** es construeixen a partir de les fonamentals mitjançant combinacions algebraiques.
A la taula següent es mostren algunes de les més utilitzades en el batxillerat:

| Magnitud | Símbol | Unitat (SI) | Símbol unitat | Tipus |
|---|---|---|---|---|
| Acceleració | $\vec{a}$ | metre/segon² | m/s² | Vectorial |
| Angle | $\alpha$ | radià | rad | Escalar |
| Camp elèctric | $\vec{E}$ | newton/coulomb | N/C | Vectorial |
| Camp gravitatori | $\vec{g}$ | newton/quilogram | N/kg | Vectorial |
| Camp magnètic | $\vec{B}$ | tesla | T | Vectorial |
| Càrrega | $Q$ | coulomb | C | Escalar |
| Energia/Treball | $E$ / $W$ | joule | J | Escalar |
| Flux magnètic | $\Phi$ | weber | Wb | Escalar |
| Freqüència | $f$ | hertz | Hz | Escalar |
| Longitud d’ona | $\lambda$ | metre | m | Escalar |
| Potència | $P$ | watt | W | Escalar |
| Potencial elèctric | $V$ | volt | V | Escalar |
| Resistència | $R$ | ohm | $\Omega$ | Escalar |
| Velocitat | $\vec{v}$ | metre/segon | m/s | Vectorial |

### 1.5 — Múltiples i submúltiples del SI

En física sovint treballem amb **valors molt grans o molt petits**.
Per evitar escriure nombres massa llargs, s’utilitzen **prefixos** que indiquen potències de deu.

| Prefix | Símbol | Valor | Exemple |
|---|---|---|---|
| Tera | T | $10^{12}$ | $1 \mathrm{TW}=10^{12}\mathrm{W}$ |
| Giga | G | $10^{9}$ | $1\mathrm{GW}=10^{9}\mathrm{W}$ |
| Mega | M | $10^{6}$ | $1\mathrm{MW}=10^{6}\mathrm{W}$ |
| Quilo | k | $10^{3}$ | $1\mathrm{km}=10^{3}\mathrm{m}$ |
| Mili | m | $10^{-3}$ | $1\mathrm{mm}=10^{-3}\mathrm{m}$ |
| Micro | µ | $10^{-6}$ | $1\mathrm{µm}=10^{-6}\mathrm{m}$ |
| Nano | n | $10^{-9}$ | $1\mathrm{nm}=10^{-9}\mathrm{m}$ |
| Pico | p | $10^{-12}$ | $1\mathrm{ps}=10^{-12}\mathrm{s}$ |

>  *Conèixer aquests prefixos permet expressar resultats amb claredat i escales adequades segons el fenomen físic estudiat.*

---

## 2 — Càlcul vectorial

### 2.1 — Elements d’un vector

Un vector és una **fletxa orientada** que representa una **magnitud física amb direcció i sentit** (com una força, una velocitat o un desplaçament).

| **Element**  | **Significat**                                                    |
| ------------ | ----------------------------------------------------------------- |
| **Direcció** | línia sobre la qual actua el vector                               |
| **Sentit**   | orientació de la fletxa sobre la línia d’acció                    |
| **Mòdul**    | longitud del segment, proporcional a la intensitat de la magnitud |

|     ![Un vector queda caracteritzat per mòdul, direcció i sentit](img/1.png)    |
| :-------------------------------------------------------------------------: |
| *Components del vector:  mòdul, direcció i sentit.* |

### 2.2 — Coordenades d’un vector

El vector definit pels punts d’origen $A(x_1, y_1)$ i extrem $B(x_2, y_2)$ s’expressa com:

$$
\vec{AB}=(x_2-x_1,\;y_2-y_1).
$$

Això vol dir que les **coordenades del vector** s’obtenen **restant les coordenades de l’extrem menys les de l’origen**. <br/>
**Exemple:**
Si $A(2,3)$ i $B(-3,1)$: $\overrightarrow{AB} = (-3 - 2, 1 - 3) = (-5, -2)$

| ![Coordenades d’un vector](img/2.png) | ![Vector AB de coordenades (-5,-2)](img/3.png)|
| :-----------------------------------: | :-------------------------------------------: |
| *Les coordenades del vector* | *El vector d'origen (2,3) i extrem (-3,1) té coordenades (-5, -2).* |

### 2.3 — Vector oposat i vector nul

- Dos vectors són **oposats** si tenen **el mateix mòdul i direcció**, però **sentit contrari**: $\vec{BA}=-\vec{AB}$.
- El **vector nul** és aquell en què l’origen i l’extrem coincideixen: $\vec{0}=(0,0)$.

|       ![Vectors oposats](img/4.png)          |
| :------------------------------------------: |
| *Els vectors $\vec{BA}$ i $\vec{AB}$ són oposats.* |

### 2.4 — Vector lliure

Tots els vectors que tenen el **mateix mòdul, direcció i sentit** són equivalents i formen un **vector lliure**.
Per comoditat, es col·loquen amb origen a l’origen de coordenades: $\vec{v}=(x,y)$.

|        ![Vectors lliures equivalents](img/5.png)                |
| :-------------------------------------------------------------: |
| *Els vectors a, b, c tenen el mateix mòdul, direcció i sentit.* |

### 2.5 — Mòdul i argument

- El **mòdul** d’un vector és la seva longitud:

$$
|\vec{v}|=\sqrt{v_x^2+v_y^2}
$$

- L’**argument** és l’angle que forma amb l’eix X:

$$
\theta=\arctan\\left(\frac{v_y}{v_x}\right)
$$

|                        ![Mòdul i components del vector](img/7.png)                        |
| :---------------------------------------------------------------------------------------: |
|       *El mòdul és la hipotenusa i les components $(v_x, v_y)$ són els catets.*           |


### 2.6 — Representacions cartesiana i polar

- En **forma cartesiana:** $\vec{v}=(v_x,v_y)$
- En **forma polar:** $\vec{v}=(v,\theta)$

on:

$$
v_x = v \cdot \cos \theta, \quad v_y = v \cdot \sin \theta
$$

|       ![Vector de mòdul v i argument θ](img/8.png)       |
| :--------------------------------------------------: |
| *Vector de mòdul v i argument $\theta$.* |

### 2.7 — Relacions trigonomètriques

Les relacions entre el mòdul i les components són:

$$
\sin\theta=\frac{v_y}{v},\quad
\cos\theta=\frac{v_x}{v},\quad
\tan\theta=\frac{v_y}{v_x}
$$

|                     ![Circumferència trigonomètrica](img/29.png)                    |
| :-----------------------------------------------------------------------------: |
| *Relacions trigonomètriques bàsiques en la circumferència unitària.* |

### 2.8 — Suma de vectors

La **suma de vectors** es pot fer de dues maneres:

### Gràficament

Hi ha dos mètodes habituals:

1. **Regla del paral·lelogram** — els vectors es col·loquen amb el mateix origen.
   El vector suma és la diagonal del paral·lelogram que formen.

|         ![Suma de vectors – regla del paral·lelogram](img/11.png)        |
| :------------------------------------------------------------------: |
| *Suma de vectors mitjançant la regla del paral·lelogram.* |

2. **Mètode del polígon** — es col·loca l’origen de cada vector en l’extrem de l’anterior.
   El vector suma uneix l’origen del primer amb l’extrem de l’últim.

|         ![Suma de vectors – mètode del polígon](img/12.png)        |
| :------------------------------------------------------------: |
| *Suma de vectors mitjançant el mètode del polígon.* |

### Analíticament

Si $\vec{a}=(a_x,a_y)$, $\vec{b}=(b_x,b_y)$, aleshores:

$$
\vec{a}+\vec{b}=(a_x+b_x, a_y+b_y).
$$

|                   ![Suma analítica de vectors](img/13.png)                   |
| :----------------------------------------------------------------------: |
| *Suma analítica de vectors a partir de les seves components.* |

### 2.9 — Diferència de vectors

Per calcular la diferència:

$$
\vec{a}-\vec{b}=\vec{a}+(-\vec{b}).
$$

És a dir, sumem al vector $\vec{a}$ el vector **oposat** de $\vec{b}$.

|                                      ![Diferència de vectors](img/14.png)                                     |
| :-------------------------------------------------------------------------------------------------------: |
| *La diferència $\vec{a} - \vec{b}$ s’obté sumant el vector oposat de b.* |

### 2.10 — Producte d’un escalar per un vector

Quan multipliquem un vector $\vec{v}$ per un **nombre real** $k\in\mathbb{R}$:

$$
k\cdot\vec{v}=(k \cdot v_x, k \cdot v_y).
$$

- $k>0$: mateix sentit; $k<0$: sentit contrari.  
- $k>1$: s’allarga; $k<1$: s’escurça.

|                            ![Producte d’un escalar per un vector](img/15.png)                           |
| :-------------------------------------------------------------------------------------------------: |
| *Canvia la intensitat del vector mantenint la direcció.* |

### 2.11 — Vector unitari

Un **vector unitari** és aquell de **mòdul 1** que indica **direcció i sentit**.

El vector unitari associat a $\vec{v}$ és:

$$
\hat{u}_v=\frac{\vec{v}}{|\vec{v}|}
$$

Això significa que té el mateix sentit i direcció, però **mòdul unitari**.

|                            ![Vector unitari](img/16.png)                            |
| :-----------------------------------------------------------------------------: |
| *Un vector amb la mateixa direcció i sentit que v, però mòdul 1* |

Si es multiplica per un escalar k: 

$$
k · \hat{u}_v
$$

el resultat és un vector amb **mòdul |k|** i la mateixa direcció.

|   ![Producte d’un vector unitari per un escalar](img/17.png)  |
| :-------------------------------------------------------: |
| *Producte d’un vector unitari per un escalar.* |

### 2.12 — Vectors unitaris i components cartesianes

En el pla, definim els vectors unitaris bàsics:

$$
\hat{\imath}=(1,0),\quad \hat{\jmath}=(0,1)
$$

| ![Vectors unitaris i j](img/18.png) |
| :--------------------: |
| *Vectors unitaris $\hat{i}$ i $\hat{j}$ al pla.* |

En l’espai tridimensional afegim:

$$
\hat{k} = (0, 0, 1)
$$

![Vector i+2j+3k](img/22.png) |
| :-------------------------: |
| *Vector tridimensional $\hat{i} + 2\hat{j} + 3\hat{k}$.* |

Així, qualsevol vector es pot escriure com:

$$
\vec{v}=v_x\hat{\imath}+v_y\hat{\jmath}+v_z\hat{k}
$$

| ![Vector en funció dels vectors unitaris i, j](img/19.png) |
| :--------------------: |
| *Representació d’un vector com a combinació lineal.* |

### 2.13 — Producte escalar

El **producte escalar** de dos vectors és una operació que dona com a resultat **un escalar (un nombre)**.

### Definició

Donats dos vectors $\vec{a} \text{ i } \vec{b}$, el seu producte escalar és: 

$$
\vec{a}\cdot\vec{b}=|\vec{a}| \cdot |\vec{b}| \cdot \cos\alpha
$$

on $\alpha$ és l’angle entre els dos vectors.

|                                  ![Producte escalar de dos vectors](img/23.png)                                 |
| :---------------------------------------------------------------------------------------------------------: |
| *És el producte dels mòduls pel cosinus de l’angle que formen.* |

###  Càlcul a partir de les components

Si $\vec{a} = (a_x, a_y, a_z), \quad \vec{b} = (b_x, b_y, b_z)$ aleshores:  

$$
\vec{a}\cdot\vec{b}=a_x \cdot b_x+a_y \cdot b_y+a_z \cdot b_z.
$$

###  Propietats

- És **commutatiu**: $\vec{a} \cdot \vec{b} = \vec{b} \cdot \vec{a}$
- Si dos vectors són **perpendiculars**, llavors: $\vec{a}\perp\vec{b}$ $\Rightarrow$ $\vec{a} \cdot \vec{b} = 0$
- El producte escalar mesura **el grau de paral·lelisme** entre vectors.

### 2.14 — Angle entre dos vectors

El producte escalar ens permet calcular **l’angle entre dos vectors**:

$$
\cos\alpha=\frac{\vec{a}\cdot\vec{b}}{|\vec{a}|\cdot|\vec{b}|}
\quad\Rightarrow\quad
\alpha=\arccos\left(\frac{\vec{a}\cdot\vec{b}}{|\vec{a}|\cdot|\vec{b}|}\right)
$$

|                          ![Angle entre dos vectors](img/24.png)                          |
| :----------------------------------------------------------------------------------: |
| *L’angle entre dos vectors es calcula a partir del seu producte escalar.* |

### 2.15 — Producte vectorial

El **producte vectorial** de dos vectors dona com a resultat **un altre vector**.

$$
\vec{c}=\vec{a}\times\vec{b}
$$

### Característiques

| Propietat    | Descripció                                                                 |  
| ------------ | -------------------------------------------------------------------------- |
| **Mòdul**    | $c  =  a  \cdot  b \cdot \sin \alpha$ |
| **Direcció** | Perpendicular al pla que conté $\vec{a}$ i $\vec{b}$ | 
| **Sentit**   | Determinat per la **regla de la mà dreta**      |  

|![Direcció del producte vectorial](img/25.png)|![Sentit del producte vectorial – regla de la mà dreta](img/26.png)|![Sentit contrari de b × a](img/27.png)|
| :-----------------------------------------------: | :-----------------------------------------------: |:-----------------------------------------------: |
| *La direcció és perpendicular al pla dels vectors.* | *El sentit ve donat per la regla de la mà dreta.* | *El sentit de $\vec{b} \times \vec{a}$ és contrari al de $\vec{a} \times \vec{b}$.* |

###  Expressió analítica (determinant 3x3)

|           ![Càlcul del producte vectorial mitjançant determinant](img/28.png)           |
| :---------------------------------------------------------------------------------: |
| *Càlcul del producte vectorial mitjançant el determinant de components.* |

### Propietats

* **No és commutatiu:** $\vec{a}\times\vec{b}=-(\vec{b}\times\vec{a})$
* Si $\vec{a}$ i $\vec{b}$ són **paral·lels**, llavors: $\vec{a}\parallel\vec{b}$ $\Rightarrow$ $\vec{a}\times\vec{b}=\vec{0}$
* El vector resultant és **perpendicular** als dos vectors originals: $\vec{a}\times\vec{b} \perp \vec{a} \text{ i } \vec{b}$

### **Interpretació geomètrica**

El mòdul $|\vec{a}\times\vec{b}|$ representa l’**àrea del paral·lelogram** determinat pels vectors $\vec{a}$ i $\vec{b}$.

|           ![Interpretació geomètrica](img/30.png)           |
| :---------------------------------------------------------------------------------: |
| *Interpretació geomètrica del mòdul del producte vectorial.* |

### 2.16 — Resum del càlcul vectorial
| Operació | Expressió | Resultat | Tipus |
|---|---|---|---|
| $\vec{a}+\vec{b}$ | suma component a component | vector | Vectorial |
| $\vec{a}-\vec{b}$ | diferència component a component | vector | Vectorial |
| $k\cdot\vec{a}$ | escalat per $k$ | vector | Vectorial |
| $\vec{a}\cdot\vec{b}$ | $a_x \cdot b_x+a_y \cdot b_y+a_z \cdot b_z$ | escalar | Escalar |
| $\vec{a}\times\vec{b}$ | determinant $3\times3$ | vector ⟂ a $\vec{a},\vec{b}$ | Vectorial |

---

## 3 — Càlcul diferencial i integral

### 3.1 — Concepte de funció i representació

Una **funció** és una relació entre dues magnituds, una de **variable independent** i una altra de **dependent**. </br>
En física, les funcions descriuen com una magnitud canvia en el temps o en l’espai.</br>
Exemples: $y=f(x)$, $y=f(t)$, $y=f(x,y,z)$.

### Exemples físics

| Gràfic               | Significat físic                                   |
| :------------------- | :------------------------------------------------- |
| Posició – Temps      | Indica com varia la posició d’un cos amb el temps. |
| Velocitat – Temps    | La pendent del gràfic és l’acceleració.            |
| Força – Desplaçament | L’àrea sota la corba és el treball realitzat.      |

|            ![Representació gràfica d’una funció física](img/31d.png)           |
| :-----------------------------------------------------------------------: |
| *Gràfics velocitat–temps i posició–temps.* |

### 3.2 — Càlcul diferencial (Derivades)

### Definició

La **derivada** d’una funció mesura la **velocitat de canvi** d’una magnitud respecte a una altra:

| ![Pendent d’una corba com a derivada](img/32b.png) |
| :-----------------------------------------------------------: |
| *Definició de derivada.* |


|       ![Pendent d’una corba com a derivada](img/32a.png)   |
| :-----------------------------------------------------------: |
| *La derivada representa la pendent de la recta tangent a la corba.* |

### Interpretació física

| Magnitud | Derivada | Significat |
|---|---|---|
| Posició $\vec{r}(t)$ | $\vec{v}(t)=\dfrac{d\vec{r}}{dt}$ | Velocitat instantània |
| Velocitat $\vec{v}(t)$ | $\vec{a}(t)=\dfrac{d\vec{v}}{dt}$ | Acceleració instantània |
| Treball $W(t)$ | $P(t)=\dfrac{dW}{dt}$ | Potència instantània |

### Regles bàsiques de derivació

| Operació | Regla | Exemple |
|---|---|---|
| Suma | $(f+g)'=f'+g'$ | $(x^2+3x)'=2x+3$ |
| Producte | $(fg)'=f'g+fg'$ | $(x\sin x)'=\sin x+x\cos x$ |
| Quocient | $\left(\frac{f}{g}\right)'=\frac{f'g-fg'}{g^2}$ | $\left(\frac{\sin x}{x}\right)'=\frac{x\cos x-\sin x}{x^2}$ |
| Composta (cadena) | $(f\circ g)'=f'(g(x)) \cdot g'(x)$ | $(\sin(x^2))'=\cos(x^2)\cdot 2x$ |

### Derivades immediates

|         ![Taula de derivades immediates](img/33b.png)        |
| :-----------------------------------------------------: |
| *Derivades habituals utilitzades en física.* |

### 3.3 — Càlcul integral

### Definició

La **integral** és l’operació inversa de la derivada i representa l’**acumulació contínua** d’una magnitud.

$$
\int_a^b f(x) \cdot \mathrm{d}x
$$

| ![Àrea sota la corba – interpretació geomètrica de la integral](img/34.png) |
| :---------------------------------------: | 
| *La integral definida representa l’àrea sota la corba de la funció.* |

### Interpretació física

| Magnitud | Integral | Significat |
|---|---|---|
| Velocitat $v(t)$ | $\int v(t) \cdot \mathrm{d}t$ | Desplaçament total  |
| Acceleració $a(t)$ | $\int a(t) \cdot \mathrm{d}t$ | Variació de la velocitat |
| Força $F(x)$ | $\int F(x) \cdot \mathrm{d}x$ | Treball realitzat  |
| Potència $P(t)$ | $\int P(t) \cdot \mathrm{d}t$ | Energia acumulada |

*Integrar és sumar infinites petites parts d’una magnitud.*

###  Integrals immediates

|        ![Taula d’integrals immediates](img/35b.png)       |
| :--------------------------------------------------: |
| *Integrals habituals en física.* |

### 3.4 — Aplicacions en Física

| Fenomen | Expressió | Interpretació |
|---|---|---|
| Velocitat instantània | $v=\dfrac{\mathrm{d}x}{\mathrm{d}t}$ | Canvi de posició |
| Acceleració | $a=\dfrac{\mathrm{d}v}{\mathrm{d}t}$ | Canvi de velocitat |
| Desplaçament | $\Delta x=\int v(t)\cdot \mathrm{d}t$ | Àrea sota la corba $v$-$t$ |
| Treball | $W=\int F(x) \cdot \mathrm{d}x$ | Energia transferida pel moviment |
| Energia | $E=\int P(t) \cdot \mathrm{d}t$ | Energia acumulada en el temps |

|                 ![Relació posició–velocitat–acceleració](img/36b.png)                                 |
| :---------------------------------------------------------------------------------------------------: |
| *Relació entre posició, velocitat i acceleració: derivar o integrar permet passar d’una a una altra.* |

### Relació fonamental derivació–integració

$$
\frac{\mathrm{d}}{\mathrm{d}x}\left(\int f(x) \cdot \mathrm{d}x\right)=f(x)
\qquad\Longleftrightarrow\qquad
\int f'(x) \cdot \mathrm{d}x=f(x)+C
$$

*Derivar descompon, integrar acumula: són processos inversos.*

### Resum del càlcul diferencial i integral
| Operació | Significat | Resultat |
|---|---|---|
| Derivada $f'(x)$ | Canvi instantani | Pendent de la corba |
| Integral $\int f(x) \cdot \mathrm{d}x$ | Acumulació | Àrea sota la corba |
| $f''(x)$ | Canvi del canvi | Acceleració, curvatura |
| $\dfrac{\mathrm{d}}{\mathrm{d}x}\left(\int f \cdot \mathrm{d}x\right)$ | Inversió d’operacions | Retorna $f(x)$ |
