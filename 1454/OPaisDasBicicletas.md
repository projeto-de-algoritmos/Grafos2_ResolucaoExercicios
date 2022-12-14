https://www.beecrowd.com.br/judge/pt/problems/view/1454

<body>
<div class="header">
<span>beecrowd | 1454</span>
<h1>O País das Bicicletas</h1>
<div>VIII Maratona de Programação IME-USP <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt=""> Brasil</div>
<strong>Timelimit: 3</strong>
</div>
<div class="problem">
<div class="description">
<p>Como você já deve saber, a bicicleta é um dos meios de transportes mais populares da China. Quase todos os chineses possuem a sua, e utilizam-na para trabalho, recreação, e outras atividades.</p>
<p>Após muitos anos pedalando, Mr. Lee já não têm a mesma disposição para encarar as diversas subidas da cidade onde mora. E a cidade em que Mr. Lee vive é extremamente montanhosa. Por razões sentimentais, ele não quer mudar para uma cidade mais plana. Resolveu, então, que tentaria evitar grandes altitudes em seus caminhos mesmo que, para isso, tivesse que pedalar um pouco mais.</p>
<p>Mr. Lee obteve com o serviço topográfico chinês uma coleção de mapas de sua cidade, em que cada rua desses mapas possui a informação da maior altitude encontrada quando trafegada. Tudo que ele precisa fazer agora é determinar rotas que minimizem a altura percorrida entre pares (origem, destino).</p>
<p>Sabendo que você planeja visitar a cidade em que ele mora no próximo ano, Mr. Lee pediu sua ajuda. Em uma primeira etapa, ele deseja que você implemente um programa que receba mapas topográficos da cidade e uma coleção de pares (origem, destino). Para cada par, seu programa deve imprimir a maior altura encontrada em uma rota entre a origem e o destino. Lembre-se que as rotas devem minimizar tais alturas. As rotas propriamente ditas, serão determinadas em uma segunda etapa (quando você chegar à China para visitá-lo).</p>
<p>Como o transporte utilizado é uma bicicleta, você pode considerar que todas as ruas da cidade são de mão dupla. Não demore, pois Mr. Lee conta com você. :-) </p>
</div>
<h2>Entrada</h2>
<div class="input">
<p>Seu programa deve estar preparado para trabalhar com diversos mapas, doravante denominados instâncias. Cada instância tem a estrutura que segue.</p>
<p>Na primeira linha são fornecidos dois inteiros <strong>n</strong> (0 ≤ <strong>n</strong>​ ≤ 100) e <strong>m</strong> (0 ≤ <strong>m</strong> ≤ 4950) que representam, respectivamente, os números de interseções e de ruas. Por razões de clareza, as interseções são numeradas de 1 a <strong>n</strong>, inclusive; toda rua começa e termina em uma interseção; e não existem interseções fora das extremidades de uma rua.</p>
<p>Nas próximas <strong>m</strong> linhas são fornecidos três inteiros: <strong>i</strong> e <strong>j</strong> (1 ≤ <strong>i</strong>, <strong>j</strong> ≤ <strong>n</strong>) que indicam a existência de uma rua entre as interseções <strong>i</strong> e <strong>j</strong>; e <strong>h</strong> que representa a maior altitude encontrada quando a rua é trafegada. Esses inteiros estão separados por espaços em branco.</p>
<p>Na linha seguinte, é dado um inteiro <strong>k</strong> (1 ≤ <strong>k</strong> ≤ <strong>50</strong>) que representa o número de pares (origem, destino) que serão especificados nas próximas <strong>k</strong> linhas. Cada par é formado por dois inteiros <strong>i</strong> e <strong>j</strong> como acima. Isto é, origem e destino são interseções de ruas, e também estão separados por espaços em branco.</p>
<p>Valores <strong>n</strong> = <strong>m</strong> = 0 indicam o final das instâncias e não devem ser processados. </p>
</div>
<h2>Saída</h2>
<div class="output">
<p>Para cada instância solucionada, você deverá imprimir um identificador <strong>Instancia</strong> <strong>h</strong> em que <strong>h</strong> é um número inteiro, sequencial e crescente a partir de 1. Nas próximas <strong>k</strong> linhas, você deve imprimir as maiores alturas encontradas nas rotas entre os <strong>k</strong> pares (origem, destino) fornecidos, um valor por linha, na ordem da entrada.</p>
<p>Uma linha em branco deve ser impressa após cada instância.</p>
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
<p>12 17<br>
1 4 4<br>
4 7 6<br>
7 10 6<br>
2 5 4<br>
5 8 5<br>
8 11 2<br>
3 6 5<br>
6 9 3<br>
9 12 1<br>
1 2 1<br>
2 3 9<br>
4 5 3<br>
5 6 7<br>
7 8 7<br>
8 9 2<br>
10 11 1<br>
11 12 2<br>
4<br>
1 5<br>
6 8<br>
6 7<br>
11 10<br>
0 0</p>
</td>
<td>
<p>Instancia 1<br>
4<br>
3<br>
6<br>
1</p>
</td>
</tr>
</tbody>
</table>
<p class="footer">
VIII Maratona de Programação IME-USP 2004.
</p>
</div>
<script defer="" src="https://static.cloudflareinsights.com/beacon.min.js/vaafb692b2aea4879b33c060e79fe94621666317369993" integrity="sha512-0ahDYl866UMhKuYcW078ScMalXqtFJggm7TmlUtp0UlD4eQk0Ixfnm5ykXKvGJNFjLMoortdseTfsRT8oCfgGA==" data-cf-beacon="{&quot;rayId&quot;:&quot;7746b315fe02d07a&quot;,&quot;token&quot;:&quot;43f41e4aa277420bad9940f8d8a80572&quot;,&quot;version&quot;:&quot;2022.11.3&quot;,&quot;si&quot;:100}" crossorigin="anonymous" style="display: none !important;"></script>

<div id="bardeen-root"></div><app-weava-root id="weava-root" class="weava" ng-version="12.2.16"></app-weava-root></body>