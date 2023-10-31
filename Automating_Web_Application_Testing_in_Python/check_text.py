from zeep import Client, Settings
import yaml

with open("config.yaml", encoding="utf-8") as f:
    data = yaml.safe_load(f)

settings = Settings(strict=False)
client = Client(wsdl=data.get("url"), settings=settings)

# h = print(client.service.checkText("Карава"))
# print(h[0]['s'])

def check_text(word):
    return client.service.checkText(word)[0]['s']

# print(check_text("гряз"))