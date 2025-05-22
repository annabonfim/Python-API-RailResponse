import random
import time
from notificacao import enviar_alerta_critica

estacoes_linha_8 = [
    "Júlio Prestes", "Palmeiras-Barra Funda", "Lapa", "Domingos de Moraes", "Imperatriz Leopoldina",
    "Presidente Altino", "Osasco", "Comandante Sampaio", "Itapevi", "Amador Bueno", "Ambuitá", "Santa Rita"
]

estacoes_linha_9 = [
    "Osasco", "Presidente Altino", "Ceasa", "Vila Lobos-Jaguaré", "Cidade Universitária", "Pinheiros",
    "Hebraica-Rebouças", "Cidade Jardim", "Vila Olímpia", "Berrini", "Morumbi-Claro", "Granja Julieta",
    "João Dias", "Santo Amaro", "Socorro", "Jurubatuba-Senac", "Autódromo", "Primavera-Interlagos",
    "Grajaú", "Bruno Covas-Mendes-Vila Natal"
]

def gerar_alerta_simulado():
    sistemas = [
        ("freio", "falha no sistema de freio"),
        ("tracao", "problema de tração detectado"),
        ("energia", "queda de energia em estação"),
        ("bateria", "nível crítico de bateria"),
        ("motor", "falha no motor do trem"),
        ("porta", "porta travada"),
        ("incendio", "detecção de fumaça no vagão"),
        ("descarrilamento", "possível descarrilamento detectado"),
        ("alagamento", "água invadindo trecho 8"),
        ("chuva_intensa", "chuva acima do limite operacional"),
        ("temperatura_extrema", "calor acima de 42ºC na via"),
        ("comunicacao", "perda de sinal com trem"),
        ("sensor", "falha de calibração nos sensores")
    ]
    sistema, descricao = random.choice(sistemas)
    linha = random.choice(["8", "9"])
    estacao = random.choice(estacoes_linha_8 if linha == "8" else estacoes_linha_9)

    return {
        "trem": random.randint(1000, 9999),
        "sistema": sistema,
        "mensagem": f"🚨 {descricao} detectada na estação {estacao}, Linha {linha}.",
        "linha": linha,
        "estacao": estacao
    }

if __name__ == "__main__":
    alerta_teste = {
        "trem": "9999",
        "sistema": "freio",
        "mensagem": "🚨 Teste de alerta crítico via simulador!",
        "hora": "2025-05-11T22:00:00",
        "prioridade": "Alta"
    }
    enviar_alerta_critica(alerta_teste)