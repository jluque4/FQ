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

---

# 3 — Moviment ondulatori

## 3.1 — Concepte d'ona

Una **ona** és una **pertorbació que es propaga en l’espai i en el temps**, transportant energia però **sense transport de matèria**.

| ![Ones generades en una corda](img/bloc5/15.png) |
|:-----------------------------------:|
| *Ones generades en una corda.* | 

En un moviment ondulatori:

- els punts del medi **oscil·len al voltant d’una posició d’equilibri**
- aquesta oscil·lació **es transmet als punts veïns**
- l’energia es propaga, però les partícules del medi **no es desplacen globalment**

---

### a. Classificació de les ones

> *Classificació de les ones segons les dimensions de propagació*

- **Ones unidimensionals:** que són les ones que es propaguen en una única direcció, és a dir, en una dimensió. 
- **Ones bidimensionals:** que són les ones que es propaguen en un pla, és a dir, en dues dimensions.
- **Ones tridimensionals:** que són les ones que es propaguen en l’espai, és a dir, en tres dimensions. 

| ![Ones generades en una corda](img/bloc5/17.png) | ![Ones generades en una corda](img/bloc5/18.png) | ![Ones generades en una corda](img/bloc5/19.png) |
|:-----------------------------------:|:-----------------------------------:|:-----------------------------------:|
| *Ones generades en una corda.* | *Ones a la superfície d’un líquid.* | *So produït per un diapasó.* | 

> *Classificació de les ones segons el medi de propagació*

- **Ones mecàniques:**: que són les ones que necessiten un medi per propagar-se. En aquest cas, el que oscil.la al pas de l’ona són les partícules del medi. 
- **Ones electromagnètiques:** que són les ones que no necessiten un medi per transmetre’s i que, per tant, es poden propagar en el buit, tot i que també es propaguen en certs medis.

> *Classificació de les ones en longitudinals i transversals*

- **Ones longitudinals:** que són les ones en les quals la direcció d’oscil.lació de les par­tícules del medi és la mateixa que la direcció de propagació de l’ona.
- **Ones transversals:** que són les ones en les quals la direcció d’oscil.lació de les partícules del medi és perpendicular a la direcció de propagació de l’ona.

| ![Classificació de les ones en longitudinals i transversals](img/bloc5/16.png) |
|:-----------------------------------:|
| *Classificació de les ones en longitudinals i transversals.* | 

---

---

## 3.2 — Ones harmòniques

Una **ona harmònica** és una pertorbació que consisteix en un **moviment harmònic simple (MHS)** que es propaga a través de les particules que formen el medi.

---

### a. Magnituds ondulatòries

> *Longitud d’ona $\lambda$*

És la longitud que hi ha entre dos punts consecutius que es troben en el mateix estat de vibració, és a dir, que es troben en la mateixa fase. Es mesura en $m$.

| ![Longitud d’ona $\lambda$](img/bloc5/20.png) |
|:-----------------------------------:|
| *Longitud d’ona $\lambda$.* | 

> *Nombre d'ona $k$*

Indica el nombre de vegades que es repeteix una ona en una longitud igual a 2$\pi$ metres. Es mesura amb $rad/m$.

$$
k = \frac{2\pi}{\lambda}
$$

> *Velocitat de la fase $v$*

La velocitat de propagació de l’ona és:

$$
v = \frac{\lambda}{T} = \lambda \cdot f
$$

També es pot expressar com:

$$
v = \frac{\omega}{k}
$$

### b. Equació d’ona

Si l’ona es propaga amb velocitat $v$, el retard entre dos punts separats una distància $x$ és:

$$
t' = t - \frac{x}{v}
$$

Això significa que el punt en $x$ oscil·la com ho feia el punt origen en un instant anterior. Substituïm aquest retard en l’equació del MHS:

$$
y(x,t)=A\sin\left[\omega\left(t-\frac{x}{v}\right)+\varphi_0\right]
$$

Definim una nova magnitud, anomenada **nombre d’ona $k$**:

$$
k = \frac{\omega}{v}
$$

i obtenim l’equació final d’una ona harmònica que es propaga en una direcció (eix X):

$$
\boxed{y(x,t)=A\sin(\omega t - kx + \varphi_0) = A\sin(\frac{2\pi t}{T} - \frac{2\pi x}{\lambda} + \varphi_0)}
$$


Aquesta expressió descriu:

