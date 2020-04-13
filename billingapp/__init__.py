from .app import login_manager
from .app import app
from .controllers import *
from .models.Main import main
from .models.User import User
from .models.Customer import Customer
from .models.Enterprise import Enterprise
from .models.InvoiceConfig import InvoiceConfig
from .models.Product import Product
from .models.Main import main
import logging as lg

main.db.init_app(app)


@app.cli.command()
def init_db():
    main.db.drop_all()
    main.db.create_all()

    user = User("maher.isnard@gmail.com", "xxxxx", "Maher", "Isnard")

    enterprise = Enterprise("Maher Isnard", "10 rue test", "Mars", "33000",
                            "06 19 19 19 19",
                            "maher.isnard@gmail.com",
                            "<span class='font-weight-bold'>Coordonnées bancaires</span><br>" +
                            "Titulaire du compte : Maher Isnard <br>" +
                            "Banque : Revolut <br>" +
                            "IBAN : GB06 OKOK 0000 0000 0000 00 <br>" +
                            "CODE BIC : TESTBIC123", "123123123123")

    enterprise.user = user

    customer = Customer("Openclassrooms", "7 cité Paradis <br>75010 Paris", "", "", "")

    customer.enterprise = enterprise

    main.db.session.add(customer)

    invoice_config_a = InvoiceConfig("legal_infos_header", "Bla bla legal infos")
    invoice_config_b = InvoiceConfig("legal_infos_vat", "TVA non applicable, art. 293 B du CGI")
    invoice_config_c = InvoiceConfig("legal_infos_footer",
                                     "Conditions de paiement : paiement à réception de facture, à 30 jours. <br>" +
                                     "Indemnité forfaitaire pour frais de recouvrement due au " +
                                     "créancier en cas de retard de paiement: 40€ <br>" +
                                     "Siret: 12312312312312")

    main.db.session.add(enterprise)
    enterprise.invoice_config = [invoice_config_a, invoice_config_b, invoice_config_c]

    main.db.session.add(Product("Session de niveau d'expertise 1", "expertiseLv1", 30))
    main.db.session.add(Product("Session de niveau d'expertise 2", "expertiseLv2", 35))
    main.db.session.add(Product("Session de niveau d'expertise 3", "expertiseLv3", 40))
    main.db.session.add(Product("Session de niveau d'expertise 1 (no show)", "expertiseLv1NoShow", 15))
    main.db.session.add(Product("Session de niveau d'expertise 2 (no show)", "expertiseLv2NoShow", 17.50))
    main.db.session.add(Product("Session de niveau d'expertise 3 (no show)", "expertiseLv3NoShow", 20))
    main.db.session.add(
        Product("Prime de cooptation (merci de préciser le nom des mentors cooptées)", "cooptation", 30))

    main.db.session.add(user)
    main.db.session.commit()
    lg.warning("Database Initialized with dummy data")


@app.template_filter()
def session_total(items):
    return sum(item.qty for item in items)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


app.jinja_env.filters['session_total'] = session_total
