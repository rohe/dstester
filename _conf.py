from saml2 import BINDING_HTTP_REDIRECT
from saml2 import BINDING_HTTP_POST
from saml2.extension.idpdisc import BINDING_DISCO
from saml2.saml import NAME_FORMAT_URI

#BASE= "http://localhost:8087"
BASE = "https://lingon.ladok.umu.se:8087"

CONFIG = {
    "entityid": "%s/sp.xml" % BASE,
    "description": "My SP",
    "service": {
        "sp": {
            "name": "DS Tester",
            "endpoints": {
                "assertion_consumer_service": [
                    ("%s/acs/redirect" % BASE, BINDING_HTTP_REDIRECT),
                    ("%s/acs/post" % BASE, BINDING_HTTP_POST)],
                "single_logout_service": [
                    ("%s/slo" % BASE, BINDING_HTTP_REDIRECT)],
                "discovery_response": [
                    ("%s/disco" % BASE, BINDING_DISCO)
                ]
            },
        }
    },
    "debug": 1,
    "key_file": "pki/mykey.pem",
    "cert_file": "pki/mycert.pem",
    "attribute_map_dir": "./attributemaps",
    "metadata": {"mdfile": ["./swamid2.md"]},
    # -- below used by make_metadata --
    "organization": {
        "name": "ITS",
        "display_name": [("Umea Universitet - ITS", "se"),
                         ("Umea Universitet ITS", "en")],
        "url": "http://www.its.umu.se",
    },
    "contact_person": [
        {
            "given_name": "Roland",
            "sur_name": "Hedberg",
            "email_address": ["dirg@its.umu.se"],
            "contact_type": "technical",
        },
    ],
    "xmlsec_binary": "/opt/local/bin/xmlsec1",
    "name_form": NAME_FORMAT_URI,
    "logger": {
        "rotating": {
            "filename": "sp.log",
            "maxBytes": 1000000,
            "backupCount": 5,
        },
        "loglevel": "debug",
    }
}
