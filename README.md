# send_emails_with_python

# Language used:
   
   - Python 3.11.2
   - python-decouple
  
# A respeito do programa:
  Este código Python tem como objetivo permitir o envio assíncrono de e-mails utilizando a biblioteca smtplib e a funcionalidade de threads da biblioteca threading. Ele é projetado para enviar um e-mail após um determinado período de tempo, especificado como argumento. O conteúdo do e-mail é gerado a partir de um template HTML lido de um arquivo.
  
A biblioteca decouple é usada para ler as credenciais do e-mail do remetente (endereço de e-mail e senha) a partir de um arquivo de configuração externo. Isso ajuda a manter as credenciais fora do código-fonte, melhorando a segurança.
A parte interessante desse código é a capacidade de fazer o envio de email marketing de forma fácil e gratuito.

# Exemplo de email marketing encaminhado:
![image](https://user-images.githubusercontent.com/95552879/255031482-b60713bf-12bf-4597-a3f5-0fda47545493.png)

Confira esse repositório para mais informações para você criar seu template:

https://github.com/gabflag/make_your_own_email_marketing


# Comentários do Dev:
  Tive um problema que estava ocorrendo porque o método .format() estava sendo aplicado ao conteúdo do template HTML, o que causava conflitos de substituição das chaves {} que fazem parte do código CSS. Como o CSS também utiliza chaves {} para definir blocos de estilo, o método .format() estava interpretando essas chaves como placeholders para formatação de string, o que gerava o erro.

Ao remover o uso do método .format() e definir diretamente o corpo do email como o conteúdo do template HTML, consegui evitar esse conflito e permitiu que o HTML fosse enviado sem alterações indesejadas ou erros de execução.

