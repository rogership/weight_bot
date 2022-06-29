## Fluxograma do código

### Coleta de dados via Telegram API Handler

1. <span style="color:green"> OK </span> Envio de dados via grupo do telegram
    formato da mensagem da forma:

    > peso <float> <data>

    1.1. Parse do message.text

    Configurações do BOT

        privacy mode off

        allow groups

2. <span style="color:green"> OK </span>. Definir função que recebe valor, valida valor, e escreve em arquivo JSON
    formato de nested dicionário

    > {data: {"peso": <peso>}}

3. TODO: Definir função que lê arquivo JSON e plota em gráfico, gera gráfico.

5 - TODO: Retornar o gráfico como imagem via API Handler quando solicitado.
    O Usuário faz query a API Handler, script retorna o gráfico via Telegram.


### Funcionalidades futuras

1. Listar tabela via bot API Handler


2. Add e Del items da tabela

