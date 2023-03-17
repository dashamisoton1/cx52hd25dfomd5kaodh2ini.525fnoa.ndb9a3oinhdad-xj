
adad = [
'اول',
'دوم',
'سوم',
'چهارم',
'پنجم',
'ششم',
'هفتم',
'هتشم',
'نهم',
'دهم'
]
def mark(__types,__vid):
                return __types.InlineKeyboardMarkup(
                [[  
                        __types.InlineKeyboardButton("کلیک کنید",switch_inline_query_current_chat=__vid)
                ]])
def spon(__types,__sp,__link):

        inl = []
        __types.InlineKeyboardButton(text = "جوین شدم",url=__link)
        for i,m in zip(__sp.keys(),adad[:len(__sp.keys())]):
                inl.append([__types.InlineKeyboardButton(text = " کانال/گروه "+m,url=i)])
        inl.append([__types.InlineKeyboardButton(text = "جوین شدم",url=__link)])

        return __types.InlineKeyboardMarkup(inl)