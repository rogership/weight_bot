## Fluxograma do código

### Coleta de dados via Telegram API Handler

1. Envio de dados via grupo do telegram
    formato da mensagem da forma:

    > peso <float> KG

    1.1. Configurações do bot para receber e enviar mensagens ao grupo

        privacy mode off

        allow groups

    1.2. Estruturar o script para parse do comando peso

2.  Código recebe dados via Telegram API Handler como variável "mensagem"
    arg parser trata mensagem, primeiro comando <peso> ou outro argumento

3. <span style="color:green"> OK </span>. Definir função que recebe valor, valida valor, e escreve em arquivo JSON
    formato de nested dicionário

    > {data: {"peso": <peso>}}

4. Definir função que lê arquivo JSON e plota em gráfico, gera gráfico.

5 - Retornar o gráfico como imagem via API Handler quando solicitado.
    O Usuário faz query a API Handler, script retorna o gráfico via Telegram.


### Funcionalidades futuras

1. Listar tabela via bot API Handler


2. Add e Del items da tabela

