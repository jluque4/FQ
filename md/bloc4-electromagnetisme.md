# Bloc 4 — Electromagnetisme

---

## 1 — Electricitat i magnetisme

En la situació més general, una càrrega elèctrica pot trobar-se simultàniament en presència d’un camp elèctric i d’un camp magnètic.

En aquest cas, la càrrega experimenta dues accions:
- una força deguda al camp elèctric,
- una força deguda al camp magnètic (si està en moviment).

La força total és la **suma de totes dues contribucions**.

---

## 2 — Llei de Lorentz

La força total que experimenta una càrrega elèctrica $q$ que es mou amb velocitat $\vec v$ en presència d’un camp elèctric $\vec E$ i d’un camp magnètic $\vec B$ ve donada per la **llei de Lorentz**:

$$
\vec F = q\cdot \vec E + q\cdot \vec v \times \vec B
$$

Aquesta expressió rep el nom de **força electromagnètica** o **força de Lorentz**.

**Interpretació**

- el terme $q\cdot \vec E$ correspon a la **força elèctrica**,
- el terme $q\cdot \vec v \times \vec B$ correspon a la **força magnètica**.

Aquesta llei recull tots els casos estudiats:

- si $\vec B = 0$ → només hi ha força elèctrica,
- si $\vec E = 0$ → només hi ha força magnètica,
- si $\vec E \neq 0$ i $\vec B \neq 0$ → acció electromagnètica completa.

---

## 3 — Aplicacions de l’electromagnetisme

---

En situacions reals, una càrrega elèctrica pot trobar-se **simultàniament** sotmesa a un **camp elèctric** i a un **camp magnètic**.
En aquest cas, el seu moviment ve determinat per la **força electromagnètica**, descrita per la **llei de Lorentz**.

---

### a. Selector de velocitats

El **selector de velocitats** és un dispositiu que permet **seleccionar partícules carregades amb una velocitat concreta**, descartant totes les altres.

| ![Selector de velocitats](img/bloc4/60.png) | 
|:--------------------------------------:|
| *En variar la tensió de la font, podem seleccionar ions amb velocitats determinades.* |

> *Funcionament físic*

* Les partícules entren en una regió on hi ha:

  * un **camp elèctric uniforme** $\vec E$
  * un **camp magnètic uniforme** $\vec B$
* els camps són **perpendiculars entre si** i també perpendiculars a la velocitat de les partícules.

Sobre cada partícula actuen dues forces:

* **força elèctrica**: $F_e = qE$
* **força magnètica**: $F_m = qvB$

Només les partícules per a les quals aquestes dues forces **s’anul·len** poden seguir una trajectòria rectilínia.

$$
qE = qvB
$$

D’aquí s’obté la **velocitat seleccionada**:

$$
\boxed{v = \frac{E}{B}}
$$

> El selector de velocitats utilitza l’acció conjunta dels camps elèctric i magnètic per seleccionar partícules amb una velocitat determinada.

---

### b. Espectròmetre de masses

L’**espectròmetre de masses** permet determinar la **relació càrrega-massa** d’un ió o distingir **isòtops** d’un mateix element.

| ![Espectròmetre de masses](img/bloc4/61.png) | 
|:--------------------------------------:|
| *Esquema d'un espectròmetre de masses.* |

> *Funcionament físic*

Consta de dues parts:

1. un **selector de velocitats**, que garanteix que totes les partícules entrin amb la mateixa velocitat,
2. una regió amb **camp magnètic uniforme**, on les partícules descriuen trajectòries circulars.

En aquesta segona regió:

* només actua la **força magnètica**,
* aquesta força fa de **força centrípeta**.

$$
qvB = \frac{mv^2}{r}
$$

Mesurant el radi, es pot determinar la relació $\frac{q}{m}$:

$$
\frac{q}{m} = \frac{v}{rB}
$$

**Idea clau**

> L’espectròmetre de masses combina el selector de velocitats amb el moviment circular en un camp magnètic per separar partícules segons la seva massa.

---

### c. Ciclotró

El **ciclotró** és un **accelerador de partícules** que utilitza camps elèctrics i magnètics per augmentar progressivament l’energia de partícules carregades.

| ![Ciclotró](img/bloc4/62.png) | 
|:--------------------------------------:|
| *Esquema d’un ciclotró.* |

> *Funcionament físic*

* Les partícules es mouen dins d’un **camp magnètic uniforme**, que les obliga a descriure trajectòries semicirculars.
* Entre dues regions hi ha un **camp elèctric altern**, que accelera les partícules cada vegada que el travessen.

La força magnètica:

* no fa treball,
* només canvia la **direcció** del moviment.

La força elèctrica:

* fa treball,
* augmenta l’**energia cinètica** de la partícula.

A mesura que augmenta la velocitat:

* el radi de la trajectòria creix,
* la partícula descriu una **espiral cap enfora**.

Si el radi de sortida del ciclotró és $r$, sabem que la velocitat de sortida de la partícula quan assoleix aquest radi és, segons l’expressió que hem obtingut anteriorment:

$$
v = \frac{rqB}{m}
$$

**Idea clau**

> El ciclotró accelera partícules gràcies a l’acció conjunta del camp elèctric (que accelera) i del camp magnètic (que guia la trajectòria).

---

### — Síntesi de les aplicacions

| Dispositiu              | Paper del camp elèctric     | Paper del camp magnètic    |
| ----------------------- | --------------------------- | -------------------------- |
| Selector de velocitats  | Compensa la força magnètica | Desvia les partícules      |
| Espectròmetre de masses | Selecciona la velocitat     | Corba la trajectòria       |
| Ciclotró                | Accelera les partícules     | Manté el moviment circular |

---