- la **posició** $y$ d’un punt del medi  
- en funció de la seva posició $x$ 
- i del temps $t$

És una combinació de:

- moviment en el temps → $\omega t $  
- propagació en l’espai → $kx$
- el signe **−** indica que l’ona es desplaça en el sentit positiu de l’eix X

| ![Evolució de l’ona al llarg del temps](img/bloc5/21.png) |
|:-----------------------------------:|
| *Evolució de l’ona al llarg del temps.* | 

---

# 4 — Fenòmens ondulatoris

Quan una ona es propaga per un medi, pot trobar-se amb obstacles, canvis de medi o altres ones. En aquestes situacions, el moviment ondulatori experimenta determinades transformacions que reben el nom de **fenòmens ondulatoris**.

Aquests fenòmens permeten explicar molts comportaments observables de les ones, com ara:

- el rebot d’una ona sobre una superfície,
- el canvi de direcció en passar d’un medi a un altre,
- la superposició de dues ones,
- o la capacitat d’una ona de rodejar obstacles.

> Els fenòmens ondulatoris descriuen el comportament de les ones quan interactuen amb el medi, amb obstacles o amb altres ones.

---

### a. Principi de Huygens

El **principi de Huygens** és un model que permet explicar com es propaguen les ones.

> Cada punt d’un front d’ona es comporta com una font d’ones secundàries.

El nou front d’ona en un instant posterior és l’embolcall (superfície tangent) de totes aquestes ones secundàries.

| ![Principi de Huygens](img/bloc5/30.png) |
|:--------------------------------------:|
| *Construcció del front d’ona segons Huygens.* |

Per estudiar la propagació d’una ona és útil introduir el concepte de **raig**.

> Un **raig** és una línia imaginària que indica la **direcció de propagació de l’ona** i és sempre **perpendicular als fronts d’ona**.

Considerem un **front d'ona** com:

> El front d’ona és el conjunt de punts del medi als quals arriba la pertorbació en un instant de temps determinat.

