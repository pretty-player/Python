from platform import system
from os import system as s
from tkinter import messagebox,Tk
win=Tk()
win.wm_withdraw()
dic={}
lis=[]
if system()=="Linux":
	clear="clear"
else:
	clear="cls"
def howmany():
	try:
		s(clear)
		how=int(input("\n\t\t\tHow Many Candidate's:"))
		howp=int(input("\n\t\t\tHow Many Votes:"))
		for x in range(int(how)):
			dyname=input(f"\n\t\t\t{x+1} Condidate Name:")
			dic[dyname.upper()]=0
			lis.append(dyname.upper())
		i=0
		while i<=int(howp-1):
			s(clear)
			print(f"\t\t\t\t\t\t\tPEOPLE ID:{i+1}")
			for x,y in enumerate(dic):
				print(x+1,":",y)
			try:
				vote=int(input("\n\t\t\tYour vote for:"))
				key=lis[vote-1]
				dic[key]=dic[key]+1
				i+=1
			except(Exception):
				messagebox.showinfo("Information","Only Enter Candidate Numbers")
				print(Exception)
		try:
			ans=input("Complete Your Election You Want View Result y/n:")
			if ans=="y" or ans=="Y" or ans=="yes" or ans=="YES":
				vlist=list(dic.values())
				maxx=max(vlist)
				wonC=vlist.index(maxx)
				name=lis[wonC]
				dname=dic[name]
				s(clear)
				print("\t\t\t+=========================+\n\t\t\t| Welcome Result Explorer |\n\t\t\t+=========================+")
				print("\n\t\t+__________________________________________________________+\n\t\t|Candidate_Name\t|\tGaining_Votes\t|\tTotal_Votes|\n\t\t+----------------------------------------------------------+")
				for z,y in dic.items():
					print(f"\n\t\t|      {z}\t|\t   {y}\t\t|\t{howp}\t   |")
				print("\t\t+----------------------------------------------------------+")
				print(f"Winning Canditate For:{name}\nGaining Votes For:{dname}")
			else:
				print("Ok Done...")
		except(Exception):
			messagebox.showinfo("title","Some Error Occur's"+str(Exception))
			howmany()
	except(Exception):
		messagebox.showinfo("Information","Input Values Only Numbers..."+str(Exception))
		howmany()
howmany()
