import psutil
import platform
import datetime

def registrar_log(mensagem):
    # função para salvar as informações em um arquivo de texto e mostrar na tela 
    data_hora = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    linha = f"[{data_hora}] {mensagem}\n" # CORRIGIDO: \n ao invés de /n

    # salvar o log no arquivo log_sistema.txt
    with open("log_sistema.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(linha)
    print(linha.strip())

def verificar_sistema():
    # função principal que faz a leitura do hardware.
    registrar_log("--- Iniciando verificação do sistema ---")

    # Sistema operacional
    so = platform.system()
    versao = platform.release()
    registrar_log(f"Sistema operacional: {so} {versao}")

    # Processador (cpu)
    cpu_uso = psutil.cpu_percent(interval=1)
    registrar_log(f"Uso da CPU: {cpu_uso}%")

    # Memoria ram
    memoria = psutil.virtual_memory()
    ram_total = round(memoria.total / (1024 ** 3), 2)
    ram_uso = memoria.percent
    registrar_log(f"Uso da memoria RAM: {ram_uso}% (Total: {ram_total} GB)")

    # Disco (CORRIGIDO: Faltava ler os dados do disco antes de fazer o alerta)
    disco = psutil.disk_usage('/')
    disco_uso = disco.percent
    registrar_log(f"Uso do Disco: {disco_uso}%")

    # Alertas de prevenção (troubleshooting automatico)
    if cpu_uso > 85:
        registrar_log("ALERTA: Uso de CPU muito alto! Risco de lentidão ou travamento.")

    if ram_uso > 85:
        registrar_log("ALERTA: Uso de RAM muito alto! Verifique processos pesados.")

    if disco_uso > 90: 
        registrar_log("ALERTA: Pouco espaço no disco principal!")

    registrar_log("--- Verificação Concluída ---\n")

# CORRIGIDO: Essas linhas agora estão totalmente encostadas à esquerda
if __name__ == "__main__":
    verificar_sistema()