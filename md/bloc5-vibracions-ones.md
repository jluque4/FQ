# Bloc 5 — Vibracions i ones

---

# 1 — Moviments periòdics i oscil·latoris

## 1.1 — Moviment periòdic

Un **moviment periòdic** és aquell en què el mòbil **repeteix el mateix moviment** a intervals regulars de temps.

| ![Moviment circular uniforme](img/bloc5/1.png) | ![Pèndol](img/bloc5/2.png) | ![Cos que penja d’una molla](img/bloc5/3.png) |
|:------------------:|:------------------------:|:------------------------:|
| *Moviment circular uniforme.* | *Pèndol.*| *Cos que penja d’una molla.*|

---

## 1.2 — Moviment oscil·latori

Un **moviment oscil·latori** (o vibratori) és un cas particular de moviment periòdic en què el mòbil:

* es mou **al voltant d’una posició d’equilibri**
* i **passa repetidament** per aquesta posició 

Anomenem **oscil·lació** (o vibració) el moviment complet que es fa durant el temps d’un període (T). 

| ![Moviment oscil·latori](img/bloc5/4.png) |
|:--------------------------------------:|
| *Moviment oscil·latori.* |

Exemples: el **pèndol** i el sistema **massa–molla**. En canvi, el **moviment circular uniforme** és periòdic però **no és oscil·latori**, perquè no hi ha cap posició d’equilibri al voltant de la qual es produeix la vibració. 

---

# 2 — Moviment harmònic simple

El **moviment harmònic simple (MHS)** és el moviment oscil·latori més senzill que existeix. 

---

## 2.1 — L’equació del MHS

> El **moviment harmònic simple** és aquell moviment que resulta de projectar un moviment circular uniforme sobre un eix que passa pel centre de la circumferència i que està contingut en el pla que la defineix.

| ![Moviment harmònic simple](img/bloc5/5.png) | ![Components cartesians](img/bloc5/6.png)|
|:--------------------------------------:|:-----:|
| *Moviment harmònic simple.* | *Components cartesians x, y del vector de posició.* | 

Aquesta és l’**equació general del moviment harmònic simple**:

$$
\boxed{x(t)=A\sin(\omega t+\varphi_0)}
$$

---

## 2.2 — Magnituds del MHS

Per descriure completament un moviment harmònic simple (MHS) cal definir un conjunt de magnituds característiques que en determinen el comportament temporal i espacial. 

---

### a. Període

El **període $T$** és el temps que el mòbil tarda a efectuar una oscil·lació completa, és a dir, a tornar a la mateixa posició amb el mateix estat de moviment.

$$
T = \text{temps d’una oscil·lació}
$$

Unitat en el SI: **segon (s)**. 

---

### b. Freqüència 

La **freqüència $f$** és el nombre d’oscil·lacions que el mòbil realitza en un segon. És la magnitud inversa del període:

$$
f = \frac{1}{T}
$$

Unitat en el SI: **hertz (Hz)**, equivalent a $s^{-1}$. 

---

### c. Freqüència angular 

La **freqüència angular $\omega$** (o pulsació) coincideix amb la velocitat angular del moviment circular uniforme del qual el MHS és projecció. La seva unitat és el **radiant per segon (rad/s)**. Les relacions entre $\omega$, $f$ i $T$ són:

$$
\omega = 2\pi f \text{ ; } \omega = \frac{2\pi}{T}
$$

Aquesta magnitud indica la rapidesa amb què evoluciona la fase del moviment.

---

### d. Elongació

L’**elongació** és la posició del mòbil respecte del punt d’equilibri $O$, amb el criteri de signes establert. Ve donada per l’equació general del MHS:

$$
x(t) = A \sin(\omega t + \varphi_0)
$$

Unitat en el SI: **metre (m)**. 

---

### e. Amplitud

L’**amplitud**  $A$ és el valor màxim de l’elongació.

$$
A = \text{màxima separació respecte l’equilibri}
$$

És constant en absència de fregament.

---

### f. Fase inicial

La **fase inicial $\varphi_0$** és una constant que depèn de la posició angular inicial del mòbil en l’instant inicial $t=0$. La relació amb la posició inicial és:

$$
x(0) = A \sin(\varphi_0)
$$

