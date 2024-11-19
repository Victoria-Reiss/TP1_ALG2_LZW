# LZW: Algoritmo de Compressão Baseado em Estrutura de Dados Trie 

* Autora: *Victoria Oliveira dos Reis (<v.oliveirareiss@gmail.com>, <v.oliveirareiss@ufmg.br>)*
* Disciplina: *Algoritmos II*

## Introdução

Nesse projeto, será abordado a implementação do algoritmo LZW utilizando uma estrutura de dados do tipo Trie. O LZW (Lempel-Ziv-Welch) é um algoritmo de compressão sem perdas amplamente utilizado, especialmente em formatos de arquivos como GIF e TIFF. Ele trabalha identificando padrões repetidos em uma sequência de dados e substituindo essas repetições por códigos mais compactos. A principal característica do LZW é a construção dinâmica de um dicionário que associa sequências de dados a códigos de forma eficiente, sem a necessidade de transmitir o dicionário completo, tornando-o ideal para compressão de dados com redundâncias frequentes. 

A utilização de uma árvore Trie compacta na implementação do LZW permite armazenar e buscar sequências de caracteres de forma eficiente, utilizando a sobreposição de prefixos comuns. Isso reduz a necessidade de armazenamento redundante e acelera a busca de padrões durante a compressão, já que cada sequência é representada de forma hierárquica, facilitando tanto a navegação quanto a inserção de novos elementos no dicionário dinâmico do algoritmo.

## Processo de Compressão do Algoritmo 

### Input/Output - Compressão

Na implementação do algoritmo de compressão, o processo ocorre da seguinte maneira: inicialmente, um arquivo de texto é recebido, e seu conteúdo é analisado para identificar padrões e armazená-los em uma estrutura Trie. Cada sequência distinta de caracteres (ou palavra) no texto é mapeada para um código único, representado em formato binário. Esses códigos servem como identificadores compactos das sequências armazenadas na Trie.

Por padrão, utilizamos um tamanho fixo de 12 bits para os códigos, o que implica em um espaço de representação de \( 2^{12} = 4096 \) combinações possíveis. No entanto, o tamanho dos códigos pode ser ajustado dinamicamente em função do volume de dados e da necessidade de armazenamento, garantindo maior eficiência para arquivos de diferentes tamanhos. Após a compressão, o arquivo resultante no formato ".lzw" contém sequências binárias que correspondem diretamente às strings registradas na Trie, proporcionando uma representação compacta e eficiente do texto original.

### Observações
No algoritmo, realizamos a leitura de arquivos de qualquer formato, garantindo sua compatibilidade ao transformá-los em uma representação binária. Essa conversão permite que os dados sejam manipulados de forma uniforme, independentemente de sua origem. Posteriormente, os caracteres do arquivo são codificados utilizando o padrão ASCII.
## Comandos de compilação

### Como comprimir um arquivo

Para comprimir um arquivo de texto no formato `.txt` utilizando o algoritmo LZW:

```sh
python main.py -c="./files/a_room_with_a_view.txt" -o="./files/a_room_with_a_view.lzw" -n=12 -f
```

* `-c`: Caminho para o arquivo de entrada a ser comprimido.
* `-n`: Número de bits usados para os códigos (padrão: 12).
* `-f`: Flag opcional para habilitar se o número de bits é variável ou fixo (padrão: False -> não é fixo). Caso não seja inserido, então assumme que o valor de bits é variável.

### Como descomprimir um arquivo

Para descomprimir um arquivo no formato `.lzw` e gerar o texto original:

```sh
python main.py -d="./files/a_room_with_a_view.lzw" -o="./files/a_room_with_a_view__dec.txt" -n=12 -f
```

* `-d`: Caminho para o arquivo comprimido.
* `-o`: Caminho para salvar o arquivo descomprimido.
* `-n`: Número de bits usados para os códigos.
* `-f`: Flag opcional para configurações adicionais.

### Exemplo de comando
```sh
python main.py -c="./files/a_room_with_a_view.txt" -o="./files/a_room_with_a_view.lzw" -n=9
```
Esse comando recebe o arquivo que será comprimido, salva o arquivo comprimido com a extensão `.lzw`e recebe o número de bits como 9. Como não foi passado -f, o algoritmo assume que o tamanho é variável caso a string ultrapasse o tamanho de 9 bits.


### Comparar os arquivos para verificar integridade

Após comprimir e descomprimir o arquivo, use o seguinte comando para verificar se os arquivos original e descomprimido são idênticos, caso queira verificar:

```sh
cmp --silent ./files/a_room_with_a_view.txt ./files/a_room_with_a_view__dec.txt && echo "Files are identical" || echo "Files differ"
```
Se os arquivos forem iguais, será exibida a mensagem: Files are identical.
Caso contrário, será exibida a mensagem: Files differ

## Exemplos de arquivos que podem ser comprimidos

