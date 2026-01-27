# Bloc 1 — Cinemàtica

# 1 — El moviment i els sistemes de referència

Els cossos ocupen punts determinats de l’espai. Quan aquestes posicions canvien al llarg del temps, diem que hi ha **moviment**.

> **Definició:**  
> El moviment és el canvi de posició d’un cos en el transcurs del temps.

La part de la física que estudia **com** es mouen els cossos, sense analitzar les causes del moviment, s’anomena **cinemàtica**.
Per simplificar, podem considerar el cos com un **mòbil puntual** o **partícula**, és a dir, un punt material on concentrem tota la massa.

- Per estudiar un moviment cal sempre un **sistema de referència**, és a dir, un punt i uns eixos respecte dels quals descrivim la posició del mòbil.  
- El moviment és **relatiu**, ja que depèn de l’observador i del sistema de referència utilitzat.

---

## 1.1 — Sistemes de coordenades

El sistema de coordenades més habitual és el **cartesià**, format per eixos perpendiculars que s’encreuen en un punt anomenat **origen O**.

### a. En el pla

Si el moviment té lloc en un pla, s’utilitzen dos eixos perpendiculars:
- **Eix X:** eix d’abscisses  
- **Eix Y:** eix d’ordenades  

També es poden utilitzar **coordenades polars (r, θ)** per moviments circulars.

| ![Sistema de coordenades en el pla](img/bloc1/1.png) |
|:--------------------------------------:|
| Sistema de coordenades cartesià en el pla |

### b. En l’espai

Si el moviment té lloc en l’espai, el sistema de coordenades cartesià consta de tres eixos **X, Y, Z**.  
Altres sistemes en l’espai són les **coordenades cilíndriques** i les **esfèriques**.

| ![Sistema de coordenades en l’espai](img/bloc1/2.png) |
|:--------------------------------------:|
| Sistema de coordenades cartesià en l'espai |

---

# 2 — Trajectòria i tipus de moviment

> **Trajectòria:** conjunt de totes les posicions que ocupa un cos durant el seu moviment.

Segons la forma de la trajectòria, podem distingir:

| Tipus de trajectòria | Dimensions | Tipus de moviment |
|----------------------|----------|-------------------|
| Rectilínia | Una dimensió | Moviment rectilini |
| Paràbola | Dues dimensions | Moviment parabòlic |
| Circular | Dues dimensions  | Moviment circular |
| Helicoidal | Tres dimensions  | Altres tipus de moviments |

---

# 3 — Les magnituds cinemàtiques

Per descriure el moviment fem servir diverses **magnituds cinemàtiques**.

## 3.1 — Temps

El **temps** és una **magnitud escalar** que indica la durada o l’instant en què es produeix un fenomen.

- Unitat SI: **segon (s)**  
- S’utilitza un **origen de temps** (t = 0) per mesurar la durada dels moviments.

L’**increment de temps** o **interval de temps** entre dos instants $t_1$ i $t_2$ és:

$$
\Delta t = t_2 - t_1
$$

---

## 3.2 — Posició

La **posició** indica on es troba el mòbil en un instant determinat respecte a l’origen del sistema de referència.

És una **magnitud vectorial** representada pel **vector de posició** $\vec{r}$.

- Unitat SI: **metre (m)**

### a. En el pla

$$
\vec{r} = x \cdot \hat{\imath} + y \cdot \hat{\jmath}
$$

### b. En l’espai

| ![Vector de posició quan el mòbil és en el punt P(x,y,z)](img/bloc1/4.png) |
|:--------------------------------------:|
| Vector de posició: $\vec{r} = x \cdot\hat{\imath} + y \cdot \hat{\jmath} + z \cdot \hat{k}$ |

<!--
La posició pot variar amb el temps. En aquest cas, parlem de la **funció del moviment** o **equació del moviment**:

- En el pla:  
  $$ \vec{r}(t) = x(t) + y(t) $$
- En l’espai:  
  $$ \vec{r}(t) = x(t) + y(t) + z(t) $$
-->

---

## 3.3 — Desplaçament

El **desplaçament** és el canvi de posició d’un cos entre dos instants de temps.  
És una **magnitud vectorial**, i la seva unitat en el SI és el **metre (m)**.

$$
\Delta \vec{r} = \vec{r}_2 - \vec{r}_1
$$

És a dir:

$$
\Delta \vec{r} = (x_2 - x_1)\cdot \hat{\imath} + (y_2 - y_1)\cdot \hat{\jmath}
$$

