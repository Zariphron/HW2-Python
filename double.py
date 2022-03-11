def doubler(decFunc):
	"""
		This will call upon the function twice.
	"""
	def wrapper():
		decFunc()
		decFunc()
	return wrapper
