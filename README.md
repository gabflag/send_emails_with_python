# send_emails_with_python


Tive um problema que estava ocorrendo porque o método .format() estava sendo aplicado ao conteúdo do template HTML, o que causava conflitos de substituição das chaves {} que fazem parte do código CSS. Como o CSS também utiliza chaves {} para definir blocos de estilo, o método .format() estava interpretando essas chaves como placeholders para formatação de string, o que gerava o erro.

Ao remover o uso do método .format() e definir diretamente o corpo do email como o conteúdo do template HTML, consegui evitar esse conflito e permitiu que o HTML fosse enviado sem alterações indesejadas ou erros de execução.


pip install python-decouple
