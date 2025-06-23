# 📱 TestareSiteEmag

Acesta este un proiect de teste automate scrise în **Python** folosind **unittest** și **Selenium WebDriver** pentru a testa funcționalități de căutare pe site-ul [eMAG.ro](https://www.emag.ro).

---

## 🧰 Tehnologii utilizate

- Python 3.x
- Selenium WebDriver
- unittest (framework de testare integrat în Python)
- ChromeDriver (pentru browser Chrome)

---

## 🚀 Descriere și funcționalitate

Clasa `SiteEmag` conține teste automate pentru verificarea unor funcții specifice site-ului eMAG:

- Acceptarea cookie-urilor (deși momentan elementul nu este folosit în cod, e declarat)
- Căutarea produsului „Iphone 15 pro max”
- Numărarea rezultatelor afișate pentru această căutare
- Verificarea disponibilității variantelor de stocare (256 GB, 512 GB, 1 TB) pe pagina produsului

---

## ▶️ Cum rulezi testele

### 1. Clonează proiectul

```bash
git clone https://github.com/poprobert0412/TestareSiteEmag.git
cd TestareSiteEmag
````

### 2. Instalează dependențele

Dacă ai un fișier `requirements.txt` (dacă nu, îl poți crea cu conținutul: `selenium`):

```bash
pip install -r requirements.txt
```

sau direct:

```bash
pip install selenium
```

### 3. Descarcă ChromeDriver

Descarcă driverul Chrome corespunzător versiunii tale de browser Chrome:
[https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

Asigură-te că executabilul este în `PATH` sau în folderul proiectului.

### 4. Rulează testele

```bash
python -m unittest site_emag_test.py
```

---

## ⚠️ Notă importantă

* Site-ul eMAG poate avea sisteme anti-automare care să blocheze rularea testelor. Acest lucru poate cauza eșecuri la rulare.
* Testele funcționează pe structura actuală a site-ului. Dacă eMAG modifică elementele HTML, testele trebuie actualizate corespunzător.
* În prezent, testul pentru verificarea cookie-urilor este definit, dar nu este utilizat în metoda `setUp`. Poate fi îmbunătățit.

---

## 📝 Exemplu de test

```python
def test_numar_iphone_15_pro_max(self):
    self.chrome.find_element(*self.search_box).send_keys("Iphone 15 pro max")
    self.chrome.find_element(*self.search_box).send_keys(Keys.ENTER)
    WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.iphone_15_pro_max))
    phones = self.chrome.find_elements(*self.iphone_15_pro_max)
    iphone_15_sum = len(phones)
    print(f"Am gasit {iphone_15_sum} de telefoane Iphone 15 pro max!")
```

---

## 👤 Autor

**Pop Robert**
GitHub: [@poprobert0412](https://github.com/poprobert0412)
