




































































































#!/usr/bin/env python3
"""
lucas_lehmer.py




is : ( ( 2 ** (82_589_933) ) - 1 ) a prime number .






تحقق من أن M_p = 2^p - 1 عدد أولي باستخدام اختبار Lucas-Lehmer
(مناسب فقط للأعداد من شكل ميرسين حيث p يجب أن يكون أولياً).

مثال:
    python3 lucas_lehmer.py 7
    python3 lucas_lehmer.py 31
"""

import sys
import time
import random

# ---------- Miller-Rabin (اختبار احتمالي لأعداد p الصغيرة نسبياً) ----------
def is_probable_prime(n, k=8):
    """Miller-Rabin primality test (احتمالي). k = عدد الجولات."""
    if n < 2:
        return False
    # بسيطات
    small_primes = [2,3,5,7,11,13,17,19,23,29]
    for sp in small_primes:
        if n % sp == 0:
            return n == sp

    # اكتشاف d and r such that n-1 = 2^r * d (d odd)
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # اختبارات عشوائية أساساتها a
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        composite = True
        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                composite = False
                break
        if composite:
            return False
    return True

# ---------- Lucas-Lehmer ----------
def lucas_lehmer_test(p):
    """
    يرجع True إذا كان M_p = 2^p - 1 عددًا أوليًا، وإلا False.
    يفترض p > 2 و p عدد أولي.
    """
    if p == 2:
        return True  # M_2 = 3 أولي
    M = (1 << p) - 1  # 2^p - 1
    s = 4
    # نكرر p-2 مرة
    for _ in range(p - 2):
        s = (s * s - 2) % M
    return s == 0

# ---------- واجهة بسيطة ----------
def main():
    if len(sys.argv) < 2:
        print("استخدام: python3 lucas_lehmer.py <p>")
        print("مثال: python3 lucas_lehmer.py 31")
        sys.exit(1)

    try:
        p = int(sys.argv[1])
    except ValueError:
        print("المدخل p يجب أن يكون عددًا صحيحًا.")
        sys.exit(1)

    if p < 2:
        print("p يجب أن يكون >= 2.")
        sys.exit(1)

    print(f"التحقق من p = {p} ...")
    # أولاً: تحقق أن p نفسه عدد أولي (اختبار احتمالي سريع)
    t0 = time.time()
    if not is_probable_prime(p, k=8):
        t1 = time.time()
        print(f"النتيجة: p = {p} ليس عددًا أوليًا (انتهى خلال {t1-t0:.3f} ثانية).")
        sys.exit(0)
    t1 = time.time()
    print(f"p يبدو أوليًا (اختبار ميلر–رابين) — انتهى خلال {t1-t0:.3f} ثانية.")
    print("الآن سيتم تنفيذ اختبار Lucas–Lehmer على M_p = 2^p - 1 ...")
    # الآن اختبار لوكاس-ليهمر
    t2 = time.time()
    is_mersenne_prime = lucas_lehmer_test(p)
    t3 = time.time()
    if is_mersenne_prime:
        print(f"M_{p} = 2^{p} - 1 هو **عدد أولي**. (الوقت: {t3-t2:.3f} ثانية)")
    else:
        print(f"M_{p} = 2^{p} - 1 **مركب**. (الوقت: {t3-t2:.3f} ثانية)")

if __name__ == "__main__":
    main()





























