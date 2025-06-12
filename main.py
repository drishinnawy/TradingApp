# main.py المعدل - نسخة بدون numpy
print('Hello from modified TradingApp')
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import webbrowser
import csv
import os
import random
import datetime
import requests

Window.size = (360, 700)

KV = '''
MDScreen:
    MDTopAppBar:
        title: "أفضل حاسبة تداول"
        elevation: 4
        pos_hint: {"top": 1}

    ScrollView:
        MDBoxLayout:
            orientation: 'vertical'
            padding: dp(10)
            spacing: dp(10)
            adaptive_height: True

            MDLabel:
                text: "معلومات السهم"
                halign: "right"
                bold: True

            MDTextField:
                id: stock_name
                hint_text: "اسم السهم"
                mode: "rectangle"

            MDTextField:
                id: stock_code
                hint_text: "رقم السهم"
                mode: "rectangle"

            MDTextField:
                id: platform_fee
                hint_text: "نسبة المنصة (مثال: 0.0015)"
                text: "0.0015"
                mode: "rectangle"

            MDLabel:
                text: "العملة"
                halign: "right"
                bold: True

            MDTextField:
                id: currency
                hint_text: "العملة (مثال: SAR, USD, EUR)"
                text: "SAR"
                mode: "rectangle"

            MDLabel:
                text: "عمليات الشراء"
                halign: "right"
                bold: True

            GridLayout:
                cols: 2
                row_force_default: True
                row_default_height: dp(50)
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height

                MDLabel:
                    text: "السعر"
                MDLabel:
                    text: "العدد"

                MDTextField:
                    id: price1
                    hint_text: "سعر 1"
                MDTextField:
                    id: qty1
                    hint_text: "عدد 1"

                MDTextField:
                    id: price2
                    hint_text: "سعر 2"
                MDTextField:
                    id: qty2
                    hint_text: "عدد 2"

                MDTextField:
                    id: price3
                    hint_text: "سعر 3"
                MDTextField:
                    id: qty3
                    hint_text: "عدد 3"

                MDTextField:
                    id: price4
                    hint_text: "سعر 4"
                MDTextField:
                    id: qty4
                    hint_text: "عدد 4"

                MDTextField:
                    id: price5
                    hint_text: "سعر 5"
                MDTextField:
                    id: qty5
                    hint_text: "عدد 5"

            MDTextField:
                id: sell_price
                hint_text: "سعر البيع"
                mode: "rectangle"

            MDRaisedButton:
                text: "حساب المتوسط والتكلفة والربح"
                on_release: app.calculate()

            MDLabel:
                id: result_label
                text: ""
                halign: "center"

            MDRaisedButton:
                text: "فتح صفحة السهم في تكرشارت"
                on_release: app.open_tickerchart()

            MDRaisedButton:
                text: "عرض شرعية السهم من أرقام"
                on_release: app.open_sharia()

            MDRaisedButton:
                text: "عرض توصيات"
                on_release: app.show_recommendations()

            MDRaisedButton:
                text: "حفظ CSV"
                on_release: app.save_csv()

            MDRaisedButton:
                text: "عرض الرسم البياني للأرباح"
                on_release: app.show_chart()

            MDRaisedButton:
                text: "تحميل كـ PDF"
                on_release: app.export_pdf()
'''

