Como comprimir um arquivo:

```sh
python main.py -c="./files/a_room_with_a_view.txt" -n=12 -f
```

Toda vez que a flage `-f` aparecer, o arquivo vai ser comprimido usando numero fixo de bits. Caso não use a flag, o programa vai usar um número variável de bits, como por exemplo abaixo: 

```sh
python main.py -c="./files/a_room_with_a_view.txt" -n=12 
```

No codigo acima fizemos uma compressão iniciando com 12 bits e aumentando conforme a necessidade.

Para descomprimir um arquivo:

```sh
python main.py -d="./files/a_room_with_a_view.lzw" -o="./files/a_room_with_a_view__dec.txt" -n=12 -f=1
```

Podemos fazer a descompressão de um arquivo com um número fixo de bits, como no exemplo acima, ou com um número variável de bits, como no exemplo abaixo:
```sh
python main.py -d="./files/a_room_with_a_view.lzw" -o="./files/a_room_with_a_view__dec.txt" -n=12
```


Agora vamos se dizer que tudo deu certo, podemos comparar os arquivos para ver se são iguais:

```sh
cmp --silent  ./files/a_room_with_a_view.txt ./files/a_room_with_a_view__dec.txt &&  echo "Files are identical" || echo "Files differ"
```

Se os arquivos forem iguais, a mensagem "Files are identical" vai aparecer, caso contrário, a mensagem "Files differ" vai aparecer.



Alguns outros exemplos de comandos:

```sh

python main.py -c="./files/ulysses.txt" -n=12
python main.py -d="./files/ulysses.lzw" -n=12 
```



O programa obrigatoriamente só comprime usando caracteres ASCII, então todo arquivo a ser passado para ele tem que tá encodificado em ASCII, caso não esteja o programa vai dar erro. O sugerido é converter o arquivo para ASCII e depois executar a compressao pelo nosso algoritmo.