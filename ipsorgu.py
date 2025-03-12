import requests

def get_ip():
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        ip = response.json().get("ip", "Bilinmiyor")
        return ip
    except Exception as e:
        return f"Hata: {e}"

if __name__ == "__main__":
    print(f"IP Adresiniz: {get_ip()}")
