from .Main import main


class InvoiceConfig(main.db.Model):
    id = main.db.Column(main.db.Integer, primary_key=True)
    key = main.db.Column(main.db.String(200), nullable=False)
    value = main.db.Column(main.db.String(200), nullable=False)
    enterprise = main.db.relationship("Enterprise", backref=main.db.backref("invoice_config", lazy='dynamic'))
    enterprise_id = main.db.Column(main.db.Integer, main.db.ForeignKey("enterprise.id"))

    def __init__(self, key, value):
        self.key = key
        self.value = value

    @staticmethod
    def get_config_value(key, enterprise_id):
        return InvoiceConfig.query.filter_by(key=key, enterprise_id=enterprise_id).one().value