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
