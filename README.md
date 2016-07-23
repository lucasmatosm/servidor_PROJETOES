PRÉ-REQUISITOS


1 - Fazer o Download dos programas:
- Visual C++ (https://download.microsoft.com/download/d/2/4/d242c3fb-da5a-4542-ad66-f9661d0a8d19/vcredist_x64.exe)
- Wampserver (http://sourceforge.net/projects/wampserver/files/WampServer%203/WampServer%203.0.0/wampserver3_x64_apache2.4.17_mysql5.7.9_php5.6.16_php7.0.0.exe)
- Visual C++ for Python (https://download.microsoft.com/download/7/9/6/796EF2E4-801B-4FC4-AB28-B59FBF6D907B/VCForPython27.msi)
- MySQL Conector C (https://dev.mysql.com/get/Downloads/Connector-C/mysql-connector-c-6.0.2-win32.msi)
2 - Instalar os arquivos conforme ordem de download
3 - Instalar o package do ambiente virtual através do comando 'pip install mkvirtualenvwrapper-win' no windows
4 - Criar o ambiente virtual através do comando 'mkvirtualenv NOME_DO_AMBIENTE' windows
5 - Entrar no ambiente virtual através do comando 'workon NOME_DO_AMBIENTE'
6 - Instalar as dependências:
- pip install django
- pip install djangorestframework
- pip install django-rest_auth
- pip install Pillow
7 - Instalar a dependencia do MySQL-python através do comando 'pip install mysql-python'
* Método alternativo em caso de falha: Download do .whl (http://www.lfd.uci.edu/~gohlke/pythonlibs/6kbpejrn/MySQL_python-1.2.5-cp27-none-win_amd64.whl) e execução do comando 'pip install MySQL_python-1.2.5-cp27-none-win_amd64.whl' no local do download.

INSTRUÇÕES

1 - Abrir o programa Wampserver (baixado e instalado na seção de pré-requisitos)
2 - Aguardar o ícone (canto inferior direito) ficar verde
3 - Abrir http://localhost/phpmyadmin/ com nome de usuario 'root' e sem senha
4 - No menu da esquerda clicar em 'New' para adicionar o BD
5 - Criar o BD com nome 'povmt'
6 - Abrir o CMD na pasta do repositório
7 - Executar o comando 'workon NOME_DO_AMBIENTE_CRIADO'
8 - Executar o comando 'python manage.py makemigrations' 
9 - Executar o comando 'python manage.py migrate'
9 - Executar o comando 'python manage.py runserver'
