# PatMail

PatMail é um aplicativo para envio automatizado de emails feito totalmente em python, usando para interface gráfica o módulo TKinter. 

## Documentação

PatMail permite ao usuário importar um arquivo .csv de contatos, contendo duas colunas, em ordem, "Name" e "Email", e um arquivo .txt, que conterá a mensagem a ser enviada aos contatos do arquivo de contatos. Além disso, PatMail permite ao usuário importar anexos para serem enviados juntos à mensagem a ser enviada aos contatos.

### Utilização

1- Importe os arquivos ou digitando o caminho do arquivo ou usando a ferramenta de busca;

2- Adicione anexos ao corpo da mensagem, caso queira;

3- Entre com seu email e senha;

4- Adicione o assunto do email;

5- Clique em "Enviar Emails";

OBS: os passos de 1 a 4 podem ser feitos em qualquer ordem.

## Funcionalidades

- Envio de email para diversos contatos de forma automatizada;
- Permite anexar arquivos para enviar;
- No arquivo .txt de mensagem, podem ser utilizadas 2 variáveis que serão substituídas por informações dos destinatários:
    * ${NAME}: é substituído pelo nome do destinatário;
    * ${EMAIL}: é substituído pelo email do destinatário;
- Após importar o arquivo de contatos e o da mensagem, na aba de contatos será possível dar dois-cliques na linha de um destinatário para abrir uma pré-visualização da mensagem para esse destinatário em específico.


## Instalação

Tendo os requisitos cumpridos, existem duas formas principais para realizar a instalação do pacote.

### Requisitos

- Python 3.6 ou superior (o aplicativo não foi testado em todas as versões, então pode ser que funcione em versões anteriores a essa);
- pip instalado;

### 1) usando como pacote do pip

- Baixe o código-fonte do PatMail;
- Navegue até a raiz do projeto:

```bash
cd Path/To/PathMail
```

- Instale o aplicativo como um pacote python:

```bash
pip install .
```

- Caso o pip não esteja no PATH do sistema:

```bash
python3 -m pip install .
```

- Após o fim da instalação, PatMail será instalado como um pacote do pip, e poderá ser aberto com:

```bash
PatMail
```

### 2) chamando o arquivo de inicio diretamente

Caso o método 1 não funcione ou não queira deixar PatMail como um pacote do pip, pode simplesmente baixar as dependências necessárias e chamar o arquivo que inicia o aplicativo:

```bash
pip install -r /Path/To/PatMail/requirements.txt
python3 /path/to/PatMail/src/main.py
```

Obs: Caso opte pela segunda forma de instalação, utilizar um `alias` pode facilitar a inicialização do aplicativo. 

#### Um exemplo no bash:

adicione ao ~/.bashrc ou equivalente a seguinte linha:

```bash
alias PatMail='python3 /path/to/PatMail/src/main.py'
```
## Solução de Problemas (Troubleshooting)

- PatMail utiliza apenas o servidor SMTP do Google para realizar os envios dos emails e, por isso, estará limitado a possiveis restrições do servidor em questão;
- Caso não consiga entrar com seu usuário e senha, tente gerar uma senha de aplicativo nas configurações do seu usuário Google e utilizá-la como senha.
- Se o PatMail não estiver permitindo a importação de um arquivo .csv, se atente às restrições: 
    * No cabeçalho (primeira linha), devem conter apenas duas informações: "Nome"/"Name" e "Email"/"E-Mail", nessa ordem (o aplicativo é case insensitive para essas informações, para facilitar);
    * TODAS as linhas devem conter duas colunas com caracteres nelas;
- Caso seu problema não esteja listado aqui ou as soluções apresentadas não resolveram seu problema, abra um issue detalhando a situação com o máximo de informações possível, para que seja possível investigar as causas do problema e procurar soluções;

## Licença

[MIT](https://choosealicense.com/licenses/mit/)