|![Vectors de posició i desplaçament entre P1 i P2](img/bloc1/5.png)|
|:--------------------------------------:|
| Vectors de posició i desplaçament entre $P_1$ i $P_2$ |

El **desplaçament** indica el vector que uneix la posició inicial i la final, mentre que l’**espai recorregut** és la longitud de la trajectòria (sempre positiu).

| ![Espai recorregut i desplaçament](img/bloc1/6.png) |
|:--------------------------------------:|
| Espai recorregut i desplaçament |

---

## 3.4 — Equació del moviment

Quan la posició d’un mòbil varia amb el temps, podem descriure el seu moviment mitjançant una **funció vectorial del temps**, anomenada **equació del moviment**.
Aquesta funció associa a cada instant $t$ un vector de posició $\vec{r}(t)$ que indica on es troba el mòbil en aquell moment:

$$
\vec{r}(t) = x(t)\cdot \hat{\imath} + y(t)\cdot \hat{\jmath} + z(t)\cdot \hat{k}
$$

- Cada component  $x(t)$, $y(t)$ i $z(t)$ és una **funció escalar del temps**, que expressa com canvia la coordenada corresponent.
- La combinació de les tres components forma una **funció vectorial**, perquè el seu resultat és un vector.

> **Interpretació geomètrica:**  
> Si representem gràficament totes les posicions successives $\vec{r}(t)$ en funció del temps, obtenim la **trajectòria** del mòbil.  
> El vector de posició indica, en cada instant, la **direcció** i la **distància** des de l’origen fins al punt on es troba el mòbil.

| ![Fig. 1.8 — Representació gràfica d’una funció vectorial del moviment](img/bloc1/7.png) |
|:--------------------------------------:|
| Equació vectorial del moviment. |

**Exemple:**

Suposem un moviment en el pla amb $x(t) = 2t$ i  $y(t) = t^2$ aleshores la funció vectorial del moviment és:

$$
\vec{r}(t) = 2t \cdot \hat{\imath} + t^2 \cdot\hat{\jmath}
$$

Per a cada valor de $t$, obtenim un punt de la trajectòria.

> - En aquest cas, la component $x(t)$ indica com avança el mòbil horitzontalment, mentre que $y(t)$ mostra com canvia la seva alçada.  
> - El conjunt de totes les posicions $\vec{r}(t)$ descriu el moviment complet en el pla.
> - La funció $\vec{r}(t)$ permet saber **on** és el mòbil en cada instant.
> - Si coneixem $\vec{r}(t)$, podem obtenir altres magnituds del moviment, com la **velocitat** i l’**acceleració**, derivant respecte al temps.

---

> **Resum:**  
> - El moviment és relatiu i depèn del sistema de referència.  
> - La trajectòria és el camí recorregut.  
> - El temps és una magnitud escalar.  
> - La posició i el desplaçament són vectors fonamentals en la descripció del moviment.

---

## 3.5 — Velocitat

La **velocitat** indica **com canvia la posició** d’un mòbil amb el temps, és a dir, la rapidesa i la direcció del moviment.

És una **magnitud vectorial**: té mòdul, direcció i sentit.

---

### a. Velocitat mitjana

Es defineix com el quocient entre el **desplaçament** i el **temps** emprat per efectuar-lo:

$$
\vec{v}_m = \frac{\Delta \vec{r}}{\Delta t} = \frac{\vec{r}_2 - \vec{r}_1}{t_2 - t_1}
$$

- Indica la **velocitat global** del moviment entre dos instants.
- Té la **mateixa direcció i sentit** que el desplaçament.
- La seva unitat en el SI és el **metre per segon (m/s)**.

| ![Velocitat mitjana com a pendent del segment](img/bloc1/8a.png) |
|:--:|
| La $\vec{v}_m$ és la pendent del segment de la gràfica $\vec{r}(t)$. |

---

### b. Velocitat instantània

Correspon a la **velocitat en un instant concret**.  
S’obté com el límit de la velocitat mitjana quan $\Delta t \to 0$:

$$
\vec{v}(t) = \lim_{\Delta t \to 0} \frac{\Delta \vec{r}}{\Delta t} = \frac{d\vec{r}}{dt}
$$

- És la **derivada temporal del vector posició**.  
- El seu mòdul s’anomena **celeritat** o **velocitat escalar**.

> **Interpretació geomètrica:**  
> El vector velocitat és **tangent a la trajectòria** en cada punt i el seu sentit indica el sentit del moviment.

| ![Vector velocitat tangent a la trajectòria](img/bloc1/9.png) |
|:--:|
| La velocitat instantània és tangent a la trajectòria. |