Unitat en el SI: **radiant (rad)**. 

---

### g. Fase del moviment

La **fase del moviment $\varphi$** és la posició angular del mòbil:

$$
\varphi = \varphi_0 + \omega t
$$

i determina l’estat de vibració del sistema en cada instant. També s’expressa en **radians**.

---

### h. Representació gràfica

Si representem l’elongació $x$ en funció del temps $t$, obtenim el **diagrama $x$-$t$**, que té forma sinusoidal o cosinusoidal. Aquesta representació permet visualitzar:

* el període $T$,
* l’amplitud $A$,
* i la fase inicial $\varphi_0$.

| ![Diagrama y-t del moviment harmònic simple](img/bloc5/7.png) | ![Exemple MHS](img/bloc5/8.png)| 
|:--------------------------------------:|:--------------------------------------:|
| *Diagrama y-t del moviment harmònic simple.* | *Exemple del MHS.*|

---

## 2.3 — Velocitat i acceleració del MHS

Podem determinar la **velocitat** i l’**acceleració** d’un moviment harmònic simple derivant l’equació del moviment respecte del temps. Partim de l’equació del moviment:

$$
x(t)=A\sin(\omega t+\varphi_0)
$$

---

> *Velocitat*

La **velocitat instantània** és la derivada de la posició respecte del temps:

$$
v(t)=\frac{dx}{dt}
$$

Derivant l’equació del moviment obtenim:

$$
v(t)=A\omega\cos(\omega t+\varphi_0)
$$

D’aquesta expressió es dedueix que:

- la velocitat és **màxima quan el mòbil passa per la posició d’equilibri** $(x=0)$  
- la velocitat és **nul·la als punts extrems** $(x=\pm A)$

El valor màxim de la velocitat és:

$$
v_{max}=A\omega
$$

---

> *Acceleració*

L’**acceleració instantània** és la derivada de la velocitat respecte del temps:

$$
a(t)=\frac{dv}{dt}
$$

Derivant l’expressió de la velocitat obtenim:

$$
a(t)=-A\omega^2\sin(\omega t+\varphi_0)
$$

Si comparem aquesta expressió amb la del moviment:

$$
x(t)=A\sin(\omega t+\varphi_0)
$$

podem escriure:

$$
\boxed{a(t)=-\omega^2 x(t)}
$$

Aquesta relació mostra una propietat fonamental del moviment harmònic simple:

> **l’acceleració és proporcional a l’elongació i té sentit contrari.**

---

> *Valors màxims i mínims del MHS*

De les expressions anteriors es dedueix:

$$
v_{max}=A\omega
$$

$$
a_{max}=A\omega^2
$$

Així:

- la **velocitat és màxima a la posició d’equilibri**
- l’**acceleració és màxima als extrems de l’oscil·lació** $(x=\pm A)$

| ![Valors màxims i mínims del MHS](img/bloc5/10.png) |
|:--------------------------------------:|
| *Valors màxims i mínims del MHS.* |

---

> *Desfasament entre les magnituds*

Les tres magnituds del moviment harmònic simple **no estan en fase**.

- la **velocitat** està desfasada **$\frac{\pi}{2}$ rad** respecte de l’elongació
- l’**acceleració** està desfasada **$\pi$ rad** respecte de l’elongació 

Això es pot observar clarament si representem conjuntament els diagrames:

| ![Desfasament entre les magnituds](img/bloc5/11.png) |
|:--------------------------------------:|
| *Desfasament entre les magnituds.* |

---

## 2.4 — Dinàmica del MHS

Fins ara hem descrit el moviment harmònic simple des del punt de vista **cinemàtic**. Ara veurem quin és l’origen físic d’aquest moviment utilitzant la **segona llei de Newton**.

---

### a. Sistema massa–molla

Considerem un cos de massa $m$ unit a una molla de constant elàstica $k$.

| ![Dinàmica del moviment harmònic simple MHS](img/bloc5/12.png) |
|:--------------------------------------:|
| *Dinàmica del moviment harmònic simple MHS.* |

Segons la **llei de Hooke**, la força que exerceix la molla és proporcional a l’elongació:

$$
F_e = -kx
$$

El signe negatiu indica que la força sempre té sentit oposat al desplaçament. Aplicant la **segona llei de Newton**:

