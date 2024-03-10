# CLIMA API ⛅

Introdução-📝
Neste projeto feito com Python e o Framework Django, consome uma **[API de clima](https://openweathermap.org/)**, e retorna todas as cidades do mundo para que o usuário consiga verificar o clima da cidade de seu interesse.

## Requisitos do Sistema

- Certifique-se de ter o **[Python](https://www.python.org/downloads/)** instalado em seu ambiente de desenvolvimento. Recomenda-se a versão mais recente. 
- Utilize a IDE de preferência, mas recomendo fortemente o **[VScode](https://code.visualstudio.com/download)**.
 
## Como instalar 💾
- Primeiramente, clone ou faça o download deste repositório: [https://github.com/GabrielMontenegrOL/FABRICA_DESAFIO_2024.1.git](https://github.com/GabrielMontenegrOL/FABRICA_DESAFIO_2024.1.git)
- Abra a pasta no VSCode.
- No terminal ou pressione CTRL + J.
- Digite: `python -m venv venv` (Comando para criar sua virtual environment).
- Após criar, digite `.\venv\Scripts\Activate.ps1` (Para ativar sua virtual environment).
- Instale as dependências com o comando: `pip install -r requirements.txt`.
- Execute os comandos de migração:
  - `python manage.py makemigrations`
  - `python manage.py migrate`
- Inicie o programa:
  - `python manage.py runserver`
    
## Utilização ⌨
- Clique para rodar:
  
![Screenshot 2024-03-10 002844](https://github.com/GabrielMontenegrOL/FABRICA_DESAFIO_2024.1/assets/131418339/b0b1b926-f034-4e2f-bdbc-314f5b5a9629)

- Bom uso:
  
![image](https://github.com/GabrielMontenegrOL/FABRICA_DESAFIO_2024.1/assets/131418339/f1ed1895-374e-46ba-b9ac-c9b96d597c84)

##Como criar o seu do ZERO🤝

- Crie uma pasta sem nada do vs code
- Abra o terminal (CTRL + J)
- Crie uma pasta nele: `python -m venv venv `
- Ative sua VM: `\venv\Scripts\Activate.ps1`

 
- Instale o DJANGO:
- `pip install django`
- `pip install djangorestframework` Se for usar HTML | Template Não é necessário.
- `pip install requests`
- `pip freeze > requirements.txt`

 
- Criando suas pastas 📂: 
- `django-admin startproject (nome) .` COLOCA O .e o nome sem ()
- `django-admin startapp (nome)` nome sem ()

 
- Modifique ⚙ sua settings.py:
- `--> projeto --> settings.py`
`INSTALLED_APPS =` 
`['rest_framework',`
`'meuprimeiroapp',`

- e dps vá no final e:
mude para `pt-br`
mude para `'America/Recife'`

-Crie uma pasta API 📂: 
`serializers.py`
`urls.py`
`viewsets.py`

-Agora adpete suas aplicações com o suas preferências! 🧠

##Guia de comandos para te ajudar 🤝:

`python manage.py createsuperusers` Cria um login
`python manage.py runserver` Rodar server
`(ctrl + c)` cancelar o runserve 

-Migrações: 
`python manage.py makemigrations`
`python manage.py migrate`

## Exemplos de API para aplicar:
- https://viacep.com.br/ 
- https://pokeapi.co/
- https://openweathermap.org/







  
  