---

### c. Components de la velocitat

En el pla:
$$
\vec{v}(t) = \frac{dx}{dt} \cdot \hat{\imath} + \frac{dy}{dt} \cdot \hat{\jmath}
$$

En l’espai:
$$
\vec{v}(t) = \frac{dx}{dt}\cdot\hat{\imath} + \frac{dy}{dt}\cdot\hat{\jmath} + \frac{dz}{dt}\cdot\hat{k}
$$

---

### d. Representació gràfica

- En una gràfica **posició–temps (r–t)**, la velocitat és la **pendent** de la corba.
- En una gràfica **velocitat–temps (v–t)**, l’**àrea sota la corba** representa el desplaçament.

| ![Interpretació gràfica de la velocitat com a derivada](img/bloc1/10.png) | ![Interpretació gràfica de la velocitat com a integral](img/bloc1/11.png)|
|:--:|:--:|
| La pendent de la gràfica $r(t)$ dóna la velocitat | l’àrea sota $v(t)$ dóna el desplaçament. |

---

## 3.6 — Acceleració

La **acceleració** mesura **com canvia la velocitat** d’un mòbil amb el temps.  
També és una **magnitud vectorial**, amb unitat **metre per segon quadrat (m/s²)**.

---

### a. Acceleració mitjana

És el quocient entre la **variació de la velocitat** i el **temps** emprat per a aquest canvi:

$$
\vec{a}_m = \frac{\Delta \vec{v}}{\Delta t} = \frac{\vec{v}_2 - \vec{v}_1}{t_2 - t_1}
$$

| ![Acceleració mitjana entre dos instants](img/bloc1/1.jpg) |
|:--:|
| L’acceleració mitjana indica com varia la velocitat al llarg del temps. |

---

### b. Acceleració instantània

És la **derivada de la velocitat respecte al temps** o, equivalentment, la **segona derivada de la posició**:

$$
\vec{a}(t) = \frac{d\vec{v}}{dt} = \frac{d^2\vec{r}}{dt^2}
$$

> **Interpretació geomètrica:**  
> El vector acceleració indica com canvia la direcció o el mòdul del vector velocitat.  
> Si l’acceleració és constant i en la mateixa direcció que $\vec{v}$, el moviment és **rectilini uniformement accelerat (MRUA)**.

---

### c. Components de l’acceleració

En el pla:
$$
\vec{a}(t) = \frac{d^2x}{dt^2}\cdot\hat{\imath} + \frac{d^2y}{dt^2}\cdot\hat{\jmath}
$$

En l’espai:
$$
\vec{a}(t) = \frac{d^2x}{dt^2}\cdot\hat{\imath} + \frac{d^2y}{dt^2}\cdot\hat{\jmath} + \frac{d^2z}{dt^2}\cdot\hat{k}
$$

---

### d. Representació gràfica

- En una gràfica **velocitat–temps (v–t)**, la **pendent** indica l’acceleració.
- En una gràfica **acceleració–temps (a–t)**, l’**àrea sota la corba** indica la variació de velocitat.

| ![Interpretació gràfica de l’acceleració](img/bloc1/1.jpg) |
|:--:|
| La pendent de $v(t)$ és l’acceleració; l’àrea sota $a(t)$ és el canvi de velocitat. |

---

### e. Casos particulars

| Cas | Característiques | Exemple |
|-----|------------------|----------|
| **a = 0** | Moviment rectilini uniforme (velocitat constant) | MRU |
| **a constant** | Moviment rectilini uniformement accelerat | MRUA |
| **a variable** | Moviment general | Moviment oscil·latori, circular... |

---

> **Resum:**  
> - La **velocitat** és la derivada de la posició.  
> - L’**acceleració** és la derivada de la velocitat.  
> - Les gràfiques $r(t)$, $v(t)$ i $a(t)$ estan relacionades per derivació i integració successiva.

---

# 4 — Cinemàtica 1D

---

## 4.1 MRU

---

## 4.2 MRUA

---

### a. Caiguda lliure

---

# 5 — Cinemàtica 2D

---

## **5.1 — De cinemàtica 1D a 2D**

> *1D (moviment en una recta)*

* Només hi ha **una direcció possible**.
* El **mòdul** indica “quant val” la magnitud.
* El **signe (+ / −)** indica el **sentit**.
* **No hi ha ambigüitat**: un sol nombre és suficient.

En aquest cas:

* la **velocitat** i l’**acceleració** estan sempre **sobre la mateixa recta**
* tots els vectors són **colineals**

