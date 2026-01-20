import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "usuarios.csv"
OUTPUT_PATH = BASE_DIR / "output" / "mensagens.csv"

print("🔄 Iniciando extração dos dados...")
print(f"📂 Procurando arquivo em: {DATA_PATH}")

if not DATA_PATH.exists():
    raise FileNotFoundError(f"Arquivo não encontrado: {DATA_PATH}")

df = pd.read_csv(DATA_PATH)

def gerar_mensagem(nome, conta):
    return (
        f"Olá {nome}! 🎉 "
        f"Temos novidades exclusivas disponíveis para sua conta {conta}. "
        f"Aproveite nossos benefícios especiais!"
    )

df["mensagem"] = df.apply(
    lambda row: gerar_mensagem(row["nome"], row["conta"]),
    axis=1
)

OUTPUT_PATH.parent.mkdir(exist_ok=True)
df.to_csv(OUTPUT_PATH, index=False)

print("🚀 Processo ETL finalizado com sucesso!")
print("📄 Arquivo gerado em:", OUTPUT_PATH)