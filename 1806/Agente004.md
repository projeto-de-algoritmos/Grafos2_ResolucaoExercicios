https://www.beecrowd.com.br/judge/pt/problems/view/1806

<body>
<div class="header">
<span>beecrowd | 1806 | [P2][Univ]</span>
<h1>Agente 004</h1>
<div>
<p>Por Thalyson Nepomuceno, Universidade Estadual do Ceará <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brazil</p>
</div>
<strong>Timelimit: 3</strong>
</div>
<div class="problem">
<div class="description">
<p>Uma organização criminosa da cidade está ficando mais poderosa a cada dia, e para tentar acompanhar esse avanço, a organização protetora da cidade está investindo muito no treinamento dos seus homens. Bino, também conhecido como Agente 004, é o melhor agente da organização protetora, então ele foi designado para uma missão especial.</p>
<p>A missão especial de Bino é entregar uma mensagem secreta de uma sede de treinamento de agentes especiais para outra. Porém a cidade está cheia de criminosos, e todos eles querem interceptar Bino na sua missão.</p>
<p>Bino não conhece muito bem as rotas da cidade, pois passou a maior parte do tempo de sua vida sendo treinado em campos especiais, diferentemente dos criminosos, que passam maior parte das suas vidas nas ruas, e conhecem todas as rotas possíveis.</p>
<p>Como Bino é o melhor agente do mundo, ele sabe que é capaz de eliminar qualquer quantidade de criminosos que estão no mesmo local dele instantaneamente. Os criminosos podem interceptar Bino em qualquer lugar da cidade(Em todas as rotas e em tudos os lugares, inclusive, nos lugares onde estão as sedes de treinamento inicial e a destino). Bino e os criminosos se deslocam com velocidade de 12 m/s. Bino sempre utiliza o caminho que encontrará menos criminosos, porém, os criminosos sempre utilizam os melhores caminhos para interceptar Bino.</p>
<p>Sua tarefa é descobrir qual a quantidade mínima de criminosos que Bino terá que eliminar para entregar uma mensagem secreta de uma sede de treinamento para outra. É garantindo que existirá um caminho entre qualquer lugar na cidade para qualquer outro lugar.</p>
</div>
<h2>Entrada</h2>
<div class="input">
<p> A primeira linha contém 4 inteiros,&nbsp; <strong>N</strong>(1 ≤ <strong>N</strong> ≤ 10000), <strong>C</strong>(1 ≤ <strong>C</strong> ≤ 50000), <strong>S</strong>(1 ≤ <strong>S</strong> ≤ 50000) e <strong>B</strong> (1 ≤ <strong>B</strong> ≤ 10000), representando respectivamente o número de lugares na cidade, o número de rotas conhecidas pelo Bino, o número de rotas conhecidas somente pelos criminosos &nbsp;e o número de criminosos. Cada uma das próximas <strong>C</strong> linhas contém três inteiros <strong>a</strong>(1 ≤ <strong>a</strong> ≤ <strong>N</strong>), <strong>b</strong>(1 ≤ <strong>b</strong> ≤ <strong>N</strong>) e <strong>v</strong>(1 ≤ <strong>v</strong> ≤ 1000), representando que existe uma rota entre os lugares <strong>a</strong> e <strong>b</strong> com distância de <strong>v</strong> metros. Cada uma das próximas <strong>S</strong> linhas contém três inteiros <strong>a</strong>(1 ≤ <strong>a</strong> ≤ <strong>N</strong>), <strong>b</strong>(1 ≤ <strong>b</strong> ≤ <strong>N</strong>), <strong>v</strong>(1 ≤ <strong>v</strong> ≤ 1000), representando que existe uma rota secreta entre os lugares <strong>a</strong> e <strong>b</strong> com distância de <strong>v</strong> metros. A próxima linha contém <strong>B</strong> inteiros <strong>l<sub>i</sub></strong>(1 ≤ <strong>l<sub>i</sub></strong> ≤ <strong>N</strong>) representando que o criminoso <strong>i</strong> está inicialmente no lugar <strong>l</strong>. A última linha do caso de teste contém 2 inteiros <strong>K</strong>(1 ≤ <strong>K</strong> ≤ 10000), &nbsp;e <strong>F</strong>(1 ≤ <strong>F</strong> ≤ 10000), representando respectivamente o lugar inicial do Bino e o lugar onde ele vai ter que entregar a mensagem secreta.</p>
</div>
<h2>Saída</h2>
<div class="output">
<p>Imprima a quantidade mínima de criminosos que Bino vai eliminar no caminho.</p>
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
<p>6 5 0 3<br>
2 1 10<br>
2 4 5<br>
4 3 5<br>
5 4 5<br>
6 4 6<br>
3 6 5<br>
3 2<br>
</p></td>
<td>
<p>2</p>
</td>
</tr>
</tbody>
</table>
<table>
<thead>
</thead>
<tbody>
<tr>
<td class="division">
<p>6 5 1 3<br>
2 1 10<br>
2 4 5<br>
4 3 5<br>
5 4 5<br>
6 4 6<br>
6 4 5<br>
3 6 5<br>
3 2<br>
</p></td>
<td>
<p>3</p>
</td>
</tr>
</tbody>
</table>
<div class="both"></div>
<p class="footer">
Contest Oficial de Aquecimento da Olimpíada Brasileira de Informática 2015
</p>
</div>
</body>