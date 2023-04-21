<h1>Granites classification with Machine Learning</h1>
 
# Tabela de conteúdos 

1. [Introdução](https://github.com/CaioBrainer/Granites_classification_with_Machine_Learning#introducao)  
2. [Metodologia](https://github.com/CaioBrainer/Granites_classification_with_Machine_Learning#metodologia)
   - [Dados](https://github.com/CaioBrainer/Granites_classification_with_Machine_Learning#dados)
   - [Modelos](https://github.com/CaioBrainer/Granites_classification_with_Machine_Learning#modelos)
     - [Linear Discriminant Analysis](https://github.com/CaioBrainer/Granites_classification_with_Machine_Learning#linear-discriminant-analysis)
     - [Decision Trees](https://github.com/CaioBrainer/Granites_classification_with_Machine_Learning#decision-trees)
     - [Random Forests](https://github.com/CaioBrainer/Granites_classification_with_Machine_Learning#random-forests)
     - [XGBoost](https://github.com/CaioBrainer/Granites_classification_with_Machine_Learning#xgboost)
     - [LightGBM](https://github.com/CaioBrainer/Granites_classification_with_Machine_Learning#lightlgbm)
3. [Resultados e Avaliação dos Modelos](https://github.com/CaioBrainer/Granites_classification_with_Machine_Learning#resultados-e-avaliação-dos-modelos)
4. [Discussão](https://github.com/CaioBrainer/Granites_classification_with_Machine_Learning#discussao)
5. [Conclusão](https://github.com/CaioBrainer/Granites_classification_with_Machine_Learning#conclusão)
6. [Referências](https://github.com/CaioBrainer/Granites_classification_with_Machine_Learning#referências)

# Introdução
<p align="justify">
A classificação de granitóides permanece um dos grandes dilemas da geoquímica de rochas ígneas, diversos são os esquemas e diagramas que propõem separar os granitóides em grupos distintos (Maniar and Piccoli, 1989; Barbarin 1999; Frost et al., 2001; Frost et al., 2016). Frost et al., (2001) aponta para a existência de mais de vinte modelos (sejam eles genéticos ou tectônicos) e que embora existam tantos modelos nenhum esquema individual tenha alcançado sucesso unânime.
</p>

<p align="justify">
Com o advento da BIG DATA e a evolução de recursos computacionais em termos de software e hardware nos ultimos anos, vemos acompanhando um grande aumento da utilização de modelos de machine learning nas mais diversas áreas de pesquisa (Dramsch, 2020), tal fenômeno também tem sido observado em diversas áreas das geociências (Zuo, Xiong, Wang and Carranza 2019, Li et al., 2021, He et al., 2022, Sun et al., 2022) e como apontado por KARPATNE ET AL. (2018) a crescente disponibilidade de dados geológicos oferece um grande potencial para aplicações de machine learning no âmbito das geociências. 
</p>

<p align="justify">
 
</p>

<p align="justify">
Neste projeto de artigo apresento uma metodologia para classificação de granitóides utilizando aprendizado de máquina, inicialmente irei os classificar utilizando a classificação proposta por Barbarin (1999) em seu artigo intitulado 
"A review of the relationships between granitoid types, their origins and their geodynamic environments."
</p>


<p align="center">
Classificação proposta por Barbarin (1999)
</p>

<p align="justify">
Como discutido por Bonin et al., (2020) os TTG's são caracterizados como uma classe distinta de granitóides e embora não façam parte da proposta original
foram incluidos no dataset, sendo possível ainda subdividir os TTG's em duas subclasses como apresentado por Moyen, (2019). 
</p>

# Metodologia
<p align="justify">
</p>

## Dados
<p align="justify">Os dados utilizados nesse artigo são provenientes do artigo do Bonin et al., (2020). Os dados são constituidos por análises químicas de rocha total de granitóides rotulados de acordo com a classificação proposta por Barbarin (1999). </p>

<p align="justify">Os dados foram tratados de forma a remover amostras com valores ausentes e normalizados para representar 100% (base anidra) sendo ainda filtrados de forma semelhante a utilizada por Bonin (2020), no qual definiu os valores minimos e máximos de SiO2 entre 52 e 80%, respectivamente.</p> 

<p align="justify">Devido a escassa quantidade de amostras referentes a classe dos RTG (ridge
‘tholeiitic’ granitoids) (n=38), também conhecidos como plagiogranitos, foi realizada uma pequena busca bibliográfica para expandir a quantidade de amostras (n=239) (referências...)
</p>

<p align="center">
<img width="700" alt="Elements distribution for classes" src="https://user-images.githubusercontent.com/92734524/233514049-f1b6f316-71f4-4e7e-88cb-a17498aaee9b.jpeg">
</p>

<p align="center">
Boxplots com a distribuição dos elementos por grupo.
</p>

## Modelos

### Linear Discriminant Analysis
<p align="justify">Linear Discriminant Analysis (LDA) é um método supervisionado proposto inicialmente por R. Fisher (1936) que busca a combinação linear de atributos (ou um hiperplano) que minimiza a variância interclasse e maximiza separação entre classes maximizando as diferenças (Xanthopoulos et al., 2012).</p> 

<p align="justify">
 Uma abordagem utilizando o LDA foi utilizada por (Bonin et al., 2020) objetivando projetar o plano para separar os tipos de granitos propostos por Barbarin (1999). Em seu artigo eles encontraram valores de variância para LD1 e LD2 de 53 e 32%, respectivamente, e concluiram que a utilização do método em conjunto com a classificação de Barbarin (1999) são uteis em seu objetivo.
</p>

<p align="justify">
 Tendo em vista que o LDA pode ser utilizado tanto para classificação quanto para projeção, e foi utilizado previamente para projeção e separação do tipo de granitos, iremos avaliar suas métricas no que diz respeito a classificação dos granitos
</p>

### Decision Trees

### Random Forest

### XGBoost

### LightGBM

<p align="justify"> </p>

# Resultados e Avaliação dos Modelos
<p align="justify">
</p>

<p align="center">
<img width="700" alt="f1_scores" src="https://user-images.githubusercontent.com/92734524/233514387-0f8e1f89-24cf-4da2-8ccb-419a96ada717.jpeg">
</p>

<p align="center">
F1 scores para os modelos treinados
</p>


<p align="center">
<img width="700" alt="cm" src="https://user-images.githubusercontent.com/92734524/233514212-b5fbbaa5-f43f-46dc-a95d-5d721e00d449.jpeg">
</p>

<p align="center">
Matrix de confusão dos melhores modelos
</p>

# Discussão
# Conclusão
# Referências


