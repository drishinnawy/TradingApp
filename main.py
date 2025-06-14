import webbrowser
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
import arabic_reshaper
from bidi.algorithm import get_display

Window.size = (400, 800)

class TradingApp(MDApp):
    dialog = None
    title = "أفضل حاسبة تداول"

    def fix_arabic(self, text):
        reshaped_text = arabic_reshaper.reshape(text)
        return get_display(reshaped_text)

    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.theme_style = "Light"
        self.title = "أفضل حاسبة تداول"
        return Builder.load_file("tradingapp.kv")

    def update_arabic_label(self, text_input, label):
        label.text = self.fix_arabic(text_input.text)

    def calc_average(self):
        try:
            total_cost = 0
            total_qty = 0
            platform_fee = float(self.get_field_value('platform_fee') or 0)
            for i in range(1, 6):
                price = self.get_field_value(f'price{i}')
                qty = self.get_field_value(f'qty{i}')
                if price and qty:
                    total_cost += float(price) * int(qty) * (1 + platform_fee)
                    total_qty += int(qty)
            avg_price = total_cost / total_qty if total_qty > 0 else 0
            self.root.ids['average_result'].text = self.fix_arabic(f"متوسط سعر الشراء بعد العمولة: {avg_price:.2f}")
        except Exception as e:
            self.root.ids['average_result'].text = self.fix_arabic(f"خطأ في الحساب: {str(e)}")

    def calc_total_cost(self):
        try:
            total_cost = 0
            platform_fee = float(self.get_field_value('platform_fee') or 0)
            for i in range(1, 6):
                price = self.get_field_value(f'price{i}')
                qty = self.get_field_value(f'qty{i}')
                if price and qty:
                    total_cost += float(price) * int(qty) * (1 + platform_fee)
            self.root.ids['cost_result'].text = self.fix_arabic(f"التكلفة الإجمالية بعد العمولة: {total_cost:.2f}")
        except Exception as e:
            self.root.ids['cost_result'].text = self.fix_arabic(f"خطأ في الحساب: {str(e)}")

    def calc_profit(self):
        try:
            total_cost = 0
            total_qty = 0
            platform_fee = float(self.get_field_value('platform_fee') or 0)
            for i in range(1, 6):
                price = self.get_field_value(f'price{i}')
                qty = self.get_field_value(f'qty{i}')
                if price and qty:
                    total_cost += float(price) * int(qty) * (1 + platform_fee)
                    total_qty += int(qty)
            sell_price = float(self.get_field_value('sell_price') or 0)
            total_sell = sell_price * total_qty * (1 - platform_fee)
            profit = total_sell - total_cost
            self.root.ids['profit_result'].text = self.fix_arabic(f"الربح/الخسارة: {profit:.2f}")
        except Exception as e:
            self.root.ids['profit_result'].text = self.fix_arabic(f"خطأ في الحساب: {str(e)}")

    def calc_possible_qty(self):
        try:
            amount = float(self.get_field_value('deal_amount') or 0)
            price = float(self.get_field_value('possible_price') or 0)
            platform_fee = float(self.get_field_value('platform_fee') or 0)
            if price > 0:
                qty = int(amount // (price * (1 + platform_fee)))
                self.root.ids['possible_qty_result'].text = self.fix_arabic(f"يمكنك شراء {qty} سهم")
            else:
                self.root.ids['possible_qty_result'].text = self.fix_arabic("يرجى إدخال سعر سهم صحيح")
        except Exception as e:
            self.root.ids['possible_qty_result'].text = self.fix_arabic(f"خطأ: {str(e)}")

    def get_field_value(self, field_id):
        field = self.root.ids.get(field_id)
        return field.text.strip() if field and field.text else ""

    def open_tickerchart(self):
        url = "https://www.tickerchart.net/app/ar"
        try:
            webbrowser.open(url)
        except Exception:
            self.show_message(self.fix_arabic("تعذر فتح المتصفح في هذه البيئة"))

    def open_sharia(self):
        url = "https://www.argaam.com/ar/company/shariahcompanies"
        try:
            webbrowser.open(url)
        except Exception:
            self.show_message(self.fix_arabic("تعذر فتح المتصفح في هذه البيئة"))

    def clear_results(self):
        # امسح كل الحقول النصية والنتائج
        ids_to_clear = [
            'stock_name', 'qty1', 'price1', 'sell_price',
            'platform_fee', 'currency',
            'qty2', 'price2', 'qty3', 'price3', 'qty4', 'price4', 'qty5', 'price5',
            'average_result', 'cost_result', 'profit_result',
            'arabic_stock_name_lbl','arabic_qty1_lbl','arabic_price1_lbl','arabic_sell_price_lbl',
            'arabic_platform_fee_lbl','arabic_currency_lbl',
            'arabic_qty2_lbl','arabic_price2_lbl','arabic_qty3_lbl','arabic_price3_lbl',
            'arabic_qty4_lbl','arabic_price4_lbl','arabic_qty5_lbl','arabic_price5_lbl',
            'deal_amount','possible_price','possible_qty_result'
        ]
        for id_ in ids_to_clear:
            field = self.root.ids.get(id_)
            if field:
                field.text = ""

    def show_message(self, text):
        if self.dialog:
            self.dialog.dismiss()
        self.dialog = MDDialog(text=text)
        self.dialog.open()

if __name__ == '__main__':
    TradingApp().run()
