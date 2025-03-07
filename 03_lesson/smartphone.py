class Smartphone:
    kind_phone = "Nokia"
    model_phone = "2210"
    number_phone = "89999999999"
    def __init__(self, kind_phone, model_phone, number_phone ):
        self.kind_phone = kind_phone
        self.model_phone = model_phone
        self.number_phone = number_phone
    def __str__(self):
        return f"{self.kind_phone} - {self.model_phone}. {self.number_phone}"