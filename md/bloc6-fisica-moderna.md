# Bloc 6 — Física relativista, quàntica, nuclear i de partícules

# 1 — La revolució de la física moderna

A finals del segle XIX semblava que la física estava pràcticament completada. La mecànica de Newton descrivia el moviment dels cossos, l’electromagnetisme de Maxwell explicava els fenòmens elèctrics i magnètics, i la termodinàmica permetia entendre les transformacions energètiques.

Molts científics pensaven que només quedaven petits detalls per resoldre. Tanmateix, alguns experiments començaven a mostrar resultats incompatibles amb la física clàssica:

- La **velocitat de la llum** semblava ser constant, independentment del moviment de l’observador (**relativitat**).
- Els **àtoms** no es comportaven com predeien les lleis clàssiques (**catàstrofe ultraviolada**, **espectres atòmics**).
- Alguns materials emetien electrons quan rebien llum (**efecte fotoelèctric**).
- Certs nuclis atòmics es desintegraven espontàniament (**radioactivitat**).

Aquestes contradiccions van evidenciar que la física clàssica tenia limitacions i van conduir al desenvolupament d’una nova física capaç d’explicar fenòmens que fins aquell moment semblaven incomprensibles.

> *El Congrés Solvay de 1927*

![Solvay conference](img/bloc6/1.png)

La imatge anterior correspon al **cinquè Congrés Solvay**, celebrat a Brussel·les l’any **1927**, considerat una de les reunions científiques més importants de la història.

En aquesta fotografia apareixen alguns dels físics que van revolucionar completament la nostra comprensió de l’univers:

- **Albert Einstein**, impulsor de la teoria de la relativitat i de la interpretació quàntica de la llum.
- **Niels Bohr**, fonamental en el desenvolupament del model atòmic.
- **Max Planck**, considerat el pare de la física quàntica.
- **Werner Heisenberg** i **Erwin Schrödinger**, creadors dels primers models matemàtics de la mecànica quàntica.
- **Marie Curie**, pionera en l’estudi de la radioactivitat.
- **Paul Dirac**, que connectaria relativitat i mecànica quàntica.

En total, a la fotografia hi apareixen **17 premis Nobel**, una concentració extraordinària de talent científic.

El tema central del congrés era una gran pregunta:

> **Com funcionen realment la matèria i la llum a escala microscòpica?**

D’aquest debat naixeria el que avui coneixem com a **física moderna**, formada principalment per tres grans blocs:

1. **La física relativista**, que descriu objectes que es mouen a velocitats molt elevades.
2. **La física quàntica**, que explica el comportament de la matèria i la radiació a escala microscòpica.
3. **La física nuclear i de partícules**, dedicada a l’estudi del nucli atòmic, la radioactivitat i les interaccions fonamentals de la matèria.

![Física classica vs física moderna](img/bloc6/2.png)

En aquest tema seguirem el mateix camí que van seguir aquests científics: primer veurem **per què la física clàssica falla en determinades situacions**, i després introduirem els nous models que permeten explicar aquests fenòmens.

Per entendre millor el context històric de la física moderna, el debat entre relativitat i mecànica quàntica, i el paper de científics com Einstein, Bohr, Heisenberg o Dirac, es recomana aquest vídeo de Veritasium:

> *The Equation That Predicted Antimatter — Veritasium*

