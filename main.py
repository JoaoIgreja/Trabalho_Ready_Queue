class Processo:
    def __init__(self, nome, prioridade, tempo_execucao):
        self.nome = nome
        self.prioridade = prioridade
        self.tempo_execucao = tempo_execucao

# Função para obter a prioridade de um processo
def obter_prioridade(processo):
    return processo.prioridade

if __name__ == "__main__":
    processos = [
        Processo("P1", 2, 5),
        Processo("P2", 1, 2),
        Processo("P3", 2, 8),
        Processo("P4", 3, 1),
        Processo("P5", 5, 1),
        Processo("P6", 4, 16),
    ]

    print("Simulador de ready queue (PS):")

    # Ordenar os processos por prioridade usando a função de chave personalizada
    processos.sort(key=obter_prioridade)

    tempo_total = 0

    for processo in processos:
        if (processo.tempo_execucao == 1):
            print(f" {processo.nome} Está Pronto para ser Executado (Prioridade {processo.prioridade}) utilizando {processo.tempo_execucao} unidade de tempo")
            tempo_total += processo.tempo_execucao -1
        else:
            print(f" {processo.nome} Está Pronto para ser Executado (Prioridade {processo.prioridade}) utilizando {processo.tempo_execucao} unidades de tempo")
        tempo_total += processo.tempo_execucao

    if (tempo_total != 1):
        print(f"Tempo total de execução: {tempo_total} unidades de tempo.")
    else:
         print(f"Tempo total de execução: {tempo_total} unidade de tempo.")
