












import requests


def get_paypal_like_rate(from_currency, to_currency, amount=1.0, paypal_margin=0.035):
    # الخطوة 1: جلب السعر الحقيقي من exchangerate.host
    url = "https://api.exchangerate.host/convert"
    params = {
        "from": from_currency,
        "to": to_currency,
        "amount": amount
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if "result" not in data or data["result"] is None:
        raise Exception("فشل في الحصول على سعر الصرف.")
    
    real_rate = data["result"] / amount

    # الخطوة 2: تطبيق هامش بايبال (خصم 3.5%)
    paypal_rate = real_rate * (1 - paypal_margin)

    return real_rate, paypal_rate

# مثال: تحويل 1 USD إلى EUR
real, paypal_like = get_paypal_like_rate("USD", "EUR")

print(f"السعر الحقيقي: 1 USD = {real:.4f} EUR")
print(f"سعر تقريبي كما في PayPal: 1 USD ≈ {paypal_like:.4f} EUR")














