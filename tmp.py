p1 = Process(target=func, args=(date_start.year, date_start.month, date_start.day,
                                hour, minutes, 0, str(date_start)))
# p2 = Process(target=func, args=(date_start.year, date_start.month, date_start.day,
#                                 hour, minutes, 0, str(date_start)))
# p3 = Process(target=func, args=(date_start.year, date_start.month, date_start.day,
#                                 hour, minutes, 0, str(date_start)))
# p4 = Process(target=func, args=(date_start.year, date_start.month, date_start.day,
#                                 hour, minutes, 0, str(date_start)))
p1.start()
# p2.start()
# p3.start()
# p4.start()
p1.join()
# p2.join()
# p3.join()
# p4.join()
