	# Наш декоратор
def decorator(function):
		# Wrapped - функция обертка
	def wraped():
		print("1")
			# Изменяемый объект
		function()

	return wraped

	'''
		Decorator является оберткой для функции someFunction
		С помошью обертки, мы можем изменять данные, и
		функционал объектов
									'''
@decorator
def someFunction():

	print("2")

	'''
		В случае, если функия будет изменена Decorator.
		Полученный результат должен быть раверн 1 2
									'''

someFunction()
