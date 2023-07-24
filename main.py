import requests

w = requests.get
token = input("Ingresa el token del usuario > ")
user = w("https://discord.com/api/users/@me", headers={'Authorization': token})
Data = user.json()

if user.status_code == 401:
    print("Token Inválido")
    exit()

rguilds = w("https://discord.com/api/users/@me/guilds", headers={'Authorization': token})
rfriends = w("https://discord.com/api/v10/users/@me/relationships", headers={'Authorization': token})

guilds = rguilds.json()
friends = rfriends.json()

lang_mappings = {
    'es': 'Spanish',
    'en': 'English',
    'da': 'Dansk',
    'de': 'Deutsch',
    'fr': 'French',
    'hr': 'Croatian',
    'it': 'Italian',
    'lt': 'Lithuanian',
    'hu': 'Hungarian',
    'nl': 'Nederlands',
    'no': 'Norwegian',
    'pl': 'Polish',
    'br': 'Brazil',
    'ro': 'Romanian',
    'fi': 'Suomi',
    'sv': 'Swedish',
    'vi': 'Vietnamese',
    'tr': 'Turkish',
    'cs': 'Czech',
    'el': 'Greek',
    'bg': 'Bulgarian',
    'ru': 'Russian',
    'uk': 'Ukrainian',
    'hi': 'Hindi',
    'th': 'Thai',
    'zh': 'Chinese',
    'ja': 'Japanese',
    'ko': 'Korean',
}

lang_prefix = Data['locale'].split('-')[0].lower()
language = lang_mappings.get(lang_prefix, 'Unknown')

user_info = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Usuario: {user}#{discriminator}
Telefono: {phone}
ID: {id}
Correo: {email}
2fA: {mfa_enabled}
Verificado: {verified_enabled}
Nsfw Allowed: {nsfw_enabled}
Lenguaje: {language}
Servidores: {num_guilds}
Amigos: {num_friends}
Bio: {bio}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""".format(user=Data['username'], discriminator=Data['discriminator'],
        phone=Data['phone'] or "False", id=Data['id'], email=Data['email'] or "False",
        mfa_enabled=Data['mfa_enabled'], language=language,
        num_guilds=len(guilds), num_friends=len(friends), 
        verified_enabled=Data['verified'] or "False", bio=Data['bio'] or "N/A",
        nsfw_enabled=Data['nsfw_allowed'] or "False")[1:]
print(user_info)
