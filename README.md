## ProvaPOO

Nesse repositório será armazenado a resolução das duas provas da disciplina de Programação Orientada a Objetos (POO) do curso de Ciências da Computação
O código fonte pode ser encontrado nos links abaixo.
- [Prova 01](./prova01)
- [Prova 02](./prova02)

As instruções para execução do programa em ambiente local pode ser visto abaixo.

### Configuração do Ambiente

inicialmente crie um ambiente virtual. Para isso use o comando:

```
python -m venv .venv
```

Logo depois é necessário ativar o ambiente virtual. Use o comando:

```
source .venv/bin/activate  
```
Por fim instale os pacotes usando o comando:

```
pip install -r requirements.txt
```

### Testes Unitários

Foram escritos alguns testes unitários. Para executá-los use o comando:

```
python -m unittest discover ./tests -v
```

se possuir [make](https://www.gnu.org/software/make/) instalo pode usar o comando:

```
make testes
```

### Prova 01

Para executar o menu use o comando:

```
python prova01/main.py 
```

### Prova 02

Para executar o menu use o comando:

```
python prova02/main.py 
```