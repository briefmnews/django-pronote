SECRET_KEY = "dump-secret-key"

ROOT_URLCONF = "pronote.urls"

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.admin",
    "pronote",
)

PRONOTE_API_KEY = "test"
PRONOTE_RESSOURCE_ID = "briefme"
PRONOTE_TERMS_AND_CONDITIONS_URL = "https://www.brief.me/gar/cgu/"
PRONOTE_RESSOURCE_TITLE = "Brief.me"
PRONOTE_URL = "https://www.brief.me"
PRONOTE_RESSOURCE_OLD_ID = "briefme-old"
PRONOTE_PUBLISHER = "Brief.me"
PRONOTE_RESSOURCE_TYPE = "Manuel"
PRONOTE_FAMILY_ID = "1234"
PRONOTE_FAMILY_LABEL = "test label"
PRONOTE_FAMILY_JUSTIFICATION = "hello"
PRONOTE_PERSONAL_INFORMATION_DEFINITION_DATA = (["Nom", "Prenom"], ["Prenom"])
PRONOTE_PERSONAL_INFORMATION_DEFINITION_JUSTIFICATION = ["test 0", "test 1"]
PRONOTE_PUBLIC = ("Professeur", "Elèves")
PRONOTE_PUBLIC_QUOTAS = ["2", "3"]
PRONOTE_DISCIPLINES = ("041400", "040600")
PRONOTE_MEFSTAT11 = ("10010012110", "21110010012")
PRONOTE_URL_MOBILE_APP = "https://www.brief.me"
PRONOTE_API_SUPPORT = ("ajoutPanier", "renduPJTAF")
PRONOTE_DESCRIPTION = "Un test de description"
PRONOTE_KEYWORDS = ("key 1",)
