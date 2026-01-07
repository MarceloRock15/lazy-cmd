import subprocess
import inquirer


def escolha(esco):
    if "Ver informações de ip" in esco["Escolha"]:
        cmd = "ipconfig"
    elif "Mostrar estatísticas de rede" in esco["Escolha"]:
        cmd = "netstat"
    elif "Limpar cachê temporário" in esco["Escolha"]:
        cmd = r"del /q/f/s C:\Windows\Temp\*"
    elif "Ver especificações de hardware" in esco["Escolha"]:
        cmd = "systeminfo"
    elif "Listar processos em execução" in esco["Escolha"]:
        cmd = "tasklist"
    elif "Mostrar versão do Windows" in esco["Escolha"]:
        cmd = "ver"
    elif "Mostrar variáveis de ambiente" in esco["Escolha"]:
        cmd = "set"
    elif "Verificar o disco rígido" in esco["Escolha"]:
        cmd = "chkdsk"
    elif "Exibir drivers instalados" in esco ["Escolha"]:
        cmd = "driverquery"
    return cmd

def main():
    while True:
        opcoes = [
            inquirer.List(
            "Escolha",
                message="O que você deseja fazer no cmd ?",
                choices=["Ver informações de ip",
                        "Mostrar estatísticas de rede",
                        "Limpar cachê temporário",
                        "Ver especificações de hardware",
                        "Listar processos em execução",
                        "Mostrar versão do Windows",
                        "Mostrar variáveis de ambiente",
                        "Verificar o disco rígido",
                        "Exibir drivers instalados",
                        "Sair" ],
            ),
        ]
        esco = inquirer.prompt(opcoes)
        if "Sair" in esco["Escolha"]:
            break
        comando = escolha(esco)

        try:
            executar = subprocess.run(comando, shell=True)
        except subprocess.CalledProcessError as err:
            print(f"Erro ao executar o comando: {err}")
        except PermissionError:
            print(f"Você não tem as permissões necessárias para executar esse comando. Tente abrir o arquivo executável com administrador.")

main()

