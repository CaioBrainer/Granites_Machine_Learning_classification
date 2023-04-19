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

# Introdução
<p align="justify">
Neste projeto de artigo apresento uma metodologia para classificação de granitóides utilizando aprendizado de máquina, inicialmente irei os classificar
utilizando a classificação proposta por Barbarin (1999) em seu artigo intitulado "A review of the relationships between granitoid types, their origins and their geodynamic environments."
</p>

<p align="center">
<img width="700" alt="Elements distribution for classes" src="https://user-images.githubusercontent.com/92734524/228396070-90be1d23-8a27-475c-9582-e2fe1baa9a13.jpg">
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
<img width="900" alt="Elements distribution for classes" src="https://user-images.githubusercontent.com/92734524/228398274-e50e1c58-11a7-423a-b4ca-4311b532be6e.jpeg">
</p>

<p align="center">
Boxplots com a distribuição dos elementos por grupo.
</p>

## Modelos

### Linear Discriminant Analysis
<p align="justify">Linear Discriminant Analysis (LDA) é um método supervisionado proposto inicialmente por R. Fisher (1936) que busca a combinação linear de atributos (ou um hiperplano) que minimiza a variância interclasse e maximiza separação entre classes maximizando as diferenças (Xanthopoulos et al., 2012).</p> 

<p align="justify">Uma abordagem utilizando o LDA foi utilizada por (Bonin et al., 2020) objetivando projetar o plano para separar os tipos de granitos propostos por Barbarin (1999). Em seu artigo eles encontraram valores de variância para LD1 e LD2 de 53 e 32%, respectivamente, e concluiram que a utilização do método em conjunto com a classificação de Barbarin (1999) são uteis em seu objetivo.</p>

<p align="justify">Tendo em vista que o LDA pode ser utilizado tanto para classificação quanto para projeção, e foi utilizado previamente para projeção e separação do tipo de granitos, iremos avaliar suas métricas no que diz respeito a classificação dos granitos</p>

### Decision Trees

### Random Forest

### XGBoost

### LightGBM

<p align="justify"> </p>

# Resultados e Avaliação dos Modelos
<p align="justify"></p>

# Discussão
# Conclusão

