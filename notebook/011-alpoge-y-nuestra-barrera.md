# 011 — La prueba de Alpöge (2026-11-20) y nuestra barrera

**Fecha:** 2026-11-26 · **Estado:** nota de lectura, no resultado propio.

## Qué ha pasado

El 20 de noviembre de 2026, Levent Alpöge (matemático de Anthropic) publicó una nota de
cuatro páginas y una librería Lean con la prueba de la hipótesis de Riemann. El 21 de
noviembre, la Lean FRO y la Mathlib Initiative certificaron la prueba: el enunciado es el de
Mathlib, la librería compila, y varios comprobadores independientes (incluidos `con-leche` y
`con-ron`, con prueba formal de que no aceptan una prueba falsa) validaron la exportación
inerte. La prueba cubre también la GRH para caracteres de Dirichlet. Andrew Sutherland
verificó aparte los cinco teoremas principales.

Escala: ~17 millones de líneas, ~175.000 ficheros. No existe todavía una exposición humana
completa; la comunidad está reduciéndola y un draft de trabajo (Rubinstein, 22-11) reconstruye
el esqueleto analítico para ζ(s).

## Cómo funciona, en corto

1. **Vía de los primos, no de los ceros.** La prueba no usa estadística de ceros. Reduce RH a
   una cota sobre una suma suavizada de potencias de primos: `G(x) ≪_ε x^{1/2+ε}` en
   intervalos `[Y, Y^{3/2}]` con `Y` arbitrariamente grande. Una cota así excluye ceros a la
   derecha de `1/2`.
2. **Dónde se atasca Chebyshev.** El método de Chebyshev cuenta primos con pesos, pero
   necesita un número con exponentes suaves y **divisibilidad controlada** (la «multiplicidad»
   que sobre cuerpos de funciones aporta el divisor en el argumento de Stepanov).
3. **El obstáculo real.** Sobre los enteros no hay derivada: no se puede «diferenciar números
   enteros» para conseguir esa multiplicidad. Es el mismo muro que separa Stepanov de los
   enteros.
4. **La idea.** Fabricar la multiplicidad de forma nativamente automorfa: **cadenas de
   levantamientos theta** entre grupos unitarios, con longitud `√X`. Cada levantamiento imita
   una unidad de multiplicidad; encadenados, dan la divisibilidad que falta. De ahí el exponente
   `1/2` (la nota lo llama «¿y qué otra cosa podría ser?»).
5. **La maquinaria.** Levantamientos theta, periodos GGP, fórmula de traza, covolúmenes,
   cohomología de Galois, torre de Iwasawa, Chowla–Selberg, masa de Siegel, y una versión débil
   de Vandiver para las clases que no se dejan matar girando.

## Qué significa para nuestras seis conclusiones

| # | Nuestro veredicto (agosto) | Estado tras la prueba |
|---|---|---|
| 1 | Rank–trace **tight** | Sigue siendo cierto: es una desigualdad sobre `tr(G)` y `‖G‖²_F`. No la toca nadie. |
| 2 | Techo 0,68185 **requiere RH** | Cierto, y ya vacío: con RH probada el techo del método deja de ser un techo del problema. |
| 3 | SDP **bloqueado** | Igual: seguía necesitando `F(α)` en `(1, 1+ε)`, o sea RH débil. |
| 4 | Estructura no conmutativa **bloqueada** | Igual. |
| 5 | Hardy–Littlewood **bloqueado** | Igual: nadie ha dado banda > 1 incondicional. |
| 6 | Mollifier + par de correlación **bloqueado** | Igual: siguen siendo redundantes con RH e incompatibles sin ella. |

**Ninguna de las seis conclusiones se cae.** Y esa es justo la lección: las seis hablaban de una
clase de datos —los dos momentos de la matriz de Gram, banda `λ ≤ 1`— y la prueba ganadora no
entra en ese espacio de datos ni una vez. Nuestra barrera era real y era local.

## Lo que sí se cae

- **El marco.** «El frente está en empujar 2/3» ya no es cierto: el frente estaba en los primos
  y en la divisibilidad. Empujar la constante era optimizar un atajo que dejó de hacer falta.
- **El plan 1 de nuestra lista de escapes** («probar RH → 0,68185») era un absurdo de
  formulación: si tienes RH tienes el 100 %, no un 68 %.
- **El escape 5** («una arquitectura de prueba fundamentalmente distinta») existía, lo listamos
  y lo tratamos como especulativo. Era matemática madura —Langlands, formas automorfas,
  geometría aritmética—, solo que fuera de nuestro campo de visión.

## Lecciones de método (las que importan para lo nuestro)

1. **Un panel multi-modelo corrige sesgos dentro de un marco; no corrige el marco.** Seis
   modelos distintos, seis ángulos distintos, un supuesto compartido: que los datos disponibles
   eran estadísticos de ceros. La diversidad de modelos no compra diversidad de encuadre.
2. **«Imposible» en un informe de agentes significa «imposible con estas herramientas».** Hay
   que escribirlo así, siempre, o la conclusión se lee como un teorema de imposibilidad.
3. **Barrera ≠ frontera del problema.** Nuestra afirmación era correcta y nuestra etiqueta
   («la barrera es real») invitaba a leerla como el mapa del problema entero.
4. **Una prueba incomprensible también es una prueba.** 17 millones de líneas sin exposición
   humana: el kernel la acepta, la comunidad la certifica, y la comprensión viene después. Eso
   cambia lo que significa «entender» en matemáticas, y es un dato para cualquier discusión
   sobre lo que un agente puede producir.

## Qué hacemos con este repositorio

- Se queda como **registro histórico fechado**: un mapa correcto de un método que resultó ser un
  ramal, no la carretera.
- Lo durable de aquel trabajo no es el resultado (no había resultado) sino el **método**: panel
  adversarial multi-modelo con trazabilidad. Eso vive en
  [`multi-model-orchestration`](https://github.com/elCanosail/multi-model-orchestration).

## Fuentes

- Nota del autor: <https://alpo.ge/remark.pdf>
- Certificación: [Lean community blog — *Lean verification of the Riemann Hypothesis*](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/), 21-11-2026.
- Verificación independiente de los teoremas principales: <https://math.mit.edu/~drew/shortgrh/>
- Reconstrucción analítica para ζ(s): [Rubinstein (ed.), *The Alpöge–Claude proof… explained*](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf), draft v2, 22-11-2026.
- Resumen enciclopédico y reacciones: [Wikipedia — Alpöge's proof of the Riemann hypothesis](https://en.wikipedia.org/wiki/Alp%C3%B6ge%27s_proof_of_the_Riemann_hypothesis).
