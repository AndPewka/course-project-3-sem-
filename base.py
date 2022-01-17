import sqlite3
import random
import datetime
def create_base_person():
	con = sqlite3.connect("Base.dp")
	cur = con.cursor()
	cur.execute("""CREATE TABLE IF NOT EXISTS profiles(phone       TEXT,
													  first_name  TEXT,
													  last_name   TEXT,
													  patronymic  TEXT,
													  password    TEXT)""")
	con.commit()

	cur.execute("""CREATE TABLE IF NOT EXISTS vacancies(hash        TEXT,
														creator     TEXT,
														phone       TEXT,
													    company     TEXT,
													    activity    TEXT,
													    address     TEXT)""")
	con.commit()

	cur.execute("""CREATE TABLE IF NOT EXISTS summaries(hash        TEXT,
														creator     TEXT,
														first_name  TEXT,
													    last_name   TEXT,
													    patronymic  TEXT,
														phone       TEXT,
														speciality  TEXT,
														diff        TEXT)""")
	con.commit()
	cur.close()
	con.close()


class Users:
	def check_login(phone,password):
		con = sqlite3.connect("Base.dp")
		description =[]
		description.append(phone)
		cur = con.cursor()
		cur.execute('SELECT password from profiles WHERE phone = ?',description)
		message = cur.fetchall()
		con.commit()
		cur.close()
		con.close()
		if message:
			confirm_password = message[0][0]
			if password == confirm_password:
				return True

	def add_profile(phone,first_name="test",last_name="test",patronymic="test",password="test"):
		description=[]

		if Users.get_profile(phone):
			return False

		con = sqlite3.connect("Base.dp")
		cur = con.cursor()
		description.append(phone)
		description.append(first_name)
		description.append(last_name)
		description.append(patronymic)
		description.append(password)
		try:
			cur.execute("INSERT INTO profiles VALUES(?,?,?,?,?)",description)
			con.commit()
		except:
			return False
		cur.close()
		con.close()
		del description
		return True
	
	def del_profile(phone):
		if not Users.get_profile(phone):
			return False
		con = sqlite3.connect("Base.dp")
		description =[]
		description.append(phone)
		cur = con.cursor()
		cur.execute('DELETE from profiles WHERE phone = ?',description)
		con.commit()
		cur.close()
		con.close()
		return True

	def get_profile(phone):
		con = sqlite3.connect("Base.dp")
		description =[]
		description.append(phone)
		cur = con.cursor()
		cur.execute('SELECT * from profiles WHERE phone = ?',description)
		messange = cur.fetchall()
		con.commit()
		cur.close()
		con.close()
		result = {}

		if messange:
			messange= messange[0]

			result["phone"] = messange[0]
			result["first_name"] = messange[1]
			result["last_name"] = messange[2]
			result["patronymic"] = messange[3]
			result["password"] = messange[4]
			if result!=0:
				return result
		
		return False

	def list_profile():
		con = sqlite3.connect("Base.dp")
		cur = con.cursor()
		cur.execute('SELECT * from profiles')
		messange = cur.fetchall()
		con.commit()
		cur.close()
		con.close()
		results= []
		if messange:
			for mess in messange:
				result = {}
				result["phone"] = mess[0]
				result["first_name"] = mess[1]
				result["last_name"] = mess[2]
				result["patronymic"] = mess[3]
				result["password"] = mess[4]
				results.append(result)
			return results

class Vacancies:
	def add_vacancie(hash,creator,phone,company,activity,address):
		description=[]
		con = sqlite3.connect("Base.dp")
		cur = con.cursor()
		description.append(hash)
		description.append(creator)
		description.append(phone)
		description.append(company)
		description.append(activity)
		description.append(address)
		try:
			x = cur.execute("INSERT INTO vacancies VALUES(?,?,?,?,?,?)",description)
			con.commit()
		except:
			return False
		cur.close()
		con.close()
		del description
		return True

	def del_vac(hash):
		con = sqlite3.connect("Base.dp")
		hashs = get_hashs_vac()
		if hash not in hashs:
			return False
		description =[]
		description.append(hash)
		cur = con.cursor()
		x = cur.execute('DELETE from vacancies WHERE hash = ?',description)
		con.commit()
		cur.close()
		con.close()
		return True
	
	def list_vacancies():
		con = sqlite3.connect("Base.dp")
		cur = con.cursor()
		cur.execute('SELECT * from vacancies')
		messange = cur.fetchall()
		con.commit()
		cur.close()
		con.close()
		results= []
		if messange:
			for mess in messange:
				result = {}
				result["hash"] = mess[0]
				result["creator"] = mess[1]
				result["phone"] = mess[2]
				result["company"] = mess[3]
				result["activity"] = mess[4]
				result["address"] = mess[5]
				results.append(result)
			return results

def get_hashs_vac():
	con = sqlite3.connect("Base.dp")
	cur = con.cursor()
	cur.execute('SELECT hash from vacancies')
	messange = cur.fetchall()
	results = []
	for mess in messange:
		results.append(mess[0])
	con.commit()
	cur.close()
	con.close()
	if messange:
		return results
	return []

def get_hash_number(type):
	if type=="vac":
		hashs = get_hashs_vac()
	else:
		hashs = get_hashs_sum()
    
	hash = str(random.getrandbits(128))[:6]
	if hashs:
		while(hash in hashs):
			hash = str(random.getrandbits(128))[:1]
	return hash

class Summaries:
	def add_summary(hash,creator,first_name,last_name,patronymic,phone,speciality,diff):
		description=[]
		con = sqlite3.connect("Base.dp")
		cur = con.cursor()
		description.append(hash)
		description.append(creator)
		description.append(first_name)
		description.append(last_name)
		description.append(patronymic)
		description.append(phone)
		description.append(speciality)
		description.append(diff)
		try:
			cur.execute("INSERT INTO summaries VALUES(?,?,?,?,?,?,?,?)",description)
			con.commit()
		except:
			return False
		cur.close()
		con.close()
		del description
		return True

	def del_summ(hash):
		con = sqlite3.connect("Base.dp")
		hashs = get_hashs_sum()
		print(hashs)
		if hash not in hashs:
			return False
		description =[]
		description.append(hash)
		cur = con.cursor()
		cur.execute('DELETE from summaries WHERE hash = ?',description)
		con.commit()
		cur.close()
		con.close()
		return True

	def list_summaries():
		con = sqlite3.connect("Base.dp")
		cur = con.cursor()
		cur.execute('SELECT * from summaries')
		messange = cur.fetchall()
		con.commit()
		cur.close()
		con.close()
		results= []
		if messange:
			for mess in messange:
				result = {}
				result["hash"] = mess[0]
				result["creator"] = mess[1]
				result["first_name"] = mess[2]
				result["last_name"] = mess[3]
				result["patronymic"] = mess[4]
				result["phone"] = mess[5]
				result["speciality"] = mess[6]
				result["diff"] = mess[7]
				results.append(result)
			return results

def get_hashs_sum():
	con = sqlite3.connect("Base.dp")
	cur = con.cursor()
	cur.execute('SELECT hash from summaries')
	messange = cur.fetchall()
	results = []
	for mess in messange:
		results.append(mess[0])
	if messange:
		return results
	
	return []

create_base_person()