class TradingApp(MDApp):
    def build(self):
        self.title = "أفضل حاسبة تداول"
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

    def get_currency_rate(self, currency):
        try:
            if currency.upper() == "SAR":
                return 1
            response = requests.get(f"https://api.exchangerate.host/latest?base=SAR")
            data = response.json()
            rate = data['rates'].get(currency.upper(), None)
            return rate if rate else 1
        except:
            return 1

    def calculate(self):
        try:
            self.total_cost = 0
            self.total_qty = 0
            self.prices = []
            self.profit_values = []

            for i in range(1, 6):
                price = self.root.ids[f'price{i}'].text
                qty = self.root.ids[f'qty{i}'].text
                if price and qty:
                    p = float(price)
                    q = int(qty)
                    self.total_cost += p * q
                    self.total_qty += q
                    self.prices.append(p)

            avg_price = self.total_cost / self.total_qty if self.total_qty > 0 else 0
            sell_price = float(self.root.ids['sell_price'].text or 0)
            platform_fee = float(self.root.ids['platform_fee'].text)
            total_cost_with_fee = self.total_cost * (1 + platform_fee)
            total_sell = sell_price * self.total_qty * (1 - platform_fee)
            self.profit = total_sell - total_cost_with_fee

            currency = self.root.ids['currency'].text.upper()
            rate = self.get_currency_rate(currency)

            converted_avg_price = avg_price * rate
            converted_total_cost = total_cost_with_fee * rate
            converted_profit = self.profit * rate

            self.root.ids['result_label'].text = f"متوسط السعر: {converted_avg_price:.2f} {currency}\nالتكلفة الإجمالية: {converted_total_cost:.2f} {currency}\nالربح/الخسارة: {converted_profit:.2f} {currency}"
        except Exception as e:
            Snackbar(text=f"خطأ في الحساب: {str(e)}").open()

    def open_tickerchart(self):
        code = self.root.ids['stock_code'].text.strip()
        if code:
            url = f"https://www.tickerchart.net/app/ar?symbol={code}"
            webbrowser.open(url)

    def open_sharia(self):
        webbrowser.open("https://www.argaam.com/ar/company/shariahcompanies")

    def show_recommendations(self):
        Snackbar(text="توصيات: سابك، أرامكو، مصرف الراجحي ✅").open()

    def save_csv(self):
        try:
            filename = f"تقرير_تداول_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['السهم', 'الرمز', 'السعر', 'العدد'])
                for i in range(1, 6):
                    p = self.root.ids[f'price{i}'].text
                    q = self.root.ids[f'qty{i}'].text
                    if p and q:
                        writer.writerow([self.root.ids['stock_name'].text, self.root.ids['stock_code'].text, p, q])
                writer.writerow(['', '', 'سعر البيع', self.root.ids['sell_price'].text])
            Snackbar(text=f"تم حفظ البيانات في {filename}").open()
        except Exception as e:
            Snackbar(text=f"خطأ في الحفظ: {str(e)}").open()

    def show_chart(self):
        try:
            self.calculate()
            fig, ax = plt.subplots()
            x = list(range(1, len(self.prices) + 1))
            profits = [((float(self.root.ids['sell_price'].text or 0)) - p) for p in self.prices]
            ax.bar(x, profits, color='green')
            ax.set_title('تقلب الأرباح')
            ax.set_xlabel('العملية')
            ax.set_ylabel('الربح')
            plt.grid(True)
            self.dialog = MDDialog(title="الرسم البياني", type="custom", content_cls=FigureCanvasKivyAgg(fig))
            self.dialog.open()
        except Exception as e:
            Snackbar(text=f"خطأ في عرض الرسم: {str(e)}").open()

    def export_pdf(self):
        try:
            import matplotlib.backends.backend_pdf
            pdf = matplotlib.backends.backend_pdf.PdfPages("تقرير_تداول.pdf")
            fig, ax = plt.subplots()
            self.calculate()
            x = list(range(1, len(self.prices) + 1))
            profits = [((float(self.root.ids['sell_price'].text or 0)) - p) for p in self.prices]
            ax.bar(x, profits, color='blue')
            ax.set_title("الرسم البياني للربح")
            pdf.savefig(fig)
            pdf.close()
            Snackbar(text="تم تصدير التقرير إلى PDF").open()
        except Exception as e:
            Snackbar(text=f"خطأ في تصدير PDF: {str(e)}").open()

if __name__ == '__main__':
    TradingApp().run()