> En cinemàtica 1D, l’acceleració només pot fer **augmentar o disminuir la velocitat**
> (canvi del mòdul o del sentit).

Es pot treballar només amb **magnituds amb signe**.

---

> *2D (moviment en el pla)*

* Hi ha **infinites direccions possibles**.
* El **mòdul** ja no indica cap on apunta la magnitud.
* El **signe no és suficient** per descriure la direcció.
* **Cal indicar mòdul, direcció i sentit**.

En aquest cas:

* la **velocitat** i l’**acceleració** **no han de tenir la mateixa direcció**
* el moviment pot ser **corb**, encara que el mòdul de la velocitat sigui constant

> En cinemàtica 2D, la velocitat pot canviar **de mòdul**, **de direcció** o de totes dues coses alhora.

És necessari utilitzar **vectors**.

---

> *Components intrínsecs de l’acceleració*

En un moviment en el pla, l’acceleració pot produir **dos efectes físics diferents** sobre el moviment:

* **Canviar el mòdul de la velocitat**
* **Canviar la direcció de la velocitat**

| ![Components intrínsecs de l’acceleració](img/bloc1/14.png) |
|:--------------------------------------:|
| *Components intrínsecs de l’acceleració.* |

Per aquest motiu, en cinemàtica 2D es descompon l’acceleració en:

$$
a = a_t + a_n
$$

* **Acceleració tangencial** $a_t$

$$
a_t = \frac{dv}{dt}
$$

  * paral·lela a la velocitat
  * responsable del **canvi del mòdul** de la velocitat

* **Acceleració normal** $a_n$

$$
a_n = \frac{v^2}{R}
$$

  * perpendicular a la velocitat
  * responsable del **canvi de direcció** del moviment

> En 1D tota l’acceleració és tangencial.
> En 2D pot aparèixer també una acceleració normal.

---

## 5.2 — Llançament parabòlic

En cinemàtica 2D, el moviment d’un mòbil en el pla **no s’analitza com un moviment nou**, sinó com la **composició de dos moviments rectilinis independents**, un en cada eix del sistema de referència.

Aquesta manera de procedir és una **extensió directa del model utilitzat en cinemàtica 1D**:
es defineixen els paràmetres del moviment, s’escriuen les equacions en funció del temps i s’apliquen les condicions del problema.

| ![llançament parabòlic](img/bloc1/13.png) |
|:--------------------------------------:|
| *Llançament parabòlic.* |

---

> *1. Modelització del moviment en dos eixos*

S’escull un sistema de referència amb:

* eix **X** horitzontal
* eix **Y** vertical

El moviment es descriu mitjançant **dos problemes de cinemàtica 1D**, un per a cada eix, que comparteixen el **mateix temps**.

---

> *2. Paràmetres del moviment*

Els paràmetres que defineixen el moviment del mòbil es desglossen per components:

* Posició inicial: $x_0,\ y_0$

* Velocitat inicial: $v_{0x},\ v_{0y}$

* Acceleració: $a_{0x},\ a_{0y}$

* temps: $t_0$

Aquests paràmetres són **constants** i caracteritzen el moviment particular del mòbil.

---

> *3. Variables dependents del temps*

Les magnituds cinemàtiques es descriuen mitjançant funcions del temps, com ja s’ha fet en cinemàtica 1D:

* Posició: $x(t),\ y(t)$

* Velocitat: $v_x(t),\ v_y(t)$

* Acceleració: $a_x(t),\ a_y(t)$

Cada una d’aquestes funcions correspon a **un moviment rectilini en una sola direcció**.

---

> *4. Model general en cada eix*

Cada eix pot seguir un model diferent:

* **Moviment rectilini uniforme (MRU)**
  quan l’acceleració és nul·la

* **Moviment rectilini uniformement accelerat (MRUA)**
  quan l’acceleració és constant

Les equacions del moviment s’escriuen **independentment en cada eix**, substituint els paràmetres corresponents al model adequat.

---

> *5. Equacions particulars del moviment*

Un cop escollit el model per a cada eix, s’obtenen les equacions:

* $x(t)$, $v_x(t)$ i $a_x(t)$ a partir del model de l’eix X
* $y(t)$, $v_y(t)$ i $a_y(t)$a partir del model de l’eix Y

Aquestes equacions descriuen completament l’evolució del moviment en funció del temps.

---

> *6. Composició vectorial del moviment*

Tot i que el moviment es resol per eixos, el moviment real és **únic i té lloc en el pla**.
Per aquest motiu, les magnituds cinemàtiques s’expressen també en forma vectorial:

