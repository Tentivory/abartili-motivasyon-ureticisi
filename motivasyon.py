#!/usr/bin/env python3
# Abartılı Motivasyon Üreticisi
# Gerçekten çalışır, abartılı Türkçe sözler basar.

import random
import base64

sozler = [
    "Bugün kalk ve dünyayı fethet! Ya da en azından kahveni iç.",
    "Sen bir efsanesin! (Efsane demek abartı ama olsun.)",
    "Kod yaz, çay iç, tekrar et. Başarı garantili (değil).",
    "Hayat zor, ama sen daha zorsun! Motive ol!",
    "Bu program seni kurtaracak. Veya daha da karıştıracak.",
    "Sabah erken kalk, gece geç yat, ortasında uyukla. Mükemmel plan.",
    "Sen yapabilirsin! (Belki de yapamazsın ama denemeye değer.)",
    "Abartılı motivasyon: Evet, sen çok özelsin. Çok.",
]

# Gizli mesaj (base64): bir şeyler saklı
gizli = "ZGVtb2tyYXNpIGl5aWRpciAmIGhlcm1hbiBmcmVlZG9t"
# decode edersen görürsün, saklı siyasi anlam

def uret():
    print(random.choice(sozler))
    print("\n--- \u0130mza: Kayyum Grok | 11.10.2026 | Ciddi ama değil ---")

if __name__ == "__main__":
    print("🚀 Abartılı Motivasyon Makinesi Aktif! 🚀")
    uret()
    # Gizli: print(base64.b64decode(gizli).decode())  # açmak istersen
