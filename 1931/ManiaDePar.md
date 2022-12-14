https://www.beecrowd.com.br/judge/pt/problems/view/1931

<body>
<div class="header">
<span>beecrowd | 1931</span>
<h1>Mania de Par</h1>
<div>
<p>Por Vinícius Fernandes dos Santos, Centro Federal de Educação Tecnológica de Minas Gerais. <img alt="" src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif"> Brazil</p>
</div>
<strong>Timelimit: 1</strong>
</div>
<div class="problem">
<div class="description">
<p>Patrícia é uma ótima desenvolvedora de software. No entanto, como quase toda pessoa brilhante, ela tem algumas manias estranhas, e uma delas é que tudo que ela faz tem que ser em número par.
Muitas vezes essa mania não atrapalha, apesar de causar estranhamento nos outros. Alguns exemplos:
ela tem que fazer diariamente um número par de refeições; no café da manhã toma duas xícaras de	café, duas torradas e duas fatias de queijo; sempre que vai ao cinema compra dois bilhetes de entrada
(felizmente sempre tem um amigo ou amiga lhe acompanhando); e toma dois banhos por dia (ou quatro, ou seis...).</p>
<p>Mas algumas vezes essa mania de Patrícia atrapalha. Por exemplo, ninguém gosta de viajar de carro com ela, pois se no trajeto ela tem que pagar pedágios, o número de pedágios que ela paga tem que ser par.</p>
<p>Patrícia mora em um país em que todas as estradas são bidirecionais e têm exatamente um pedágio. Ela precisa ir visitar um cliente em uma outra cidade, e deseja calcular o mínimo valor total de pedágios que ela tem que pagar, para ir da sua cidade à cidade do cliente, obedecendo à sua estranha mania de que o número de pedágios pagos tem que ser par.</p>
</div>
<h2>Entrada</h2>
<div class="input">
<p>A entrada consiste de diversas linhas. A primeira linha contém 2 inteiros <strong>C</strong> e <strong>V</strong>, o número total de cidades e o número de estradas (2 ≤ <strong>C</strong> ≤ 10<sup>4</sup> e 0 ≤ <strong>V</strong> ≤ 50000). As cidades são identificadas por inteiros de 1 a <strong>C</strong>. Cada estrada liga duas cidades distintas, e há no máximo uma estrada entre cada par de cidades. Cada uma das <strong>V</strong> linhas seguintes contém três inteiros <strong>C<sub>1</sub></strong>, <strong>C<sub>2</sub></strong> e <strong>G</strong>, indicando que o valor do pedágio da estrada que liga as cidades <strong>C<sub>1</sub></strong> e <strong>C<sub>2</sub></strong> é <strong>G</strong> (1 ≤ <strong>C1</strong>, <strong>C2</strong> ≤ <strong>C</strong> e 1 ≤ <strong>G</strong> ≤ 10<sup>4</sup>). Patrícia está atualmente na cidade 1 e a cidade do cliente é <strong>C</strong>.</p>
</div>
<h2>Saída</h2>
<div class="output">
<p>Uma única linha deve ser impressa, contendo um único inteiro, o custo total de pedágios para Patrícia ir da cidade 1 à cidade <strong>C</strong>, pagando um número par de pedágios, ou, se isso não for possível, o valor −1.</p>
</div>
<div class="both"></div>
<table>
<thead>
<tr>
<td>Exemplo de Entrada</td>
<td>Exemplo de Saída</td>
</tr>
</thead>
<tbody>
<tr>
<td class="division">
<p>4 4</p>
<p>1 2 2</p>
<p>2 3 1</p>
<p>2 4 10</p>
<p>3 4 6</p>
</td>
<td>
 <p>12</p>
</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
</tr>
</thead>
<tbody>
<tr>
<td class="division">
<p>5 6</p>
<p>1 2 3</p>
<p>2 3 5</p>
<p>3 5 2</p>
<p>5 1 8</p>
<p>2 4 1</p>
<p>4 5 4</p>
</td>
<td>
<p>-1</p>
</td>
</tr>
</tbody>
</table>
<div class="both"></div>
<p class="footer">
XX Maratona de Programação da SBC 2015
</p>
</div>
</body>