def sales_stats(data, **kwargs):
   revenue = sum([item[1]*item[2] for item in data]) if kwargs.get('revenue') else None
   if kwargs.get('quantity'):
       quantity = {}
       for item in data:
           if item[0] in quantity:
               quantity[item[0]] += item[1]
           else:
               quantity[item[0]] = item[1]
   else:
       quantity = None
   return revenue, quantity