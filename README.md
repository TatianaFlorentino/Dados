# Análise de Sentimentos pós Covid primeira Onda
![Screenshot](https://github.com/TatianaFlorentino/trajetoriads/blob/main/img/RH.jpeg)

A pandemia de COVID-19 transformou o mundo em poucos meses, os impactos causados foram inúmeros e alarmantes, como ainda não havia sido visto nesse século. As consequências causadas pelo vírus foram desde quarentenas de longa duração impostas pelas autoridades, como o fechamento de fábricas, escritórios, escolas e a obrigatoriedade do isolamento social, até os sentimentos gerados nas pessoas como o medo pela infecção, a frustração e o tédio, a perda financeira, e a dor pela perda de seus entes queridos. A COVIDiSTRESS é uma das maiores pesquisas realizadas no mundo em relação a percepção das pessoas diante das sensações causadas pela pandemia. Esse trabalho visa analisar as opiniões em relação à pandemia de COVID-19 daqueles que responderam à pesquisa no idioma português. Para isso, foi realizado a coleta desses dados no site COVIDiSTRESS, limpeza e organização dos mesmos, modelagem dos tópicos no qual foram definidos os termos mais relevantes e as palavras mais importantes para avaliação da análise de sentimentos feito com técnicas de mineração de texto. Para a conclusão das análises foram observados os comentários ao longo do tempo.

**Palavras-chave**: Covid-19, Pandemia, Processamento da Linguagem Natural, Análise de Sentimentos, COVIDiSTRESS, léxico, Representação bag of words, cálculos TFIDF, N-gramas, stemização de entidades nomeadas, Modelos tópicos 

![image](https://github.com/TatianaFlorentino/Dados/assets/41309689/d26b1b84-de68-4609-8cf7-94209982412d)

![image](https://github.com/TatianaFlorentino/Dados/assets/41309689/b1f99852-19c2-4cf1-a2c2-88a2d3647483)

![image](https://github.com/TatianaFlorentino/Dados/assets/41309689/29596ff9-e398-4cf5-b6de-9ba5198beb06)

![image](https://github.com/TatianaFlorentino/Dados/assets/41309689/a3a83b7d-cc6e-4cb7-a006-e95539a8a4c1)

Com a função de obter sentimentos, obtém-se a valência positiva e negativa de cada palavra, assim como a valência das oito emoções classificadas pelo NRC. 
Após a conversão foi extraída a parte textual com o comando corpus, para a construção dos corpora, a coleção de texto. Contagem das palavras, esse recurso foi usado para transformar um determinado texto em um vetor com base na frequência (contagem) de cada palavra que ocorre em todo o texto. Isso é útil quando se tem vários desses textos e deseja-se converter cada palavra em cada texto em vetores (para usar em análises de texto posteriores).

![image](https://github.com/TatianaFlorentino/Dados/assets/41309689/00354391-29f5-4c1c-a7cb-0b8a6833c162)

As similaridades dos comentários desse dataset foram obtidas por meio de um processo automático de K-Means, observou-se que haviam palavras correlatas.
![image](https://github.com/TatianaFlorentino/Dados/assets/41309689/5f7ad499-39a2-461d-a972-5761b6bbf3f6)

 Para ilustrar as polaridades presentes nos comentários foi elaborada uma nuvem de palavras baseadas nos adjetivos mais frequentes, as quais estão apresentadas na Figura 7.
![image](https://github.com/TatianaFlorentino/Dados/assets/41309689/ce54fb84-b096-4802-9da3-2467fb51cfab)


Código feito na linguagem R 
[Link:](https://github.com/TatianaFlorentino/scriptR/blob/master/TextMining_Oficial.R)


