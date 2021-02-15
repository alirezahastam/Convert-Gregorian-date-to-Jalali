def Miladi_to_Shamsi(y, m, d):
    g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    if (m > 2):
        y2 = y + 1
    else:
        y2 = y
    days = 355666 + (365 * y) + ((y2 + 3) // 4) - ((y2 + 99) //
                                                     100) + ((y2 + 399) // 400) + d + g_d_m[m - 1]
    jalali_year = -1595 + (33 * (days // 12053))
    days %= 12053
    jalali_year += 4 * (days // 1461)
    days %= 1461
    if (days > 365):
        jalali_year += (days - 1) // 365
        days = (days - 1) % 365
    if (days < 186):
        jalali_month = 1 + (days // 31)
        jalali_day = 1 + (days % 31)
    else:
        jalali_month = 7 + ((days - 186) // 30)
        jalali_day = 1 + ((days - 186) % 30)
    return [jalali_year, jalali_month, jalali_day]
  
