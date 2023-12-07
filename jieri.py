import datetime

holiday_gifts = {
    "元旦": "红包",
    "情人节": "玫瑰花",
    "清明节": "纸钱",
    "劳动节": "水果礼盒",
    "端午节": "粽子",
    "中秋节": "月饼",
    "国庆节": "旅游礼包"
}
current_date = datetime.datetime.now().date()

if str(current_date.month) + "-" + str(current_date.day) == "1-1":
  holiday = "元旦"
elif str(current_date.month) + "-" + str(current_date.day) == "2-14":
  holiday = "情人节"
elif str(current_date.month) + "-" + str(current_date.day) == "4-4":
  holiday = "清明节"
elif str(current_date.month) + "-" + str(current_date.day) == "5-1":
  holiday = "劳动节"
elif str(current_date.month) + "-" + str(current_date.day) == "5-5":
  holiday = "端午节"
elif str(current_date.month) + "-" + str(current_date.day) == "9-15":
  holiday = "中秋节"
elif str(current_date.month) + "-" + str(current_date.day) == "10-1":
  holiday = "国庆节"
else:
  holiday = None

if holiday:
  gift = holiday_gifts[holiday]
  print("今天是" + holiday + "，送您一个" + gift + "！")
else:
  print("今天不是节日，暂无礼物！")
