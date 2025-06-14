import webbrowser
import requests
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
import arabic_reshaper
from bidi.algorithm import get_display

Window.size = (400, 800)

def fix_arabic(text):
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    return bidi_text

class TradingApp(MDApp):
    dialog = None

    def build(self):
        self.title = fix_arabic("أفضل حاسبة تداول")
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.theme_style = "Light"
        return Builder.load_file("tradingapp.kv")

    def get_currency_rate(self, currency):
        try:
            if currency.upper() == "SAR":
                return 1
            response = requests.get("https://api.exchangerate.host/latest?base=SAR")
            if response.ok:
                data = response.json()
                return data.get('rates', {}).get(currency.upper(), 1)
            return 1
        except:
            return 1

    def calculate(self):
        try:
            total_cost = 0
            total_qty = 0
            for i in range(1, 6):
                price = self.root.ids.get(f'price{i}').text
                qty = self.root.ids.get(f'qty{i}').text
                if price and qty:
                    p = float(price)
                    q = int(qty)
                    total_cost += p * q
                    total_qty += q
            avg_price = total_cost / total_qty if total_qty > 0 else 0
            sell_price = float(self.root.ids['sell_price'].text or 0)
            platform_fee = float(self.root.ids['platform_fee'].text or 0)
            total_cost_with_fee = total_cost * (1 + platform_fee)
            total_sell = sell_price * total_qty * (1 - platform_fee)
            profit = total_sell - total_cost_with_fee

            currency = self.root.ids['currency'].text.upper()
            rate = self.get_currency_rate(currency)

            text = (
                f"متوسط السعر: {avg_price * rate:.2f} {currency}\n"
                f"التكلفة الإجمالية: {total_cost_with_fee * rate:.2f} {currency}\n"
                f"الربح/الخسارة: {profit * rate:.2f} {currency}"
            )
            self.root.ids['result_label'].text = fix_arabic(text)
        except Exception as e:
            self.show_message(fix_arabic(f"خطأ في الحساب: {str(e)}"))

    def open_tickerchart(self):
        code = self.root.ids['stock_code'].text.strip()
        if code:
            url = f"https://www.tickerchart.net/app/ar?symbol={code}"
            try:
                webbrowser.open(url)
            except Exception:
                self.show_message(fix_arabic("تعذر فتح المتصفح في هذه البيئة"))
        else:
            self.show_message(fix_arabic("يرجى إدخال رقم السهم"))

    def open_sharia(self):
        url = "https://www.argaam.com/ar/company/shariahcompanies"
        try:
            webbrowser.open(url)
        except Exception:
            self.show_message(fix_arabic("تعذر فتح المتصفح في هذه البيئة"))

    def show_recommendations(self):
        self.show_message(fix_arabic("ميزة التوصيات ستتوفر لاحقًا."))

    def save_csv(self):
        import csv
        try:
            stock_name = self.root.ids['stock_name'].text
            stock_code = self.root.ids['stock_code'].text
            platform_fee = self.root.ids['platform_fee'].text
            currency = self.root.ids['currency'].text
            sell_price = self.root.ids['sell_price'].text

            rows = [['السهم', 'الرمز', 'العمولة', 'العملة', 'سعر البيع']]
            rows.append([stock_name, stock_code, platform_fee, currency, sell_price])
            for i in range(1, 6):
                price = self.root.ids.get(f'price{i}').text
                qty = self.root.ids.get(f'qty{i}').text
                rows.append([f"سعر {i}", price, f"عدد {i}", qty])

            with open("trading_result.csv", "w", encoding="utf-8", newline='') as f:
                writer = csv.writer(f)
                writer.writerows(rows)

            self.show_message(fix_arabic("تم حفظ النتائج في trading_result.csv"))
        except Exception as e:
            self.show_message(fix_arabic(f"خطأ في حفظ الملف: {str(e)}"))

    def export_pdf(self):
        self.show_message(fix_arabic("ميزة التصدير PDF ليست مدعومة في هذا الإصدار."))

    def show_message(self, text):
        if self.dialog:
            self.dialog.dismiss()
        self.dialog = MDDialog(text=text)
        self.dialog.open()

if __name__ == '__main__':
    TradingApp().run()
