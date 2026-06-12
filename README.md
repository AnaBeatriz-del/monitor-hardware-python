Monitor Automático de Sistema em Python

Este projeto é um script de automação focado na análise de sistemas e resolução de problemas. Ele realiza o monitoramento contínuo dos recursos de hardware da máquina e gera logs automáticos, auxiliando na prevenção de falhas e lentidão.

Funcionalidades
* **Leitura de Hardware:** Coleta dados em tempo real do uso de Processador (CPU) e Memória RAM.
* **Análise de Armazenamento:** Verifica a capacidade e o espaço disponível no disco principal.
* **Troubleshooting Preventivo:** Emite alertas automáticos caso o uso de recursos ultrapasse limites seguros (ex: CPU ou RAM acima de 85%).
* **Automação de Logs:** Registra todo o histórico de leituras em um arquivo `log_sistema.txt` para auditoria e análise posterior.

Tecnologias Utilizadas
* **Python 3**
* **Bibliotecas nativas:** `platform`, `datetime`
* **Bibliotecas externas:** `psutil` (leitura de processos e utilização do sistema)

Como executar na sua máquina

1. Clone este repositório ou baixe o arquivo `monitor_sistema.py`.
2. Abra o terminal na pasta do projeto e instale a dependência necessária:
   `pip install psutil`
3. Execute o script:
   `python monitor_sistema.py`
