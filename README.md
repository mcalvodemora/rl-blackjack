# Aprendizaje por Refuerzo - Blackjack



## Bienvenido

¡Bienvenido a nuestro proyecto de Aprendizaje por Refuerzo - Blackjack! En el desarrollo de este proyecto encontrarás la implementación y entrenamiento de un agente que puede jugar al famoso y clásico juego de backjack de forma automática en un entrono virtual, utilizando técnicas de Aprendizaje por Refuerzo (Reinforcement Learning - RL).

El RL es un área del aprendizaje automático, cuya ocupación es determinar qué acciones debe escoger un agente en un entorno dado con el fin de maximizar alguna noción de "recompensa".

En nuestro caso, el proyecto emplea el siguiente entorno disponible en Gym OpenAI ([Blackjack](https://www.gymlibrary.dev/environments/toy_text/blackjack/)) para implementar el juego y crear nuestros agentes.

## Equipo desarolladores

Nuestro equipo de colaboradores que implementaron y desarrollaron este proeyecto incluye:
 - Celia Quiles Alemañ | 202315604@alu.comillas.edu
 - Álvaro Ezquerro Pérez | alvaroezquerro@alu.comillas.edu
 - María Calvo de Mora Román | 202320059@alu.comillas.edu

## Visión general del entorno

En el entorno de Blackjack ([Blackjack](https://www.gymlibrary.dev/environments/toy_text/blackjack/)), es vencer al crupier obteniendo una suma de cartas más cercana a 21 que las del crupier, sin pasarse. 

Este juego se juega con un mazo infinito (o con reemplazo). El juego comienza con el crupier teniendo una carta boca arriba y otra boca abajo, mientras que el jugador tiene dos cartas boca arriba.

El jugador puede solicitar cartas adicionales (acción de "pegar o hit", acción=1) hasta que decida detenerse ("quedarse o stand", acción=0) o se pase de 21 ("busto o bust", pérdida inmediata). Después de que el jugador se queda, el crupier revela su carta boca abajo y toma cartas hasta que su suma sea 17 o mayor. Si el crupier se pasa, el jugador gana. Si ninguno de los dos se pasa, el resultado (ganar, perder, empate) se decide por quién tenga la suma más cercana a 21.

Por tanto, existen dos acciones posibles en este entorno: 
- Quedarse (0):  el jugador decide no recibir más cartas.
- Pegar (1): el jugador solicita una carta adicional.

Otro factor importante a tener en cuenta es el espacio de observación del agente que se entrena en dicho entorno. La observación que recibe el jugador consiste en una tupla de 3 elementos:la suma actual de las cartas del jugador, el valor de la carta del crupier que está visible (1-10, donde 1 es el as) y la presencia de un as utilizable por parte del jugador (0 o 1), el cual contará como 1 o 11 dependiendo del valor de la mano. Puedes echar un vistazo rápido al GIF inferior para hacerte un mejor idea del entorno y la jugabilidad:

![Example of BlackJack environment](docs/imgs/blackjack.gif)


## Algoritmos de aprendizaje

En este proyecto compararemos el rendimiento de varias técnicas de Aprendizaje por Refuerzo, entre las que se incluyen:
- **Q-learning**: Un algoritmo que propone una adpatación del algoritmo de iteración Qvalue para las situaciones en las que las probabilidades de transición t las recompensas son inicialmente desconocidas. Específicamente, este algoritmo aprende una función Q que estima la recompensa futura esperada de realizar una acción determinada en un estado concreto. Funciona explorando el espacio de juego y aprendiendo de las recompensas que recibe del entorno. Mediante el uso de una política epsilon-greedy, equilibra la compensación entre exploración y explotación, lo que significa que el agente tomará ocasionalmente una acción aleatoria para explorar nuevas posibilidades y evitar quedarse atascado en una política subóptima.

- **Deep Q-Network (DQN)**: utiliza una red neuronal profunda para aproximar una política o una función de valor. Es decir, es un enfoque de Aprendizaje por refuerzo basado en el Aprendizaje Profundo que utiliza una red neuronal para aproximar la función Q. Combina Q-Learning con la repetición de experiencias para mejorar la eficiencia de las muestras y la estabilidad durante el entrenamiento. La repetición de experiencias significa que el agente almacena sus experiencias y aprende de ellas en un momento posterior, lo que permite un uso más eficiente de los datos y reduce el riesgo de que el agente se quede atascado en un estado concreto.

- **Dueling Deep Q-Network**: de manera similar a DQN utiliza una red neuronal profunda para aproximar una política o una función de valor. La diferencia clave ante una DQN radica en que, en vez de predecir el Q-valor de cada acción, predice el valor de cada estado y la ventaja de cada acción. Esto se realiza dividiendo la última capa en dos, una para cada predicción (valor de estado y ventaja), por último, se unen ambas predicciones para obtener el Q-valor de cada acción. Este algoritmo se implementará, tanto con dos redes una principal y una target, como solo con la principal.

- **Advantage actor-critic (A2C)**: Este algoritmo, más complejo, combina las ventajas del enfoque de política y del enfoque de valor, para aprender una política óptima. Utiliza una red neuronal para aproximar tanto la política de acciones como la función de valor, permitiendo que el agente aprenda de la experiencia y mejore su rendimiento a lo largo del tiempo.


## Evaluación de las técnicas

Con el fin de evaluar la eficacia de las técnicas de aprendizaje por refuerzo que aplicamos, mediremos:
- La tasa de victorias, empates y derrotas de cada agente tras un número fijo de episodios de entrenamiento.
- Así como el número de pasos totales realizados para el aprendizaje.

De igual modo, y para comprender mejor y visualmente la evolución de las distintas técnicas implementadas, hemos creado un vídeo que muestra los resultados de los algoritmos aplicados. Dicho video puede ser encontrado en el directorio `docs/imgs/results.gif` y verlo para ver cómo juegan nuestros agentes.

Adicionalmente, para un análisis más profundo, consulte nuestro informe disponible en `docs/Informe_RL_Blackjack.pdf`. Este documento contiene explicaciones detalladas de los algoritmos utilizados y un análisis de su rendimiento e idoneidad para el juego del Blackjack.

## Conclusión

Este proyecto sirve como demostración práctica de la aplicación de diversas estrategias de Aprendizaje por Refuerzo a una tarea de control difícil como jugar partidas de BlackJack donde no solo dependes de tus cartas, sino también de las de tu contrincante. Al explorar distintos algoritmos, obtenemos información valiosa sobre sus capacidades y eficacia en diferentes escenarios.