# Youtube API
Este é um código Flask que cria uma API para baixar vídeos do YouTube. A API aceita uma solicitação GET com o link do vídeo do YouTube como parâmetro e retorna uma URL com o arquivo de vídeo para o usuário.

#### Dependências:

    Flask==2.2.2
    Flask-Cors==3.0.10
    moviepy==1.0.3
    pytube==12.1.2

#### Rotas:

  * '/search':
    Essa rota aceita um parâmetro 'link' que é o link do vídeo do YouTube. Ele retorna as informações do vídeo, como miniatura, título e link para download, bem como as resoluções disponíveis.

  * '/download':
    Essa rota aceita dois parâmetros 'link' e 'res' que é o link do vídeo do YouTube e a resolução desejada, respectivamente. Ele retorna o arquivo de vídeo para o usuário.

#### Como usar:

   * Certifique-se de ter as dependências instaladas
   * Execute o arquivo python
   * use a rota '/search' passando o link do video como parametro
   * use a rota '/download' passando o link do video e a resolução desejada como parametro

>#### Nota:
>  É necessário ter autorização para baixar vídeos do youtube.
>  as dependências pytube e moviepy são usadas para baixar e converter o vídeo, respectivamente,
>  a biblioteca flask_cors é usada para permitir que o aplicativo seja acessado por outros domínios,
>  o arquivo é automaticamente removido após o download, mas pode ser adicionado outras funções para armazenar os arquivos baixados.