$$
\vec r(t) = x(t)\cdot \hat\imath + y(t)\cdot \hat\jmath
$$

$$
\vec v(t) = v_x(t)\cdot\hat\imath + v_y(t)\cdot\hat\jmath
$$

$$
\vec a(t) = a_x(t)\cdot\hat\imath + a_y(t)\cdot\hat\jmath
$$

Aquestes expressions permeten descriure **la direcció i el sentit del moviment** en cada instant.

---

> *7. Aplicació de les condicions del problema*

La resolució dels problemes es fa imposant les condicions específiques de cada situació sobre les funcions del moviment, com ja es feia en cinemàtica 1D.

Exemples habituals:

* $y(t)=0$ : impacte amb el terra
* $v_y(t)=0$ : alçada màxima
* $x_A(t)=x_B(t)$ i $y_A(t)=y_B(t)$ : trobada de dos mòbils

Aquestes condicions permeten determinar el temps corresponent i, a partir d’aquest, la resta de magnituds del moviment.

---

**Idea clau**

> En cinemàtica 2D, un moviment es resol com **dos moviments rectilinis en 1D**
> que comparteixen el mateix temps, però es descriu mitjançant **vectors**.

| ![llançament parabòlic](img/bloc1/14.jpg) |
|:--------------------------------------:|
| *Llançament parabòlic.* |

---

## 5.3 — Magnituds moviment circular

**El moviment circular** és un moviment en el pla en què la trajectòria és una **circumferència**.

En aquest tipus de moviment:

* la distància del mòbil al centre $R$ **és constant**
* el canvi fonamental **no és una translació**, sinó una **rotació**

Per descriure una rotació, cal introduir **magnituds angulars**, de manera anàloga a les magnituds lineals utilitzades en els moviments rectilinis.

---

### a. Angle recorregut

La posició del mòbil es pot descriure mitjançant l’**angle girat** $\varphi$, mesurat respecte d’una direcció de referència.

| ![Moviment circular](img/bloc1/15.png) |
|:--------------------------------------:|
| *L’estudi del moviment circular se simplifica utilitzant les coordenades polars.* |

> La unitat en el SI: **radiant (rad)**. Un radiant és l’angle que comprèn un arc de circumferència de longitud igual al radi. 

| ![Radiant](img/bloc1/17.png) |
|:--------------------------------------:|
| *Representació gràfica d'un radiant.* |

---

### b. Desplaçament angular

El desplaçament del mòbil es pot mesurar de dues maneres:

* **Increment de l’angle girat**
  $$
  \Delta\varphi = \varphi - \varphi_0
  $$

* **Arc recorregut** $s$, longitud de la trajectòria sobre la circumferència:

  $$
  s = r \cdot \Delta\varphi
  $$

| ![Desplaçament angular](img/bloc1/16.png) |
|:--------------------------------------:|
| *Desplaçament angular i conveni de signes.* |

---

### c. Velocitat angular

La velocitat de gir es mesura mitjançant la **velocitat angular** (**rad/s**):

* **Velocitat angular mitjana**
  $$
  \omega_m = \frac{\Delta\varphi}{\Delta t} = \frac{\varphi - \varphi_0}{t - t_0}
  $$

| ![Velocitat angular](img/bloc1/18.png) |
|:--------------------------------------:|
| *Velocitat angular.* |

* **Velocitat angular instantània**
  $$
  \omega = \frac{d\varphi}{dt}
  $$

* És un vector de direcció perpendicular al pla de gir i el sentit del qual està marcat per la regla de la mà dreta.

| ![Velocitat angular](img/bloc1/19.png) |
|:--------------------------------------:|
| *Representació del vector velocitat angular.* |

---

### d. Acceleració angular

Si la velocitat angular varia amb el temps, es defineix l’**acceleració angular** (**rad/s²**):

$$
\alpha = \frac{d\omega}{dt}
$$

* És un vector de direcció perpendicular al pla de gir i el sentit del qual està marcat per la regla de la mà dreta.

---

### e. Relació amb les magnituds lineals

Les magnituds angulars es poden relacionar amb les lineals mitjançant el radi $r$:

$$
v = \omega \cdot r
\qquad
a_t = \alpha \cdot r
$$

---

### f. Període

El període $T$ (en $s$) és la magnitud que mesura el temps que triga el mòbil a fer una volta en un moviment circular.

---

### g. Freqüència

La freqüència $f$ (en $Hz$) és la magnitud que mesura el nombre de voltes que fa un mòbil en un segon en un moviment circular.

$$
f = \frac{1}{T}
$$

---

## 5.4 — MCU