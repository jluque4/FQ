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