$$
F = ma
$$

obtenim:

$$
ma = -kx
$$

o bé

$$
a = -\frac{k}{m}x
$$

Comparant amb l’expressió general del moviment harmònic simple $a = -\omega^2 x$ deduïm que:

$$
-\omega^2 x = -\frac{k}{m}x
$$

i per tant:

$$
\boxed{\omega = \sqrt{\frac{k}{m}}}
$$

Per tant, el **període d’oscil·lació** del sistema massa–molla és:

$$
T = 2\pi \sqrt{\frac{m}{k}}
$$

Aquest resultat mostra que el període depèn:

- de la **massa del cos**
- de la **constant elàstica de la molla**

però **no depèn de l’amplitud de l’oscil·lació**.

---

### b. Pèndol senzill

Un **pèndol senzill** està format per una massa $m$ suspesa d’un fil de longitud $l$.

| ![Pèndol que es mou amb moviment harmònic simple MHS](img/bloc5/13.png) |
|:--------------------------------------:|
| *Pèndol que es mou amb moviment harmònic simple MHS.* |

Quan el pèndol es separa de la vertical un angle $\theta$, el pes es pot descompondre en dues components:

- component **normal**:  $p_n = mg\cos\theta$
- component **tangencial**:  $p_t = mg\sin\theta$

La component tangencial és la responsable del moviment i actua com una **força restauradora**. Aplicant la segona llei de Newton en direcció tangencial:

$$
F_t = -mg\sin\theta
$$

Si l’angle és petit, es pot fer l’aproximació $\sin\theta \approx \theta$ i, tenint en compte que la longitud d’arc és $s = l\cdot \theta$ i $s \approx x$ s’obté una equació equivalent a la del moviment harmònic simple:

$$
m \cdot -\omega^2 x = -m\cdot g \cdot \frac{x}{l} 
$$

Per tant,

$$
\boxed{\omega = \sqrt{\frac{g}{l}}}
$$

i el **període d’oscil·lació del pèndol** és:

$$
T = 2\pi \sqrt{\frac{l}{g}}
$$

En aquest cas el període depèn:

- de la **longitud del fil**
- de l’**acceleració de la gravetat**

i **no depèn de la massa del cos**.

---

---

## 2.5 — Energia del MHS

El moviment harmònic simple també es pot estudiar des del punt de vista energètic. En el cas d’un sistema **massa–molla**, l’energia mecànica del sistema és la suma de:

---

> *Energia cinètica*

L’energia cinètica del cos és:

$$
E_c=\frac{1}{2}mv^2
$$

Aquesta energia depèn de la velocitat del cos.

- És **màxima a la posició d’equilibri**, on la velocitat és màxima.
- És **nul·la als punts extrems**, on la velocitat és zero.

---

> *Energia potencial elàstica*

L’energia potencial associada a la molla és:

$$
E_p=\frac{1}{2}kx^2
$$

Aquesta energia depèn de l’elongació de la molla.

- És **màxima als punts extrems** de l’oscil·lació.
- És **nul·la a la posició d’equilibri**.

---

> *Conservació de l’energia mecànica*

Com que la força elàstica és una **força conservativa**, l’energia mecànica del sistema es manté constant:

$$
E = E_c + E_p
$$

Substituint les expressions de l’energia:

$$
E = \frac{1}{2}mv^2 + \frac{1}{2}kx^2
$$

El valor de l’energia mecànica és el mateix en qualsevol punt del moviment.

---

> *Interpretació del moviment*

Durant l’oscil·lació es produeix una transformació contínua entre energia cinètica i energia potencial:

- **a la posició d’equilibri**

$$
E_p = 0, \quad E_c = E_m = \frac{1}{2} m (A\omega)^2
$$

- **als punts extrems**

$$
E_c = 0, \quad E_p = E_m = \frac{1}{2}kA^2
$$

Així, l’energia del sistema es transforma constantment entre **energia cinètica i energia potencial**, mentre que la **energia mecànica total es conserva**.

$$
\frac{1}{2} m (A\omega)^2 = \frac{1}{2}kA^2
$$

Analogament per a un pèndol senzill la $E_{c_{max}} = E_{p_{max}}$:

$$
\frac{1}{2} m v_{max}^2 = mgy_{max}
$$