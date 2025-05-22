def classificar_alerta(alerta):
    sistema = alerta["sistema"].lower()
    mensagem = alerta["mensagem"].lower()

    # Alta prioridade
    if sistema in ["freio", "incendio", "descarrilamento", "motor"]:
        return "Alta"
    if "fogo" in mensagem or "fumaça" in mensagem:
        return "Alta"

    # Média prioridade
    if sistema in ["tracao", "energia", "bateria", "alagamento", "chuva_intensa", "temperatura_extrema"]:
        return "Média"
    if "queda de energia" in mensagem or "nível crítico" in mensagem:
        return "Média"

    # Baixa prioridade
    if sistema in ["porta", "comunicacao", "sensor"]:
        return "Baixa"
    if "perda de sinal" in mensagem or "falha de calibração" in mensagem:
        return "Baixa"

    # Default se não identificado
    return "Média"