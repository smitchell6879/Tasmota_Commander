import requests

class SwitchModel:
    def __init__(self, address, user=None, pwd=None) -> None:
        if user:
            self.url = f"http://{address}/cm?user={user}&password={pwd}&"
        else:
            self.url = f"http://{address}/cm?"

def toggle(SwitchModel):
    url = f"{SwitchModel.url}cmnd=Power%20TOGGLE"
    req = requests.post(url=url)
    print(req.status_code)

def on(SwitchModel):
    url = f"{SwitchModel.url}cmnd=Power%20On"
    req = requests.post(url=url)
    print(req.status_code)

def off(SwitchModel):
    url = f"{SwitchModel.url}cmnd=Power%20off"
    req = requests.post(url=url)
    print(req.status_code)