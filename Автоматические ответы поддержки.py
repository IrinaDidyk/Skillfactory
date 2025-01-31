def customer_support_simulator(questions):
   responses = []
   for question in questions:
       question = question.lower()
       if 'ошибка' in question:
           responses.append("Мы извиняемся за причиненные неудобства. Наши специалисты уже работают над этой ошибкой.")
       elif 'заказ' in question:
           responses.append("Ваш заказ обрабатывается. Мы уведомим вас, как только он будет отправлен.")
       elif 'вернуть' in question:
           responses.append("Вы можете вернуть товар в течение 14 дней с момента получения.")
       else:
           responses.append("Благодарим вас за обращение. Ваш вопрос передан специалистам.")
   return responses