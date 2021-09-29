# Speedtest in Excel with Python

### Speedtest no Excel com Python

-----

### Introduction (us_EN)

I've noticed that my internet is not only unstable but does not deliver the speed that I've subscribed.

From time to time I measure the values directly on Speedtest.net, but I decided to make this little script to automate
my analysis and download the speed data from my internet every 15 minutes to really be sure if they are delivering or
not what was hired.

After downloading the data, 'Download' 'Upload' and 'Ping' speeds are automatically saved into a csv file -
database.csv.

I created an Excel spreadsheet (speedtest_results.txt) to read this csv and to show a graph of my average daily speed.

The run.py code is available here, if you want to test it by yourself.

If you are not a Python programmer but are interested in running the program, I generated an .EXE (for Windows) that
runs the same code, but without having to install anything. The file is windows_runner.exe. In that case, please read
the windows_runner_readme.md.

### How to run this code

#### Installing the packages

First things first. Please, install the required python packages by doing:

```commandline
pip install -r requirements.txt
```

#### Running the file

Open the run.py file and set the desired fetch interval

```python
REPEAT_MODE = True  # If False will run only once
MINUTES_TO_RERUN = 15
```

After running the script for the first time, a file called database.csv will be created in the same folder.

That will be the file that Excel will seek to update its internal database and graphs.

#### Updating the Excel Sheet

After having some data in the database.csv you can open the spreadsheet "speedtest_results.xlsm" (works in Excel 2016+
or Excel part of Office 365).

You'll have to update the spreadsheet data. For that you can go to:

- Menu > Data > Refresh All

----

### Introdução (pt_BR)

Venho notando que a minha internet além de instável não entrega a velocidade que eu contratei.

De vez em quando eu até meço os valores diretamente pelo Speedtest, porém eu decidi fazer esse scriptzinho para
automatizar a análise e baixar os dados da velocidade da minha internet a cada 15 minutos para realmente ter certeza se
eles estão entregando ou não o que foi contratado.

Então as velocidades de 'Download,' 'Upload' e 'Ping' são salvas automaticamente num arquivo csv chamado 'database.csv'
na mesma pasta do script.

Criei uma planilha em Excel para ler este csv para mostrar um gráfico da minha velocidade média diária.

Estou disponibilizando o código fonte em Python pra vc testar na sua internet também.

Caso não seja programador Python mas tenha interesse em rodar programa, gerei um .EXE (para Windows) que roda o mesmo
código, mas sem precisar instalar nada. O arquivo é o "windows_runner.exe"

### How to run this code

#### Installing the packages

First things first. Please, install the required python packages by doing:

```commandline
pip install -r requirements.txt
```

#### Rodando o arquivo

Abra o arquivo run.py e defina os parâmetros de execução

```python
REPEAT_MODE = True  # Se False o arquivo rodará apenas 1x
MINUTES_TO_RERUN = 15
```

Depois de rodar o script pela primeira vez, um arquivo chamado 'database.csv' será criado na mesma pasta.

Este será o arquivo que o Excel procurará para atualizar a sua referência e seus gráficos.

#### Atualizando a planilha do Excel

Depois de ter alguns dados no arquivo 'database.csv', você pode abrir a planilha "speedtest_results.xlsm" (que funciona
no Excel 2016+ ou parte do Office 365)

Você precisará atualizar a planilha para que os dados mais recentes apareçam. Para isto, vá para:

- Menu > Dados > Atualizar Tudo

#### Tags

csv, python, excel, speedtest, wifi speed, internet speed, internet connection, wifi monitor, monitoring wifi,
monitoring internet speed, speedtest monitor, download speed monitor, upload speed monitor