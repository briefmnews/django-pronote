# django-pronote
Handle CAS login for Pronote (index éducation)

## Installation
Install with [pip](https://pypi.org/):
```
pip install -e git://github.com/briefmnews/django-pronote.git@main#egg=pronote
```

## Setup
In order to make `django-pronote` works, you'll need to follow the steps below.

### Settings
First you need to add the following configuration to your settings:

```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',

    'pronote',
    ...
)
```

### Mandatory settings
Here is the list of all the mandatory settings:
```python
PRONOTE_API_KEY
PRONOTE_RESSOURCE_ID
PRONOTE_TERMS_AND_CONDITIONS_URL
PRONOTE_RESSOURCE_TITLE
PRONOTE_URL
```

### Optional settings
The optional settings with their default values:
```python
PRONOTE_RESSOURCE_OLD_ID (default: None)
PRONOTE_PUBLISHER (default: None)
PRONOTE_RESSOURCE_TYPE (default: None)
PRONOTE_FAMILY_ID = (default: None)
PRONOTE_FAMILY_LABEL = (default: None)
PRONOTE_FAMILY_JUSTIFICATION = (default: None)
PRONOTE_PERSONAL_INFORMATION_DEFINITION_DATA = (default: ())
PRONOTE_PERSONAL_INFORMATION_DEFINITION_JUSTIFICATION = (default: [])
PRONOTE_PUBLIC = (default: ())
PRONOTE_PUBLIC_QUOTAS = (default: [])
PRONOTE_DISCIPLINES = (default: ())
PRONOTE_MEFSTAT11 = (default: ())
PRONOTE_URL_MOBILE_APP = (default: None)
PRONOTE_API_SUPPORT = (default: ())
PRONOTE_DESCRIPTION = (default: None)
PRONOTE_KEYWORDS = (default: ())
```