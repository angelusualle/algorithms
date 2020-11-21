import math
def int_to_english(num):
    ans = ''
    if num > 999.999999e9:
        raise Exception('Error: too big')
    if num < 0:
        ans += 'negative '
        num *= -1
    tri_places = {9: 'billion', 6: 'million', 3: 'thousand'}
    tens_places = {9: 'ninety', 8: 'eighty',  7: 'seventy', 6: 'sixty', 5: 'fifty', 4: 'fourty', 3: 'thirty', 2: 'twenty'}
    teens_places = {19: 'nineteen', 18: 'eighteen', 17: 'seventeen', 16: 'sixteen', 15: 'fifteen', 14: 'fourteen', 13: 'thirteen', 12: 'twelve', 11: 'eleven', 10: 'ten'}
    ones_places = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    def get_hundred_qty(hundreds):
        hundreds_txt = ''
        if hundreds > 100:
            digit = int(hundreds // 100)
            hundreds_txt += ones_places[digit] + ' hundred '
            hundreds -= digit * 100
        if hundreds > 19:
            digit = int(hundreds // 10)
            hundreds_txt += tens_places[digit] + ' '
            hundreds -= digit * 10
        elif hundreds > 10:
            hundreds_txt += teens_places[hundreds] + ' '
            hundreds = 0
        elif hundreds == 10:
            hundreds_txt += tens_places[hundreds] + ' '
            hundreds = 0
        if hundreds > 0:
            hundreds_txt += ones_places[hundreds] + ' '
        return hundreds_txt
    if int(math.log10(num)) >= 9:
        qty = int(num // 1e9)
        txt = get_hundred_qty(qty)
        ans += txt + 'trillion '
        num -= int(qty*1e9)
    if int(math.log10(num)) >= 6:
        qty = int(num // 1e6)
        txt = get_hundred_qty(qty)
        ans += txt + 'billion '
        num -= int(qty*1e6)
    if int(math.log10(num)) >= 3:
        qty = int(num // 1e3)
        txt = get_hundred_qty(qty)
        ans += txt + 'thousand '
        num -= int(qty*1e3)
    if num > 0:
        txt = get_hundred_qty(num)
        ans += txt 
    return ans
