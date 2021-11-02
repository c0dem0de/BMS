import mysql.connector,bullet,random
usr = input("Enter usrname: ")
pwd = bullet.Password(prompt='Enter pwd: ', hidden='*').launch()
base = mysql.connector.connect(host='localhost', user=f'{usr}', passwd=f'{pwd}', database='bms')
pointr = base.cursor()
# usr = "home"
# pwd = "Trio1-Pope-Overbill"
print("\n\
╔‑‑‑‑‑‑‑‑‑‑‑‑‑‑--‑‑‑‑‑‑‑‑╗\n\
┇   ○ Create Account     ┇\n\
┇   ◉ Retrieve Account   ┇\n\
┇   ○ Transactions       ┇\n\
┇   ○ Account Holders    ┇\n\
┇   ○ Remove Account     ┇\n\
┇   ○ Log Out            ┇\n\
╚‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑-‑‑‑‑‑‑‑╝")
acc_no = int(input("Enter the account no: "))
pointr.execute("SELECT * FROM members WHERE ID=%s",(acc_no,))
data = list(pointr)
print(data[0])