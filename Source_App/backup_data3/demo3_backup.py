from googletrans import Translator
from tkinter import filedialog
from tkinter import *
from time import sleep
import difflib
import docx




def func_ThucThi():
	############################################################################
	#tách từng đoạn tiếng việt từ file vie.txt do người viết bỏ vào list_doan_vie

	path_file_vie = entry_1_text.get()
	file_txt_vie = open(path_file_vie, encoding="utf-8")
	lst_vie = file_txt_vie.readlines()

	list_catdong = []

	i = 0
	while i < len(lst_vie):
		listcon_catdong = lst_vie[i].splitlines()
		j = 0
		while j < len(listcon_catdong):
			if(len(listcon_catdong[j]) > 0):
				list_catdong.append(listcon_catdong[j])
			j += 1
		i += 1

	list_doan_vie = list_catdong


	############################################################################
	#tách từng đoạn tiếng anh từ file eng.txt do người viết bỏ vào list_doan_eng

	path_file_eng = entry_2_text.get()
	file_txt_eng = open(path_file_eng, encoding="utf-8")
	lst_eng = file_txt_eng.readlines()

	list_catdong = []

	i = 0
	while i < len(lst_eng):
		listcon_catdong = lst_eng[i].splitlines()
		j = 0
		while j < len(listcon_catdong):
			if(len(listcon_catdong[j]) > 0):
				list_catdong.append(listcon_catdong[j])
			j += 1
		i += 1

	list_doan_eng = list_catdong


	
	file3 = open('result_0.6_full_final.txt',"w", encoding='utf-8')
	dem = 1
	i = 0
	#len(list_doan_vie)
	while i < 20:
		lb_3.config(text="Đang thực thi: " +str(i+1)+ "/20" )
		translator = Translator()
		strEng_may = translator.translate(list_doan_vie[i], dest='en')
		j = 0
		#len(list_doan_eng)
		while j < len(list_doan_eng):
			diff1 = difflib.SequenceMatcher(None, strEng_may.text, list_doan_eng[j])

			print(i,".",j, " - ", diff1.ratio())

			if(diff1.ratio() > 0.6):
				print(dem)
				file3.write(str(dem) + ". ĐỘ TƯƠNG ĐƯƠNG: " + str(round(diff1.ratio(), 2)) + "\n\t" + list_doan_vie[i] + "\n\t" + list_doan_eng[j] +"\n")
				dem += 1
			#end if
			j += 1

		#end while con	
		i += 1
	#end while
	lb_3.config(text="Xong !" +"\n"+ "File kết quả được lưu ở: E:/_Desktop/DoAn_1/python_app/harryP1_txt_eng.txt")


	"""
	file_test = open('result_test.txt',"w", encoding='utf-8')
	file_test.write( str(len(list_doan_vie)) +"\n"+ str(len(list_doan_eng)) )
	lb_3.config(text="Xong !" +"\n"+ "File kết quả được lưu ở: E:/_Desktop/DoAn_1/python_app/harryP1_txt_eng.txt")
	"""
#end def func_ThucThi




###########################################################
# thiết kế giao diện bằng Tkinter

def print_test():
	str_printtest = entry_2_text.get()
	lb_3.config(text=str_printtest)

def choose_Vie_TextFile():
	root.filename = filedialog.askopenfilename(initialdir = "/",title = "Chọn file Text nội dung tiếng VIỆT",filetypes = (("Text files","*.txt"),("all files","*.*")))
	entry_1_text.set(root.filename)

def choose_Eng_TextFile():
	root.filename = filedialog.askopenfilename(initialdir = "/",title = "Chọn file Text nội dung tiếng ANH",filetypes = (("Text files","*.txt"),("all files","*.*")))
	entry_2_text.set(root.filename)

#khởi tạo Form giao diện, vị trí xuất hiện và tiêu đề của Form
root = Tk()
root.geometry("+610+155")
root.title("Do An 1")


#khởi tạo các componemt có trong giao diện: các label, button, entry (textbox)
lb_title = Label(root, text="Xây dựng tập dữ liệu cặp câu song ngữ Anh-Việt.", fg="blue", font="Times 16 bold")
lb_br1 = Label(root, text="")
lb_br2 = Label(root, text="")
lb_br3 = Label(root, text="")
lb_1 = Label(root, text="Chọn file text chứa nội dung tiếng VIỆT:")
lb_2 = Label(root, text="Chọn file text chứa nội dung tiếng ANH:")
btn_1 = Button(root, text="Chọn", fg="red", command=choose_Vie_TextFile)
btn_2 = Button(root, text="Chọn", fg="red", command=choose_Eng_TextFile)
btn_3 = Button(root, text="Thực thi", fg="blue", command=func_ThucThi)
entry_1_text = StringVar()
entry_2_text = StringVar()
entry_1 = Entry(root, width=50, textvariable=entry_1_text)
entry_2 = Entry(root, width=50, textvariable=entry_2_text)


#sắp xếp vị trí xuất hiện của các componemt trong giao diện, ở đây là sắp xếp theo Gird Layout
lb_title.grid(row=0, sticky=N, columnspan=2)
lb_br1.grid(row=1)

lb_1.grid(row=2)
entry_1.grid(row=3); btn_1.grid(row=3, column=1)


lb_2.grid(row=4)
entry_2.grid(row=5); btn_2.grid(row=5, column=1)

lb_br2.grid(row=6)
btn_3.grid(row=7, columnspan=2)

lb_br3.grid(row=8)
lb_3 = Label(root, text="")
lb_3.grid(row=9, columnspan=2)

#chạy giao diện
root.mainloop()