[![The Equation That Predicted Antimatter](https://img.youtube.com/vi/Y-W-w8yNiKU/maxresdefault.jpg)](https://www.youtube.com/watch?v=Y-W-w8yNiKU)


**No cal entendre tota la part matemàtica del vídeo**, ja que tracta conceptes molt més avançats dels que entren a les PAU. L’objectiu és entendre el **context històric i científic** del naixement de la física moderna i les dificultats que van portar al desenvolupament de la relativitat, la física quàntica i la física de partícules.

---

# 2 — Física quàntica

La física clàssica descriu correctament molts fenòmens macroscòpics, però a escala microscòpica apareixen comportaments que no es poden explicar amb els models tradicionals.

A principis del segle XX, diversos experiments van mostrar que la llum i la matèria no es comportaven exactament com predeia la física clàssica. Aquestes contradiccions van donar lloc al desenvolupament de la **física quàntica**, una nova teoria capaç d’explicar el comportament de la matèria i la radiació a escala atòmica.

En aquest apartat estudiarem tres idees fonamentals de la física quàntica:

1. La **quantificació de l’energia** proposada per Planck.
2. L’**efecte fotoelèctric**, explicat per Einstein.
3. La **dualitat ona-corpuscle**, introduïda per De Broglie.

---

## 2.1 — Hipòtesi de Planck: la quantificació de l’energia

La física clàssica considerava que la llum podia intercanviar energia de forma contínua. Tanmateix, alguns experiments mostraven comportaments incompatibles amb aquesta idea. Per explicar-los, el físic **Max Planck** va proposar una idea revolucionària:

> L'energia associada a una radiació electromagnètica d'una determinada freqüència només pot tenir valors que són múltiples d'un quantum elemental (en la llum és el fotó) que és proporcional a la freqüència de la radiació.

$$
E = h·f
$$

on:

- $E$: energia del fotó (J)
- $h$: constant de Planck $h = 6,63 \times 10^{-34}\ \text{J·s}$
- $f$: freqüència de la radiació (Hz)

Com que la freqüència i la longitud d’ona estan relacionades per l’expressió:

$$
f=\frac{c}{\lambda}
$$

també podem expressar l’energia d’un fotó com:

$$
E=\frac{hc}{\lambda}
$$

on:

- $c = 3,0 \times 10^8\ \text{m/s}$ és la velocitat de la llum al buit.
- $\lambda$ és la longitud d’ona de la radiació.

La llum no transporta energia de forma contínua, sinó en **petits paquets d’energia anomenats fotons**.

Això implica que:

- **més freqüència → més energia**
- **menys longitud d’ona → més energia**

| ![Diagrama de l'espectre electromagnètic.](img/bloc6/8.png) |
|:--------------------------------------:|
| *Diagrama de l'espectre electromagnètic.* |

La intensitat de la llum indica **quants fotons arriben**, però no l’energia de cada fotó. En física quàntica és habitual expressar energies en **electró-volts (eV)**:

$$
1\ \text{eV}=1,6\times10^{-19}\ \text{J}
$$

L’eV és l’energia que guanya un electró quan travessa una diferència de potencial d’1 volt.

---

## 2.2 — L’efecte fotoelèctric

La teoria ondulatòria de la llum predeia que l’energia transportada depenia únicament de la **intensitat** de la radiació.

> *Segons la física clàssica*

- una llum molt intensa sempre hauria d’arrencar electrons d’un metall;
- qualsevol freqüència de llum hauria de funcionar si s’espera prou temps;
- els electrons haurien de guanyar energia progressivament.

Tanmateix, els experiments mostraven un comportament completament diferent.

> *Què s’observa experimentalment?*

Quan s’il·lumina una placa metàl·lica amb radiació electromagnètica:

- només s’emeten electrons si la freqüència de la llum supera un valor mínim;
- l’emissió és **instantània**;
- l’energia dels electrons depèn de la **freqüència**, no de la intensitat.

Aquest fenomen rep el nom d’**efecte fotoelèctric**.

> *La interpretació d’Einstein*

Per explicar aquest fenomen, **Albert Einstein** va proposar que la llum està formada per **fotons**, cadascun amb energia:

$$
E = hf
$$

Quan un fotó impacta sobre un electró del metall, li transfereix tota la seva energia.

Aquesta energia es reparteix de la manera següent:

- una part s’utilitza per arrencar l’electró del metall;
- la resta es transforma en energia cinètica de l’electró emès.

Això es resumeix en el **balanç energètic de l’efecte fotoelèctric**:

$$
E_{fotó} = W_0 + E_c
$$

on:

- $E_{fotó}$: energia del fotó incident.
- $W_0$: **treball d’extracció** (energia mínima necessària per arrencar un electró).
- $E_c$: energia cinètica màxima de l’electró emès.

Com que:

$$
E_{fotó}=hf=\frac{hc}{\lambda}
$$

també podem escriure:

$$
hf = W_0 + E_c
$$

> *La freqüència llindar*

Cada metall necessita una energia mínima per arrencar electrons. Per això existeix una **freqüència llindar** $f_0$:

- Si $f<f_0$ → **no hi ha emissió d’electrons**.
- Si $f>f_0$ → sí que hi ha efecte fotoelèctric.

La freqüència llindar compleix:

$$
W_0 = h f_0
$$

o equivalentment:

$$
\lambda_0=\frac{c}{f_0}
$$

> *Concepte clau*

La intensitat de la llum indica **quants fotons arriben**, però:

> **l’energia de cada electró depèn només de la freqüència de la llum.**

Per això:

- **llum més energètica (freqüència alta)** → electrons més ràpids;
- **llum més intensa** → més electrons emesos.

---

## 2.3 — La dualitat ona-corpuscle

La radiació electromagnètica té propietats ondulatòries (reflexió, refracció, interferència, etc.), però de vegades presenta propietats corpusculars, com és el cas de la interacció amb la matèria (efecte fotoelèctric), De Broglie va estendre a totes les partícules la dualitat ona-corpuscle.

> *hipòtesi de De Broglie*

Segons De Broglie, qualsevol partícula en moviment té associada una longitud d’ona anomenada **longitud d’ona de De Broglie**:

$$
\lambda = \frac{h}{p} = \frac{h}{m·v}
$$

on:

- $\lambda$: longitud d’ona associada a la partícula (m)
- $h = 6,63 \times 10^{-34}\ \text{J·s}$: constant de Planck
- $m$: massa de la partícula (kg)
- $v$: velocitat de la partícula (m/s)

> *Interpretació física*

La longitud d’ona associada a la matèria és molt petita per objectes macroscòpics.

Per exemple:

- una pilota → longitud d’ona pràcticament nul·la;
- un electró → longitud d’ona apreciable.

Per això els efectes ondulatoris de la matèria només són observables a **escala microscòpica**.

---

# 3 — Física nuclear

## 3.1 — Composició dels nuclis atòmics

L’àtom està format per:

- un **nucli central**, on es concentra pràcticament tota la massa;
- una **escorça electrònica**, formada per electrons.

El **nucli atòmic** està format per dues partícules:

- **protons** → tenen càrrega positiva;
- **neutrons** → no tenen càrrega elèctrica.

Els protons i els neutrons reben el nom de **nucleons**.

| ![Partícules constituents de l’àtom i el seu nucli.](img/bloc6/3.png) |
|:--------------------------------------:|
| *Partícules constituents de l’àtom i el seu nucli.* |

| Partícula | Símbol | Càrrega | Situació |
|-----------|---------|----------|-----------|
| Protó | $p$ | $+1$ | Nucli |
| Neutró | $n$ | $0$ | Nucli |
| Electró | $e^-$ | $-1$ | Escorça |

> *Notació nuclear*

Els nuclis es representen mitjançant la notació:

$$
{}^A_ZX
$$

on:

- $X$: símbol químic de l’element
- $Z$: És el **nombre de protons** del nucli. El nombre de protons determina l’element químic.
- $A$: És el nombre total de nucleons (protons + neutrons), per tant:

$$
A = Z + N
$$

| ![Notació nuclear.](img/bloc6/4.png) |
|:--------------------------------------:|
| *Notació nuclear.* |

> *Partícules elementals*

| ![Model estàndard de les partícules elementals.](img/bloc6/5.png) |
|:--------------------------------------:|
| *Model estàndard de les partícules elementals.* |

> *Isòtops*

Els **isòtops** són àtoms del mateix element químic que tenen:

> **el mateix nombre de protons $Z$ però diferent nombre de neutrons $N$.**

Per tant:

- tenen propietats químiques semblants,
- però poden tenir estabilitat nuclear diferent.

Per exemple, els isòtops de l’hidrogen:

$$
{}^1H,\ {}^2H,\ {}^3H
$$

## 3.2 — Estabilitat nuclear

> **Si els protons tenen càrrega positiva i es repel·leixen elèctricament, per què el nucli no es desintegra?**

El nucli es manté unit gràcies a una altra interacció fonamental: la **força nuclear forta**.

Aquesta força:

- actua entre **protons i neutrons** (nucleons),
- és **molt més intensa** que la repulsió elèctrica,
- té un **abast molt curt**, limitat a dimensions comparables a la mida del nucli atòmic.

La força nuclear forta és atractiva i permet mantenir units els nucleons malgrat la repulsió elèctrica entre protons. Per això els nuclis atòmics poden existir i ser estables.
uan aquest equilibri és adequat, el nucli és **estable**. Però si la repulsió elèctrica esdevé massa gran o hi ha un desequilibri entre protons i neutrons, el nucli pot tornar-se **inestable**.

Tanmateix, a mesura que augmenta el nombre de nucleons:

- hi ha més protons repel·lint-se;
- la repulsió electrostàtica augmenta;
- la força nuclear forta no creix igual, perquè només actua a distàncies molt petites.

Per aquest motiu:

> **Els nuclis molt grans tendeixen a ser menys estables.**

## 3.3 — Radioactivitat natural

> La **radioactivitat** és el procés pel qual un nucli atòmic inestable es transforma espontàniament en un altre nucli més estable mitjançant l’emissió de radiació.

Aquest fenomen té diverses característiques importants:

- és **espontani**, no cal provocar-lo;
- és **aleatori**, no podem predir quan es desintegrarà un nucli concret;
- és independent de factors externs com:
  - temperatura,
  - pressió,
  - estat químic.

Per tant:

> **No podem saber quan es desintegrarà un nucli individual, però sí predir el comportament estadístic d’un gran nombre de nuclis.**

Aquest comportament estadístic ens permetrà definir posteriorment conceptes com:

- **semivida**
- **constant radioactiva**
- **activitat radioactiva**

### a) Les reaccions nuclears

Les transformacions radioactives s’expressen mitjançant **reaccions nuclears**. En qualsevol reacció nuclear es compleixen dues lleis de conservació molt importants:

- **La suma dels nombres màssics $A$ es conserva.**
- **La suma dels nombres atòmics $Z$ es conserva.**

Aquest principi és fonamental per completar correctament les reaccions nuclears.

### b) Tipus principals de radiacions

> *Radiació alfa $\alpha$*

Es produeix quan una àtom emet una particula $\alpha$ (nucli de He):

$$
{}^{238}\_{92}\text{U} \rightarrow {}^{234}\_{90}\text{Th}+{}^{4}\_{2}\text{He}
$$

| ![Esquema d’un procés de desintegració per emissió d’una partícula α.](img/bloc6/6.png) |
|:--------------------------------------:|
| *Esquema d’un procés de desintegració per emissió d’una partícula α.* |

---

> *Radiació $\beta^-$*

En aquesta desintegració **un neutró es transforma en un protó** emetent un electró ${}^{1}\_{0}n^0 \rightarrow {}^{1}\_{1}p + {}^0\_{-1}e + {}^0\_{0}\bar{\nu}$

$$
{}^{14}\_{6}C \rightarrow {}^{14}\_{7}N + {}^0\_{-1}e + {}^0\_{0}\bar{\nu}
$$

---

> *Radiació $\beta^+$*

En aquest cas **un protó es transforma en un neutró** emetent un positró ${}^{1}\_{1}p^+ \rightarrow {}^{1}\_{0}n + {}^0\_{1}e + {}^0\_{0}\nu$

$$
{}^{22}\_{11}Na \rightarrow {}^{22}\_{10}Ne + {}^0\_{+1}e + {}^0\_{0}\nu
$$

| ![Esquema d’un procés de desintegració per emissió d’una partícula β.](img/bloc6/7.png) |
|:--------------------------------------:|
| *Esquema d’un procés de desintegració per emissió d’una partícula β.* |

---

> *Radiació gamma $\gamma$*

La radiació gamma consisteix en l’emissió de **radiació electromagnètica molt energètica**. No implica expulsió de nucleons.

Per tant:

- el nombre màssic **no canvia**;
- el nombre atòmic **no canvia**.

La radiació gamma acostuma a produir-se després d’una desintegració alfa o beta, quan el nucli encara es troba en un estat energètic excitat per retornar al estat fonamental.

$$
{}^{60}\_{27}Co^* \rightarrow {}^{60}\_{27}Co + \gamma
$$

---

## 3.4 — Llei de desintegració radioactiva

La velocitat de desintegració d'ina mostra radioactiva no és constant amb el temps, sinó que la seva variació és de manera **exponencial** i segueix la llei següent:

$$
N=N_0e^{-\lambda t}
$$

Aquesta expressió mostra que:

> **La quantitat de material radioactiu disminueix exponencialment amb el temps.**

on:

- $N$: nombre de nuclis que queden després d’un temps $t$
- $N_0$: nombre inicial de nuclis
- $t$: temps transcorregut
- $\lambda$: constant radioactiva de desintegració (unitats $s^{-1}$)

Aquesta constant representa la **probabilitat de desintegració** d’un nucli per unitat de temps.

Per tant:

- valor gran de $\lambda$ → nucli molt inestable;
- valor petit de $\lambda$ → nucli més estable.

> *La semivida o període de semidesintegració*

> Mesura **el temps necessari perquè es desintegri la meitat dels nuclis d’una mostra radioactiva.**

La semivida i la constant radioactiva estan relacionades per:

$$
T_{1/2}=\frac{\ln 2}{\lambda}
$$

Si una substància té $T_{1/2}=10\ \text{anys}$ llavors:

| Temps | Quantitat restant |
|--------|-------------------|
| 0 anys | 100 % |
| 10 anys | 50 % |
| 20 anys | 25 % |
| 30 anys | 12,5 % |

---

## 3.5 — Activitat radioactiva

> L’activitat d’una mostra radioactiva, A, es defineix com el nombre de desintegracions que es donen per unitat de temps, de manera que representa la velocitat de desintegració.

$$
A=-\frac{dN}{dt} = \lambda N = A_0 e^{-\lambda t} = A_0\left(\frac12\right)^{t/T_{1/2}}
$$

on:

- $A$: activitat radioactiva
- $A_0$: Activitat inicial $A_0 = \lambda N_0$
- $N$: nombre de nuclis radioactius
- $\lambda$: constant radioactiva

El signe negatiu indica que:

> **el nombre de nuclis disminueix amb el temps.**

> *Unitat de l’activitat: el becquerel (Bq)*

La unitat de l’activitat radioactiva en el Sistema Internacional és el **becquerel (Bq)**

$$
1\ \text{Bq}=1\ \text{desintegració/s} = s^{-1}
$$

És a dir:

> **Una activitat d’1 Bq significa que es produeix una desintegració cada segon.**

Algunes vegades es fa servir també el Curie(Ci) : $ 1 Ci = 3,7·10^{10} Bq$

---

## 3.6 — Energia nuclear

Podríem pensar que la massa d’un nucli és exactament igual a la suma de les masses dels seus protons i neutrons. Tanmateix, experimentalment s’observa que:

> **La massa real del nucli és lleugerament inferior a la suma de les masses dels nucleons separats.**

Aquesta diferència rep el nom de **defecte de massa**:

$$
\Delta m = \sum m_{nucleons} - m_{nucli}
$$

La massa “desapareguda” s’ha transformat en energia que segons la teoria de la relativitat d’Einstein:

$$
E=\Delta m · c^2
$$

on:

- $E$: energia alliberada o absorbida (J)
- $\Delta m$: defecte de massa (kg)
- $c$: velocitat de la llum

Aquesta expressió mostra que:

> **Una petita quantitat de massa pot transformar-se en una enorme quantitat d’energia.**

Això explica l’elevada energia alliberada en les reaccions nuclears.

---

> *Energia d’enllaç nuclear*

L’energia associada a la unió dels nucleons rep el nom d’**energia d’enllaç nuclear**. Es defineix com:

> l’energia necessària per separar completament tots els nucleons d’un nucli o és l’energia alliberada quan el nucli es forma.

Com més gran és l’energia d’enllaç **més estable és el nucli.**

---

> *Energia d’enllaç per nucleó*

Per comparar l’estabilitat de diferents nuclis es fa servir la **energia d’enllaç per nucleó**:

$$
\frac{E}{A}
$$

on:

- $E$: energia d’enllaç total
- $A$: nombre de nucleons

Experimentalment s’observa que:

> **Els nuclis més estables tenen una energia d’enllaç per nucleó més elevada.**

---

## 3.7 — Fissió i fusió nuclear

Hem vist que les reaccions nuclears poden alliberar grans quantitats d’energia quan es produeix un defecte de massa. Aquesta energia es pot obtenir principalment de dues maneres:

> **En la fissió, un nucli pesant es trenca.**

> **En la fusió, dos nuclis lleugers s’uneixen.**

---

### a) Fissió nuclear

La **fissió nuclear** consisteix en la ruptura d’un **nucli pesant** en dos nuclis més petits. Aquest procés acostuma a iniciar-se quan el nucli captura un neutró.

| ![Esquema d’una reacció de fissió nuclear.](img/bloc6/9.png) |
|:--------------------------------------:|
| *Esquema simplificat d’una reacció de fissió nuclear.* |

En aquest procés:

- es formen nuclis més estables;
- es produeix un **defecte de massa**;
- part de la massa es transforma en energia.

Els neutrons produïts poden provocar noves fissions:

> **reacció en cadena**

Aquest principi és el que utilitzen:

- les **centrals nuclears**;
- les **bombes de fissió**.


### b) Fusió nuclear

La **fusió nuclear** consisteix en la unió de **nuclis lleugers** per formar un nucli més pesant.

| ![Esquema d’una reacció de fusió nuclear.](img/bloc6/10.png) |
|:--------------------------------------:|
| *Esquema simplificat d’una reacció de fusió nuclear.* |

Perquè es produeixi la fusió cal:

> **temperatures extremadament elevades**

que permetin superar la repulsió elèctrica entre nuclis positius.

Aquest procés és el responsable de l’energia emesa:

- pel **Sol**;
- per les **estrelles**.

---

# 4 — Teoria de la relativitat