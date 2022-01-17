import re
from sqlite3.dbapi2 import complete_statement
from flask import Flask,render_template,request,jsonify,session,redirect,url_for,make_response,flash
import datetime
from functions import *
from base import *

app = Flask(__name__)
app.config["SECRET_KEY"] = "81564c74a6d95207f7966017cbe942571b7db427"
app.permanent_session_lifetime= datetime.timedelta(days = 10)


@app.route("/clear",methods = ['post', 'get'])
def clean():
	session.clear()
	return redirect(url_for("auth"))

@app.route("/auth",methods = ['post', 'get'])
def auth():
	user = Users
	token = session.get("token")
	if token:
		return redirect(url_for("profile"))
	
	if request.method != "POST":
		return render_template('auth.HTML')

	form_login = request.form.get("login")
	form_password = request.form.get("password")

	if (not (form_login and form_password)):
		return render_template('auth.HTML',message="не указан логин или пароль")

		
	if user.check_login(form_login,form_password):
		if not checkNumber(form_login):
			return render_template('auth.HTML',message="Введите корректный номер телефона")
			
		session["token"] = form_login
		return redirect(url_for("profile"))
	else:
		return render_template('auth.HTML',message="Неверный логин или пароль")
	
@app.route("/reg",methods = ['post', 'get'])
def reg():
	user = Users
	phone = request.form.get("phone")
	last_name = request.form.get("last_name")
	first_name = request.form.get("first_name")
	patronymic = request.form.get("patronymic")
	password = request.form.get("password")
	confirm_password = request.form.get("confirm_password")

	if request.method == "POST":
		if (not (phone and last_name and first_name and patronymic and password and confirm_password)):
			return render_template('reg.HTML',message="Какое-то поле воода данных не введено")

		if (password != confirm_password):
			return render_template('reg.HTML',message="Пароли не совпадают")
		
		if (not user.get_profile(phone)):
			if not checkNumber(phone):
				return render_template('reg.HTML',message="Введите корректный номер телефона")
			user.add_profile(phone,first_name,last_name,patronymic,password)
			return redirect(url_for("auth"))
		else:
			return render_template('reg.HTML',message="Аккаунт по данному номеру уже зарегистрирован!")

	return render_template('reg.HTML')
@app.route("/profile")
def profile():
	user = Users
	token = session.get("token")
	if not token: 
		return redirect(url_for("auth"))
	
	info = user.get_profile(session["token"])
	return render_template('profile.HTML',info = info)

@app.route("/summary",methods=["GET","POST"])
def summary():
	summ = Summaries
	token = session.get("token")
	if not token: 
		return redirect(url_for("auth"))
	
	summaries = summ.list_summaries()
	
	hash = get_hash_number("summ")
	phone = request.form.get("phone")
	first_name = request.form.get("first_name")
	last_name = request.form.get("last_name")
	patronymic = request.form.get("patronymic")
	phone = request.form.get("phone")
	speciality = request.form.get("speciality")
	diff = request.form.get("diff")

	if request.method == "POST":
		if (not (phone and first_name and last_name and patronymic and phone and speciality and diff)):
			return render_template('summary.HTML',summaries = summaries,message = "резюме не была добавлено, какое-то поле ввода было не заполнено")
		else:
			if not checkNumber(phone):
				return render_template('summary.HTML',summaries = summaries,message = "Введите корректный номер телефона")
			summ.add_summary(hash,token,first_name,last_name,patronymic,phone,speciality,diff)

	summaries = summ.list_summaries()

	if summaries:
		return render_template('summary.HTML',token = token,summaries = summaries)
	else:
		return render_template('summary.HTML')

@app.route("/deleteVac",methods=["GET","POST"])
def deleteVac():
	vac = Vacancies
	response = request.json
	vac.del_vac(response["hash"])
	return response

@app.route("/deleteSumm",methods=["GET","POST"])
def deleteSumm():
	summ = Summaries
	response = request.json
	summ.del_summ(response["hash"])
	return response

@app.route("/vacancies",methods=["post","get"])
def vacancies():
	vac = Vacancies

	token = session.get("token")

	if not token: 
		return redirect(url_for("auth"))
	
	listVacs = vac.list_vacancies()

	hash = get_hash_number("vac")
	phone = request.form.get("phone")
	company = request.form.get("company")
	activity = request.form.get("activity")
	address = request.form.get("address")

	if request.method == "POST":
		if (not (company and activity and address and phone)):
			return render_template('vacancies.HTML',listVacs = listVacs,message = "Вакансия не была добавлена, какое-то поле ввода было не заполнено")
		else:
			if not checkNumber(phone):
				return render_template('vacancies.HTML',listVacs = listVacs,message = "Введите корректный номер телефона")
			vac.add_vacancie(hash,token,phone,company,activity,address)	

	listVacs = vac.list_vacancies()
	if listVacs:
		return render_template('vacancies.HTML',token = token,listVacs = listVacs)
	else:
		return render_template('vacancies.HTML')

@app.errorhandler(404)
def pageNotFound(error):
	return redirect(url_for("auth"))

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True,port="80")