Podemos utilizar arquivos com caracteres gerados aleatoriamente ou selecionar textos disponíveis na internet para os testes. Na pasta `files`, foram disponibilizados alguns textos do *Projeto Gutenberg*, uma iniciativa digital sem fins lucrativos que oferece acesso gratuito a uma vasta coleção de livros, principalmente de obras clássicas que estão em domínio público. O projeto foi fundado por Michael S. Hart em 1971 e tem como objetivo preservar e disponibilizar conteúdo literário, acadêmico e cultural em formato digital, facilitando o acesso a essas obras em todo o mundo. Entre os exemplos de textos utilizados, estão obras nos idiomas inglês e português, permitindo avaliar a compressão de dados em caracteres diferentes como "ç", um símbolo que não pertecence a língua inglesa.

### Lista de alguns livros disponíveis no arquivo `files`. 

1. FIALHO DE ALMEIDA, Cidade do Vício.

2. AUSTEN, Jane. Pride and Prejudice.

3. CARROLL, Lewis. Alice's Adventures in Wonderland.

4. SHAKESPEARE, William. Romeo and Juliet.

5. t1.bmp, uma imagem em bmp.

## Análise do Processo de Compressão

Nossa análise do processo será conduzida com base nos arquivos disponibilizados na pasta `Files`. Esses arquivos servirão como dados de entrada para a avaliação e testes do algoritmo, permitindo uma análise prática e detalhada de seu desempenho em diferentes cenários.

### LZW Compression and Decompression

### Settings

| **File**                | **To Compress**               | **Type** | **Output File**                  |
|-------------------------|-------------------------------|-------------------|----------------------------------|
| **the_odyssey.txt**      | ./files/the_odyssey.txt       | Texto              | ./files/the_odyssey.lzw          |
| **dracula.txt**          | ./files/dracula.txt           | Texto              | ./files/dracula.lzw              |
| **mob_dick.txt**         | ./files/mob_dick.txt          | Texto              | ./files/mob_dick.lzw             |
| **romeo_and_juliet.txt** | ./files/romeo_and_juliet.txt  | Texto              | ./files/romeo_and_juliet.lzw     |
| **cidade_do_vicio.txt**  | ./files/cidade_do_vicio.txt   | Texto              | ./files/cidade_do_vicio.lzw      |
| **bible.txt**            | ./files/bible.txt             | Texto              | ./files/bible.lzw                |
| **sample_river.bmp**     | ./files/sample_river.bmp      | Imagem             | ./files/sample_river.lzw         |
| **paper.pdf**            | ./files/paper.pdf             | PDF                | ./files/paper.lzw                |

### Compression Statistics

| **File**                | **Compression Time** | **Original File Size** | **Compressed File Size** | **Compression Ratio** |
|-------------------------|----------------------|------------------------|--------------------------|-----------------------|
| **the_odyssey.txt**      | 104.88744s           | 694,136 Bytes          | 353,337 Bytes            | 50.9031%              |
| **dracula.txt**          | 131.32729s           | 865,646 Bytes          | 441,922 Bytes            | 51.0511%              |
| **mob_dick.txt**         | 187.68008s           | 1,230,548 Bytes        | 635,931 Bytes            | 51.6787%              |
| **romeo_and_juliet.txt** | 26.49134s            | 160,731 Bytes          | 96,844 Bytes             | 60.2522%              |
| **cidade_do_vicio.txt**  | 69.82445s            | 439,733 Bytes          | 247,831 Bytes            | 56.3594%              |
| **bible.txt**            | 540.11007s           | 4,356,020 Bytes        | 1,822,356 Bytes          | 41.8353%              |
| **sample_river.bmp**     | 172.95390s           | 818,058 Bytes          | 807,327 Bytes            | 98.6882%              |
| **paper.pdf**            | 253.50712s           | 1,168,615 Bytes        | 1,150,954 Bytes          | 98.4887%              |

A análise dos dados de compressão revela que a média do **Compression Ratio** dos arquivos comprimidos é de **63.65%**, indicando uma redução significativa no tamanho dos arquivos após a compressão. Além disso, o **desvio padrão** do **Compression Ratio** é de **20.75%**, o que sugere uma variação considerável nos resultados de compressão entre os diferentes arquivos analisados. Esse desvio padrão mais alto implica que, enquanto alguns arquivos apresentam uma compressão muito eficiente, outros podem ter uma taxa de compressão mais baixa, provavelmente devido às características específicas de cada tipo de arquivo, como formato, conteúdo e estrutura interna. Esses dados são cruciais para entender a eficácia da compressão em diferentes contextos e podem ser usados para otimizar os processos de compressão para arquivos semelhantes.


## Referências
* MASSACHUSETTS INSTITUTE OF TECHNOLOGY. 6.02 Course Notes, Chapter 3: Data Compression. Disponível em: https://web.mit.edu/6.02/www/s2012/handouts/3.pdf.
* WIKIPEDIA. Radix tree. Disponível em: https://en.wikipedia.org/wiki/Radix_tree.