| ![Raig i front d'ona](img/bloc5/22.png) |
|:--------------------------------------:|
| *Raigs i fronts d’ona en el fenòmen de la refracció.* |

Això ens permet representar de manera senzilla:

- cap a on es propaga l’ona,
- com canvia de direcció,
- i com interacciona amb superfícies o canvis de medi.

---

### b. Reflexió

La **reflexió** és el fenomen ondulatori que es produeix quan una ona arriba a una superfície i **rebota**, canviant la seva direcció de propagació però mantenint-se en el mateix medi.

| ![Reflexió d'una ona](img/bloc5/23.png) |
|:--------------------------------------:|
| *Reflexió d’una ona.* |

---

> *Elements de la reflexió*

- **Raig incident**: raig que arriba a la superfície  
- **Raig reflectit**: raig que surt després del rebot  
- **Normal**: recta perpendicular a la superfície en el punt d’impacte  
- **Angle d’incidència** $ \alpha_i $: angle entre el raig incident i la normal  
- **Angle de reflexió** $ \alpha_r $: angle entre el raig reflectit i la normal  

---

> *Llei de la reflexió*

> L’angle d’incidència és igual a l’angle de reflexió i només canvia la **direcció de propagació** de l'ona.

$$
\boxed{\alpha_i = \alpha_r}
$$

---

> *Tipus de reflexió*

**Reflexió especular** (superfície llisa):

- els raigs reflectits mantenen una direcció ordenada  
- exemple: mirall  

**Reflexió difusa** (superfície rugosa):

- els raigs es dispersen en diferents direccions  
- exemple: paret  

---

---

### c. Refracció

> La **refracció** és el fenomen ondulatori que es produeix quan una ona passa d’un medi a un altre i **canvia la seva direcció de propagació** a causa del canvi de velocitat.

| ![Refracció d'una ona](img/bloc5/24.png) |
|:--------------------------------------:|
| *Reflexió i refracció d’una ona.* |

---

> *Elements de la refracció*

- **Raig incident**: raig que arriba a la superfície de separació  
- **Raig refractat**: raig que entra en el nou medi  
- **Normal**: recta perpendicular a la superfície  
- **Angle d’incidència** $ \alpha_i $ 
- **Angle de refracció** $ \alpha_r\prime $

Quan l’ona canvia de medi:

- la **velocitat** canvia  
- la **longitud d’ona** canvia  
- la **freqüència es manté constant**

---

> *llei de Snell*

$$
\boxed{\frac{\sin \alpha_i}{\sin \alpha_r\prime} = \frac{v_1}{v_2}}
$$

on:

- $v_1$ és la velocitat en el primer medi  
- $v_2$ és la velocitat en el segon medi  

Com que $v = \lambda f$ i la **freqüència es manté constant**:

$$
\frac{\lambda_1}{\lambda_2} = \frac{v_1}{v_2}
$$

- si l’ona entra en un medi **més lent** → es desvia cap a la normal  
- si entra en un medi **més ràpid** → s’allunya de la normal  

---

---

### d. Interferència

> La **interferència** és el fenomen ondulatori que es produeix quan dues o més ones coincideixen en un mateix punt de l’espai.

---

> *Principi de superposició*

Quan dues o més ones es troben, la deformació resultant és la suma de les deformacions individuals:

$$
\sum_i y = y_1 + y_2 + y_3 \text{ ...}
$$

| ![Interferència de dues ones unidimen­sionals d’amplituds i freqüències diferents.](img/bloc5/25.png) |
|:--------------------------------------:|
| *Interferència de dues ones unidimen­sionals.* |


| ![Interferència de dues ones coherents.](img/bloc5/26.png) |
|:--------------------------------------:|
| *Interferència de dues ones coherents.* |

---

> *Tipus d’interferència*

Considerem un punt genèric P, que és a una distància $r_1$ de la font $F_1$, i a una distància $r_2$ de la font $F_2$. Per trobar la funció d’ona resultant, sumem ambdós moviments ondulatoris:

| ![Dues fonts coherents que emeten ones transversals circulars](img/bloc5/27.png) |
|:--------------------------------------:|
| *Dues fonts coherents que emeten ones transversals circulars* |


$$
y = y_1 + y_2 = A_0 sin(ω t − k r_1) + A_0 sin(ω t − k r_2) = A_0 [sin(ω t − k r_1) + sin (ω t − k r_2)] 
$$

aplicant la relació trigonometrica $sin\alpha + sin\beta = 2 \cdot cos[\frac{1}{2} (\alpha - \beta)] \cdot sin[\frac{1}{2} (\alpha + \beta)]$ obtenim:

$$
y = 2A_0 cos[k(\frac{r_2-r_1}{2})] \cdot sin(\omega t - k(\frac{r_2+r_1}{2}))
$$

---

#### a. Interferència constructiva

Es produeix quan les ones arriben en fase. Si recordem que el nombre d’ona k i la longitud d’ona λ estan relacionats:

$$
\Delta r = n\lambda \quad (n = 0,1,2,\ldots)
$$

- les amplituds es **sumen**
- s’obté una **amplitud màxima**

---

#### b. Interferència destructiva

Es produeix quan les ones arriben en oposició de fase.

$$
\Delta r = \left(n+\frac{1}{2}\right)\lambda
$$

- les amplituds es **cancel·len**
- s’obté una **amplitud nul·la**

---

#### c. Interferència parcialment constructiva.

En funció de les distàncies als focus, es produeix una gradació entre la interferència constructiva i la interferència destructiva.

La diferència de camins és:

$$
\Delta r = |r_1 - r_2|
$$

on:

$r_1$ i $r_2$ són les distàncies des de cada focus

---

### e. Efecte Doppler

L’**efecte Doppler** és el fenomen pel qual la **freqüència percebuda d’una ona canvia** quan hi ha moviment relatiu entre la font i l’observador.

| ![Efecte Doppler](img/bloc5/28.png) | ![Efecte Doppler](img/bloc5/29.png) |
|:----------------------------------:|:----------------------------------:|
| *Font emissora d’ones transversals en repòs.* | *Efecte Doppler: compressió i dilatació de les ones.* |

- si la font i l’observador **s’apropen** → la freqüència percebuda **augmenta**  
- si **s’allunyen** → la freqüència percebuda **disminueix**

Quan la font es mou:

- les ones es **comprimeixen** davant seu → $\lambda$ més petita  
- les ones s’**estiren** darrere → $\lambda$ més gran  

per tant, la freqüència percebuda és:

$$
\boxed{f' = f \cdot \frac{v \pm v_o}{v \mp v_f}}
$$

on:

- $ f' $ → freqüència observada  
- $ f $ → freqüència emesa  
- $ v $ → velocitat de l’ona  
- $ v_o $ → velocitat de l’observador  
- $ v_f $ → velocitat de la font  

---

### f. Difracció

La **difracció** és el fenomen pel qual una ona experimenta una distorsió o variació en la direcció de propagació d’una ona quan aquesta troba en la seva transmissió un obstacle que té unes dimensions comparables a la longitud d’ona i que n’impedeix la propagació.

| ![Difracció](img/bloc5/31.png) |
|:-----------------------------:|
| *Difracció d’una ona.* |

---

> La difracció és significativa quan la mida de l’obstacle o de l’obertura és comparable amb la longitud d’ona:

$$
\text{mida} \approx \lambda
$$

---

#### Conseqüències

- les ones poden **rodejar obstacles**  
- poden **penetrar en zones d’ombra geomètrica**  

---

#### Exemples

- el so es pot sentir darrere d’una porta  
- les ones de l’aigua envolten obstacles  
- la llum es difracta en escletxes petites  

---

---

# 5 — Ones estacionàries

Les **ones estacionàries** es formen per la superposició de dues ones **coherents** (mateixa amplitud, longitud d’ona i freqüència) que es propaguen en sentits oposats.

---

| ![Ones estacionàries](img/bloc5/32.png) |
|:-----------------------------:|
| *Ones estacionàries.* |

$$
y = y_i + y_r = A_0 sin(ω t + k x) + (-A_0) sin(ω t − k x) = A_0 [sin(ω t + k x) - sin (ω t − k x)] 
$$

aplicant la relació trigonometrica $sin\alpha - sin\beta = 2 \cdot sin[\frac{1}{2} (\alpha - \beta)] \cdot cos[\frac{1}{2} (\alpha + \beta)]$ obtenim:

$$
\boxed{y(x,t) = 2A_0 sin(k x) \cdot cos(\omega t)}
$$

---

> *Interpretació*

Comparant l'expressió obtinguda amb l'equació del MHS obtenim:

$$
y(x,t) = A(x) \cdot cos(\omega t)
$$

on l'amplitud seria:

$$
A(x) = 2A_0 sin(k x)
$$

A diferència d’una ona progressiva:

- **no hi ha propagació d’energia**
- el patró d’oscil·lació és fix en l’espai

Per això s’anomenen **ones estacionàries**.

---

> *Nodes i ventres*

#### Nodes

Són punts on l’elongació és sempre nul·la:

$$
\sin(kx) = 0
$$

Per tant la posició dels nodes:

$$
\boxed{x = n \cdot \frac{\lambda}{2}} \text{  amb n = 0,1,2...}
$$

#### Ventres (antinodes)

Són punts on l’amplitud és màxima:

$$
\sin(kx) = \pm 1
$$

Per tant la posició dels ventres:

$$
\boxed{x = n \cdot \frac{\lambda}{4}}  \text{  amb n = 1,3,5... es a dir són múltiples imparells}
$$


| ![Nodes i ventres en una ona estacionària.](img/bloc5/33.png) |
|:-----------------------------:|
| *Nodes i ventres en una ona estacionària.* |

---

### a. Modes de vibració d’una corda amb extrems fixos

Suposem ara que la corda està fixada pels seus dos extrems i sigui L la seva longitud, com que els extrems fixos es comporten com a **nodes** tenim:

$$
L = n \cdot \frac{\lambda}{2} \rightarrow \lambda_n = \frac{2L}{n} \text{  amb n = 1,2,3...}
$$

| ![Ones estacionàries produïdes en una corda fixa pels seus extrems](img/bloc5/34.png) |
|:-----------------------------:|
| *Ones estacionàries produïdes en una corda fixa pels seus extrems.* |

---

### b. Modes de vibració d’una corda amb un extrem fix i un extrem lliure

Considerem ara el cas d’una corda que té un extrem fix i l’altre lliure a una distància L, l'extrem fixe es comportarà com un **node** i l'extrem lliure com un **ventre**:

$$
L = n \cdot \frac{\lambda}{4} \rightarrow \lambda_n = \frac{4L}{n} \text{  amb n = 1,3,5...}
$$

| ![Ones estacionàries produïdes en una corda amb un extrem fix i un extrem lliure](img/bloc5/35.png) |
|:-----------------------------:|
| *Ones estacionàries produïdes en una corda amb un extrem fix i un extrem lliure.* |

Nota:
> Aquesta situació també es dona en el cas de les ones sonores produïdes en una columna d’aire que vibra i que està confinada en un tub

---

### c. Modes de vibració en una columna d’aire amb extrems lliures

Es pot demostrar que aquest cas és anàleg al d'una corda fixada pels seus dos extrems però intercanviant els nodes pels ventres.

$$
L = n \cdot \frac{\lambda}{2} \rightarrow \lambda_n = \frac{2L}{n} \text{  amb n = 1,2,3...}
$$

| ![Modes de vibració en una columna d’aire amb extrems lliures](img/bloc5/36.png) |
|:-----------------------------:|
| *Modes de vibració en una columna d’aire amb extrems lliures.* |

---

# 6 — Ones sonores

## 6.1 — Intensitat sonora

> *El so transporta energia*

Una ona sonora transporta energia des del focus fins al medi que l’envolta. A mesura que ens allunyem del focus, aquesta energia es reparteix sobre superfícies cada vegada més grans i el so es va debilitant.

---

> *Intensitat sonora*

La intensitat sonora és la potència transmesa per unitat de superfície perpendicular a la direcció de propagació:

$$
I=\frac{P}{S}
$$

on:

- $I$ → intensitat sonora $(W/m^2)$
- $P$ → potència de la font $(W)$
- $S$ → superfície

---

> *So esfèric*

En una ona sonora esfèrica:

$$
S=4\pi r^2
$$

i, per tant:

$$
\boxed{I=\frac{P}{4\pi r^2}}
$$

---

> La intensitat disminueix amb el quadrat de la distància:

$$
I\propto \frac{1}{r^2}
$$

$$
\frac{I_1}{I_2} = \frac{A_1^2}{A_2^2} = \frac{r_1^2}{r_2^2}
$$

---

## 6.2 — El decibel

L’oïda humana pot detectar sons molt febles i molt intensos. Per això s’utilitza una escala logarítmica anomenada **nivell sonor** o **nivell d’intensitat sonora**, mesurada en decibels (dB).

$$
\boxed{\beta=10\log\left(\frac{I}{I_0}\right)}
$$

on:

- $\beta$ → nivell sonor (dB)
- $I$ → intensitat sonora
- $I_0=10^{-12}\,W/m^2$ → llindar d’audició

---

> El decibel no mesura energia directament, sinó una comparació logarítmica respecte del llindar d’audició.

---

# 7 — Òptica

## 7.1 — Naturalesa de la llum

La **llum** és una **ona electromagnètica**, formada per dos camps que varien en el temps i en l’espai seguint un **moviment harmònic simple** de manera que el camp elèctric $\vec{E}$ i el camp magnètic $\vec{B}$ de l’ona estan en fase i són perpendiculars entre si, i també són perpendiculars a la direcció de propagació de l'ona, representada per $\vec{c}$ és a dir, aquestes ones són transversals:

$$
\vec{E}(x,t)=E_0 \sin(\omega t - kx) \cdot \vec{j}
$$

$$
\vec{B}(x,t)=B_0 \sin(\omega t - kx) \cdot \vec{k}
$$

$$
\vec{c} = c \cdot \vec{i}
$$

| ![Ona electromagnètica](img/bloc5/37.png) |
|:-----------------------------:|
| *Ona electromagnètica.* |

La velocitat de propagació en el buit és:

$$
c = 3 \cdot 10^8 \text{m/s}
$$

i compleix:

$$
c = \lambda f
$$

> La llum és una ona formada per camps $E$ i $B$ que oscil·len harmònicament i es propaguen en el buit.


---

## 7.2 — Òptica geomètrica

### a. Sistema òptic

> *Distància focal*

- La **distància focal** és la distància entre el centre òptic i el focus del sistema (lent o mirall)

---

> *Posició de l’objecte i de la imatge*

- $s$: distància de l’objecte al centre òptic  
- $s'$: distància de la imatge al centre òptic  

---

> ***criteri DIN** — Sistema de referència*

Es defineix un sistema de coordenades cartesianes amb:

- origen al centre òptic  
- eix principal horitzontal  
- la llum es propaga d’esquerra a dreta  

#### Conveni de signes

- cap a la dreta → positiu  
- cap a l’esquerra → negatiu  
- cap amunt → positiu  
- cap avall → negatiu  

| ![Sistema òptic](img/bloc5/38.png) |
|:-----------------------------:|
| *Sistema òptic.* |

---

> *Interpretació*

- $s < 0$ → objecte real situat abans del sistema òptic, al costat d’on ve la llum.
- $s' > 0$ → imatge situada a la dreta del sistema.
- $s' < 0$ → imatge situada a l’esquerra del sistema.

*Interpretació física*

- **Imatge real** → els raigs es tallen realment.
- **Imatge virtual** → només es tallen les prolongacions dels raigs.

---

> Les distàncies en òptica es mesuren sempre respecte del centre òptic i amb un conveni de signes.

---

### B. Augment lateral ($\beta$)

L’augment lateral mesura la relació entre la mida de la imatge i la de l’objecte:

$$
\beta = \frac{y'}{y}
$$

on:

- $y'$ → mida de la imatge  
- $y$ → mida de l’objecte  

#### Interpretació

- $\beta > 0$ → imatge dreta  
- $\beta < 0$ → imatge invertida 
- $\beta > 1$ → imatge més gran que l'objecte  
- $\beta < 1$ → imatge més petita que l'objecte    

---

### c. Potència d’una lent

La potència d’una lent es defineix com:

$$
P = \frac{1}{f}
$$

on:

- $f$ → distància focal (en metres)  
- $P$ → potència (en diòptries)

---

### d. Sistemes òptics: miralls i lents

> *Elements d’un sistema òptic*

- **Vertex (V)**: centre de la lent o del mirall 
- **Centre de curvatura (C)**: És el centre de l'esfera que genera el mirall
- **Radi de curvatura (R)**: És la distància des del centre de curvatura (C) fins al vèrtex del mirall (V)
- **Eix principal**: recta horitzontal que passa pel centre  
- **Focus objecte (F)**: punt tal que els raigs que en proven es transformen en paral·lels a l’eix  
- **Focus imatge (F')**: punt on convergeixen els raigs paral·lels (o les seves prolongacions)  
- **Distància focal (f)**: distància entre el focus i el centre òptic  

> *Sistema de rajos*

- El **raig paral.lel** a l’eix òptic, que, d’acord amb la definició de focus, passa per F.
- El **raig focal**, definit com aquell que passa pel focus F, i que, d’acord amb aquesta definició, es reflecteix paral.lelament a l’eix òptic.
- El **raig radial** que passa pel centre de curvatura; aquest raig es reflecteix perpendicularment a la superfície del mirall i, per tant, coincideix amb el raig reflectit.

---

> Tots els sistemes òptics es resolen amb el mateix model de raigs i la mateixa equació; només canvien els signes.

### d. Taula resum d’òptica geomètrica

| Sistema            | Focus objecte | Focus imatge | Equació general           | Augment lateral |
|--------------------| -----| -------|------------------------------------------|-----------------|
| **Mirall pla**     | $ s' = -s $ | $ f' = \infty $ | $ s' = -s $              | $ \beta = 1 $ |
| **Mirall esfèric** | $ f = \frac{R}{2} $ | $ f' = \frac{R}{2} $ | $ \frac{1}{f} = \frac{1}{s} + \frac{1}{s'} $ | $ \beta = -\frac{s'}{s} $ |
| **Lent**           | $P = \frac{1}{f}$ | $P = \frac{1}{f'}$ | $ \frac{1}{f} = \frac{1}{s'} - \frac{1}{s} $ | $ \beta = \frac{s'}{s} $ |

---

> *Miralls*

| ![Mirall convex](img/bloc5/42.png) | ![Mirall concau](img/bloc5/39.png)|
|:-----------------------------:|:-----------------------------:|
| *Mirall convex.* |  *Mirall concau.* |

| ![Mirall convex](img/bloc5/43.png) | ![Mirall concau](img/bloc5/44.png)| ![Mirall concau](img/bloc5/46.png)|
|:-----------------------------:|:-----------------------------:| :-----------------------------:|
| *Mirall convex.* |  *Mirall concau.* |  *Mirall concau.* |

> *Lents*

| ![Lent biconvexa](img/bloc5/40.png) | ![Lent bicòncava](img/bloc5/41.png) |
|:-----------------------------:|:-----------------------------:|
| *Lent biconvexa.* |  *Lent bicòncava.* |

| ![Lent biconvexa](img/bloc5/45.png) |
|:-----------------------------:|
| *Lent biconvexa.* |

---