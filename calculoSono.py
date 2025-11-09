from datetime import datetime, timedelta

def calcular_horarios_para_dormir(acordar_str):
    formato = "%H:%M"
    
    try:
        # Converte o horário informado em datetime
        horario_acordar = datetime.strptime(acordar_str, formato)

        # Cada ciclo de sono dura aproximadamente 90 minutos
        ciclo = timedelta(minutes=90)

        # Número de ciclos a considerar (adultos: 4 a 6 ciclos)
        ciclos = [6, 5, 4]

        # Tempo extra para pegar no sono (aproximadamente 15 minutos)
        tempo_para_dormir = timedelta(minutes=15)

        # Explicação sobre os ciclos (apenas uma vez)
        print(f"\nCada ciclo de sono dura cerca de 90 minutos. Dormir múltiplos ciclos (de 4 a 6) ajuda a acordar mais descansado.\n")

        print(f"Se você quer acordar às {acordar_str}, tente dormir nestes horários:\n")

        for qtd_ciclos in ciclos:
            # Calcula o horário para deitar subtraindo os ciclos e o tempo para pegar no sono
            tempo_dormir = horario_acordar - (ciclo * qtd_ciclos) - tempo_para_dormir
            print(f"- {tempo_dormir.strftime('%H:%M')} → {qtd_ciclos} ciclos de sono (~{qtd_ciclos * 1.5:.1f} horas de sono)")

        print("\n Dica: Deitar um pouco antes do horário calculado ajuda a pegar no sono mais tranquilo. ")

    except ValueError:
        print("Formato inválido! Use o formato HH:MM (ex: 06:30)")

# Exemplo de uso:
entrada = input("Digite o horário que deseja acordar (HH:MM): ")
calcular_horarios_para_dormir(entrada)
