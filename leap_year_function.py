#leap year function


if (year_set % 4) == 0:
   if (year_set % 100) == 0:
       if (year_set % 400) == 0:
           print('leap year')
       else:
           print('no leap year')
   else:
       print('leap year')
else:
   print('no leap year')
