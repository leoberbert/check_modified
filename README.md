# Check Modified

Script simples que verifica se um arquivo de log passado como entrada, está a mais de 1 hora sem incremento, caso afirmativo, envia uma mensagem(webhook) json para outra API através do método POST.

```console

./check_modified.py /tmp/application.log my_application_name

URGENTE - Aplicacao my_application_name na maquina dolly sem incrementar o log /tmp/application.log a mais de 1h.

```

