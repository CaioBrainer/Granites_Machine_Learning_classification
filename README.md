<h1>Granites classification with Machine Learning</h1>
 



# Tabela de conteúdos 

1. [Introdução](https://github.com/CaioBrainer/Granites_classification_with_Machine_Learning#introducao) 
2. [Metodologia](https://github.com/CaioBrainer/Granites_classification_with_Machine_Learning#metodologia)
3. [Resultados e Avaliação dos Modelos](https://github.com/CaioBrainer/Granites_classification_with_Machine_Learning#resultados-e-avaliacao-dos-modelos)

# Introdução
<p align="justify">
Neste projeto de artigo apresento uma metodologia para classificação de granitóides utilizando aprendizado de máquina, inicialmente irei os classificar
utilizando a classificação proposta por Barbarin (1999) em seu artigo intitulado "A review of the relationships between granitoid types, their origins and their geodynamic environments."
</p>

<p align="center">
<img width="400" alt="Elements distribution for classes" src="link_da_figura_upload_pelo_desktop">
</p>

# Metodologia
<p align="justify">
</p>

## Dados
<p align="justify">Os dados utilizados nesse artigo são provenientes do artigo do Bonin et al., (2020). Os dados são constituidos por análises químicas de rocha total de granitóides rotulados de acordo com a classificação proposta por Barbarin (1999). 

<p>Os dados foram tratados de forma a remover amostras com valores ausentes e filtrados de forma semelhante a utilizada por Bonin (2020), no qual definiu os valores minimos e máximos de SiO2 entre 52 e 80%.</p> 

<p>Devido a escassa quantidade de amostras referentes a classe dos RTG (ridge
‘tholeiitic’ granitoids) (n=38), também conhecidos como plagiogranitos, foi realizada uma pequena busca bibliográfica para expandir a quantidade de amostras (n=239) (referências...)
</p>

## Modelos

### Linear Discriminant Analysis
<p align="justify">Linear Discriminant Analysis (LDA) é um método supervisionado proposto inicialmente por R. Fisher (1936) que busca a combinação linear de atributos (ou um hiperplano) que minimiza a variância interclasse e maximiza separação entre classes maximizando as diferenças (Xanthopoulos et al., 2012).</p> 

<p align="justify">Uma abordagem utilizando o LDA foi utilizada por (Bonin et al., 2020) objetivando projetar o plano para separar os tipos de granitos propostos por Barbarin (1999). Em seu artigo eles encontraram valores de variância para LD1 e LD2 de 53 e 32%, respectivamente, e concluiram que a utilização do método em conjunto com a classificação de Barbarin (1999) são uteis em seu objetivo.</p>

<p align="justify">Tendo em vista que o LDA pode ser utilizado tanto para classificação quanto para projeção, e foi utilizado previamente para projeção e separação do tipo de granitos, iremos avaliar suas métricas no que diz respeito a classificação dos granitos</p>

### Decision Tree Classifier
<p> Árvores de decisão são algoritmos de aprendizado supervisionado não paramétrico que utilizam uma série de testes/regras lógicas para dividir os dados analisados em conjuntos reduzidos de forma a atingir a classificação de cada registro.</p>

<p>A seleção de atributos para cada nó se dá pela cálculo do ganho de informação ou pela impureza de Gini</p>

### Emsemble Models
<p> </p>

<p align="center">
<img width="400" alt="f2" src="link_da_figura_upload_pelo_desktop">
</p>

<p align="center">
Legenda
</p>


# Resultados e Avaliação dos Modelos
<p align="justify">

</p>


<p align="center">
<img width="650" alt="f3" src="">
</p>



