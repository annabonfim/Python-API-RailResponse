import oracledb
from datetime import datetime

# Substitua pelos dados do seu banco (esses são exemplos!)
conn = oracledb.connect(
    user="rm559561",
    password="200702",
    dsn="oracle.fiap.com.br:1521/ORCL"  # ou outro que apareça no seu SQL Developer
)

def salvar_no_banco(alerta):
    sql = """
        INSERT INTO ALERTAS (TREM, SISTEMA, MENSAGEM, PRIORIDADE, HORA)
        VALUES (:1, :2, :3, :4, TO_TIMESTAMP(:5, 'YYYY-MM-DD"T"HH24:MI:SS.FF'))
    """
    with conn.cursor() as cursor:
        cursor.execute(sql, (
            alerta["trem"],
            alerta["sistema"],
            alerta["mensagem"],
            alerta["prioridade"],
            alerta["hora"]
        ))
    conn.commit()
    print(f"[DB] Alerta salvo: {alerta['mensagem']}")

def buscar_todos():
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT ID_ALERTA, TREM, SISTEMA, MENSAGEM, PRIORIDADE, HORA
            FROM ALERTAS
            ORDER BY HORA DESC FETCH FIRST 50 ROWS ONLY
        """)
        colunas = [col[0].lower() for col in cursor.description]
        return [dict(zip(colunas, row)) for row in cursor.fetchall()]


# Funções para atualizar e deletar alertas
def atualizar_alerta(id_alerta, novos_dados):
    sql = """
        UPDATE ALERTAS
        SET TREM = :1,
            SISTEMA = :2,
            MENSAGEM = :3,
            PRIORIDADE = :4,
            HORA = TO_TIMESTAMP(:5, 'YYYY-MM-DD"T"HH24:MI:SS.FF')
        WHERE ID_ALERTA = :6
    """
    with conn.cursor() as cursor:
        cursor.execute(sql, (
            novos_dados["trem"],
            novos_dados["sistema"],
            novos_dados["mensagem"],
            novos_dados["prioridade"],
            novos_dados["hora"],
            id_alerta
        ))
    conn.commit()
    print(f"[DB] Alerta {id_alerta} atualizado.")

def deletar_alerta(id_alerta):
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM ALERTAS WHERE ID_ALERTA = :1", (id_alerta,))
    conn.commit()
    print(f"[DB] Alerta {id_alerta} deletado.")