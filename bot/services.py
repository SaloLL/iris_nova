# bot/services.py

class MessageService:
    def process_message(self, text: str) -> dict:
        """
        Procesa el texto del usuario.
        Retorna un diccionario con resultado.
        """

        text = text.strip()

        if text.startswith("+"):
            try:
                value = int(text.replace("+", "").strip())
                print(f"[LOG] Valor recibido: {value}")
                return {"status": "success", "value": value}
            except ValueError:
                return {"status": "error", "message": "Formato inválido. Usa: + 5000"}

        return {"status": "unknown"}