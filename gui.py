from tkinter import  Tk, Button, Label, Frame
from time import strptime, strftime
from calendar import monthrange

class Calendar(Frame):			
	def __init__(self,master,year,month):		## 객체에서 인자 3개 받아야함
		Frame.__init__(self,master)
		self.pack()


		self.labels = [['Mon','Tue','Wed','Thu','Fri','Sat','Sun'],	## 달력 값 넣을 list
				  [[],[],[],[],[],[],[]],
				  [[],[],[],[],[],[],[]],
				  [[],[],[],[],[],[],[]],
				  [[],[],[],[],[],[],[]],
				  [[],[],[],[],[],[],[]] ]
		self.first_day = monthrange(year, month)[0]		## 월의 첫번째 날
		self.days = monthrange(year,month)[1]			## 월의 일 수
		self.day_counter=1		## 일을 count 하기 위한 변수
		for i in range(1,6):	## 첫 행 제외하고(이미 199line에서 할당함) 해당 일 할당
			if i == 1:
				for j in range(self.first_day,7):
					self.labels[i][j] = self.day_counter
					self.day_counter+=1
					if self.day_counter > self.days:
						break
			else:
				for j in range(0,7):
					self.labels[i][j]= self.day_counter
					self.day_counter += 1
					if self.day_counter > self.days:
						break

		for i in range(0,6):			## 첫행은 버튼 필요없기에 label 생성
			for j in range(0,7):
				if i == 0:
					label = Label(self,
								  padx=10,
								  text=self.labels[i][j])
					label.grid(row=i,column=j)
				else:					## 그 이외의 행은 button 생성
					button=Button(self,
								  padx=10,
								  text=self.labels[i][j])
					button.grid(row=i,column=j)

if __name__ == '__main__':
	root = Tk()		
	app = Calendar(root,2012,2)
	app.pack()
	root.mainloop()