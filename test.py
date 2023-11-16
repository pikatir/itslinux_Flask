from flask import Flask
app = Flask(__name__)

# Обработчик маршрута для GET-запроса
@app.route('/')
def index():
# HTML-страница, которую мы отправляем в ответ на GET-запрос
	return """
	<!DOCTYPE html>
	<html>
	<head>
		<title>Привет, мир!</title>
	</head>
	<body>
		<h1>Привет, мир!</h1>
		<p>Это статичная HTML-страница, возвращаемая на GET-запрос.</p>
	</body>
	</html>
	"""

if __name__ == '__main__':
# Запуск сервера
	app.run(host = "0.0.0.0", port = 5000, debug=True)
