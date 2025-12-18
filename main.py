import subprocess
import inquirer

while True:
    def escolha(esco):
        if 'Ver informações de ip' in esco['Escolha']:
            cmd = "ipconfig"
        else:
            cmd = " "
        return cmd

    def main():
        opcoes = [
            inquirer.List(
            "Escolha",
                message="O que você deseja fazer no cmd ?",
                choices=["Ver informações de ip", "Outro"],
            ),
        ]
        esco = inquirer.prompt(opcoes)
        comando = escolha(esco)
        executar = subprocess.run([comando], shell=True)

    main()

