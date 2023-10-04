class Processo:
    def __init__(self, nome, prioridade, tempo_execucao):
        self.nome = nome
        self.prioridade = prioridade
        self.tempo_execucao = tempo_execucao

def obter_prioridade(processo):
    return processo.prioridade

def obter_tempo_execucao(processo):
    return processo.tempo_execucao

if __name__ == "__main__":
    processos = [
        Processo("P1", 2, 5),
        Processo("P2", 1, 2),
        Processo("P3", 2, 8),
        Processo("P4", 3, 1),
        Processo("P5", 5, 1),
        Processo("P6", 4, 16),
    ]

    print("\nSimulador de ready queue (PS):")

    processos.sort(key=obter_prioridade)

    print("Prioridade:")
    tempo_total_prioridade = 0

    for processo in processos:
        if processo.tempo_execucao == 1:
            print(f" {processo.nome} Está Pronto para ser Executado (Prioridade {processo.prioridade}) utilizando {processo.tempo_execucao} unidade de tempo")
            tempo_total_prioridade += processo.tempo_execucao - 1
        else:
            print(f" {processo.nome} Está Pronto para ser Executado (Prioridade {processo.prioridade}) utilizando {processo.tempo_execucao} unidades de tempo")
        tempo_total_prioridade += processo.tempo_execucao

    if tempo_total_prioridade != 1:
        print(f"{tempo_total_prioridade} unidades de tempo.")
    else:
         print(f"{tempo_total_prioridade} unidade de tempo.")

   
    processos.sort(key=obter_tempo_execucao)

    print("\nSJF:")
    tempo_total_sjf = 0

    for processo in processos:
        if processo.tempo_execucao == 1:
            print(f" {processo.nome} Está Pronto para ser Executado (Tempo de Execução {processo.tempo_execucao}) utilizando {processo.tempo_execucao} unidade de tempo")
            tempo_total_sjf += processo.tempo_execucao - 1
        else:
            print(f" {processo.nome} Está Pronto para ser Executado (Tempo de Execução {processo.tempo_execucao}) utilizando {processo.tempo_execucao} unidades de tempo")
        tempo_total_sjf += processo.tempo_execucao

    if tempo_total_sjf != 1:
        print(f"{tempo_total_sjf} unidades de tempo.")
    else:
         print(f"{tempo_total_sjf} unidade de tempo.\n")
